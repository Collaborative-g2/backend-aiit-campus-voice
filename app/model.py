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
            response = review_table.query(
                KeyConditionExpression=Key('subject_id').eq(subject_id)
            )
            print(f"DynamoDB Query Response: {response}")
        else:
            response = review_table.scan()
            print(f"DynamoDB Scan Response: {response}")
        
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

        

