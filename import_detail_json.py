import json
import boto3
import uuid
from datetime import datetime

# DynamoDBクライアントの初期化
dynamodb = boto3.resource('dynamodb')
table_name = "Review Table"  # テーブル名
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # リクエストボディからJSONデータをパース
        body = json.loads(event['body'])
        
        # 必須フィールドのチェック
        required_fields = ['subject_id', 'term', 'rating', 'workload', 'comment']
        for field in required_fields:
            if field not in body:
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": f"Missing required field: {field}"})
                }

        # IDとタイムスタンプを生成
        review_id = str(uuid.uuid4())
        created_timestamp = datetime.utcnow().isoformat()

        # DynamoDBに挿入するデータの準備
        item = {
            "id": review_id,
            "subject_id": body['subject_id'],
            "term": body['term'],
            "rating": body['rating'],
            "workload": body['workload'],
            "comment": body['comment'],
            "created": created_timestamp
        }

        # DynamoDBにデータを保存
        table.put_item(Item=item)

        # レスポンスを返す
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Review saved successfully",
                "id": review_id
            })
        }

    except Exception as e:
        # エラーハンドリング
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

