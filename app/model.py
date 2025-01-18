import boto3
from boto3.dynamodb.conditions import Key


# DynamoDBクライアントの作成
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SubjectTable')
review_table = dynamodb.Table('ReviewTable') 

def get_subjects():
    response = table.scan()
    return response.get("Items", [])
    
def get_reviews(subject_id=None):
    try:
        if subject_id:
            print(f"Querying DynamoDB with subject_id: {subject_id}")
            #response = review_table.query(
            #    KeyConditionExpression=Key('subject_id').eq(subject_id)
            #)
            response = review_table.query(
                IndexName="CreatedIndex",  # GSIを使用
                KeyConditionExpression=Key('subject_id').eq(subject_id),
                ScanIndexForward=False,  # 降順で取得
            )
            print(f"DynamoDB Query Response: {response}")
        else:
            # subject_idが指定されていない場合、テーブル全体から最新順で5件を取得
            print("No subject_id provided. Fetching the latest 5 reviews.")
            response = review_table.scan()  # テーブル全体をスキャン
            items = response.get('Items', [])
            print(f"Raw Items from Scan: {items}")

            # createdで降順ソートして最新5件を取得
            items = sorted(
                items,
                key=lambda x: x.get('created', ''),  # createdフィールドでソート
                reverse=True  # 降順
            )[:5]  # 最初の5件を取得
            response['Items'] = items  # ソート後のデータをレスポンスに反映

            print(f"Sorted and Limited Items: {items}")
        
        items = response.get('Items', [])
        print(f"Raw Items: {items}")

        formatted_items = [
            {
                'id': item.get('id', ''),
                'subject_id': item.get('subject_id', ''),
                'term': item.get('term', 0),
                'rating': float(item.get('rating', 0)),  # Decimalをfloatに変換
                'workload': item.get('workload', ''),
                'comment': item.get('comment', ''),
                'created': item.get('created', '')
            }
            for item in items
        ]
        print(f"Formatted Items: {formatted_items}")

        return formatted_items
    except Exception as e:
        print(f"Error in get_reviews: {str(e)}")
        return []
    

# テーブルオブジェクトを取得
def get_review_table():
    return dynamodb.Table('ReviewTable')  # DynamoDBテーブル名を正しく設定