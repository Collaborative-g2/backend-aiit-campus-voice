import json
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
            "body": json.dumps({"message": str(e)})
        }


