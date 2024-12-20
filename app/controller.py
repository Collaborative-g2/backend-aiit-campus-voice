import json
from app.model import get_subjects
from app.view import format_response

def health_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "ok"
        }),
    }

def top_handler(event, context):
    # DynamoDBから取得する代わりにモックデータを使用
    subjects = get_subjects()
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(format_response(subjects))
    }