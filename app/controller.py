import json
import uuid
from datetime import datetime
from decimal import Decimal  # Decimal をインポート
from app.model import get_review_table  # model.py からテーブル取得関数をインポート
from app.model import get_subjects
from app.model import get_reviews
from app.view import format_response
from app.view import format_review_response

def health_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "ok"
        }),
        
    }

def subject_handler(event, context):
    keyword = event.get('queryStringParameters', {}).get('q', '')
    subjects = get_subjects()
    
    if keyword:
        filtered_subjects = [
            s for s in subjects 
            if keyword in s['subject_name']
        ][:10]  # キーワード検索結果の上位10件
    else:
        filtered_subjects = subjects[:10]  # 全件取得の場合の上位10件
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(format_response(filtered_subjects))
    }
    
def review_handler(event, context):
    try:
        import json
        print(f"Received event: {json.dumps(event)}")

        # クエリパラメータから `subject_id` を取得
        subject_id = event.get('queryStringParameters', {}).get('subject_id', '')
        print(f"Extracted subject_id: {subject_id}")

        # レビューを取得
        reviews = get_reviews(subject_id)
        print(f"Reviews: {reviews}")

        # 整形されたレスポンスを返す
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps(format_review_response(reviews))
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"message": str(e)})
        }

def review_post_handler(event, context):
    try:
        # DynamoDBテーブルを取得
        table = get_review_table()

        # API Gatewayから受け取ったリクエストボディをパース
        if 'body' not in event or not event['body']:
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({'error': 'Request body is missing'})
            }

        body = json.loads(event['body'])

        # 必須フィールドのチェック（idは除外）
        required_fields = ['subject_id', 'rating', 'workload', 'comment']
        for field in required_fields:
            if field not in body:
                return {
                    "statusCode": 400,
                    "headers": {
                        "Content-Type": "application/json",
                        "Access-Control-Allow-Origin": "*"
                    },
                    "body": json.dumps({'error': f'Missing required field: {field}'})
                }

        # 一意のIDを生成
        unique_id = str(uuid.uuid4())

        # 現在時刻をISO 8601形式で作成
        created_time = datetime.utcnow().isoformat() + "Z"

        # レコード作成
        item = {
            'id': unique_id,  # 生成した一意のIDを使用
            'subject_id': body['subject_id'],
            'rating': Decimal(str(body['rating'])),  # floatをDecimalに変換
            'workload': body['workload'],
            'comment': body['comment'],
            'created': created_time
        }

        # データをDynamoDBに挿入
        table.put_item(Item=item)

        # 成功レスポンスを返す
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                'message': 'Review created successfully',
                'id': unique_id,  # 生成したIDをレスポンスに含める
                'created': created_time
            })
        }

    except Exception as e:
        # エラー時のレスポンス
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({'error': str(e)})
        }
