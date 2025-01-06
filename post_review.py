import json

# サンプルデータ (subject_nameに基づいて検索するデータ)
sample_data = [
    {"id": "1", "subject_name": "ネットワーク特論", "term": "2", "rating": "2", "workload": "Sample workload for subject 1.", "comment": "Sample comment for subject 1."},
    {"id": "2", "subject_name": "オブジェクト指向プログラミング特論", "term": "1", "rating": "3", "workload": "Sample workload for subject 2.", "comment": "Sample comment for subject 2."},
    {"id": "3", "subject_name": "プロジェクトマネジメント特論1", "term": "2", "rating": "4", "workload": "Sample workload for subject 3.", "comment": "Sample comment for subject 3."},
    # その他データ
]

def lambda_handler(event, context):
    # クエリパラメータを取得 (subject_name)
    query_params = event.get('queryStringParameters', {})
    subject_name = query_params.get('subject_name', None)
    
    # subject_nameが提供されていない場合のエラーレスポンス
    if not subject_name:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "subject_name query parameter is required"})
        }
    
    # subject_nameに基づいてサンプルデータを検索
    filtered_data = [item for item in sample_data if subject_name.lower() in item['subject_name'].lower()]
    
    # 該当するデータが見つからない場合のレスポンス
    if not filtered_data:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": f"No subjects found for {subject_name}"})
        }
    
    # 結果を返すレスポンス
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": f"Subjects found for '{subject_name}'",
            "data": filtered_data
        })
    }

