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