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
    # DynamoDBから取得する代わりにモックデータを使用
    subjects = get_subjects()
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(format_response(subjects))
    }

def search_handler(event, context):
   keyword = event.get('queryStringParameters', {}).get('q', '')
   subjects = get_subjects()
   
   if keyword:
       filtered_subjects = [
           s for s in subjects 
           if keyword in s['subject_name']
       ]
   else:
       filtered_subjects = subjects

   return {
       "statusCode": 200,
       "headers": {"Content-Type": "application/json"},
       "body": json.dumps(format_response(filtered_subjects))
   }