import json

def review_post_handler(event, context):
    # クエリパラメータを取得 (subject_name)
    query_params = event.get('queryStringParameters', {})
    subject_name = query_params.get('subject_name', None)
    
    # subject_nameをログに記録
    if not subject_name:
        print("subject_name query parameter is required")
    else:
        # subject_nameに基づく処理内容をログに記録
        print(f"Processing review for subject_name: {subject_name}")
    
    # 成功時の200ステータスのみを返す
    return {
        "statusCode": 200,
        "body": ""  # ボディは空
    }

