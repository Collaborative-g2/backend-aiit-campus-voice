import json

# データベースに相当するJSONデータ
data = [
    {"id": "1", "subject_id": "ISA001", "subject_name": "ネットワーク特論", "professor": "迫川 修", "course": "情報アーキテクチャ"},
    {"id": "36", "subject_id": "ISA036", "subject_name": "データマネジメント特論", "professor": "浪岡 保男", "course": "情報アーキテクチャ"},
    # 他のデータは省略
]

def lambda_handler(event, context):
    # クエリパラメータから `subject_name` を取得
    query_params = event.get("queryStringParameters", {})
    subject_name = query_params.get("subject_name") if query_params else None

    if not subject_name:
        # 必須パラメータがない場合は400エラーを返す
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "subject_name is required"})
        }

    # データ検索
    result = next((item for item in data if item["subject_name"] == subject_name), None)

    if result:
        # 一致するデータが見つかった場合
        response = {
            "subject_name": result["subject_name"],
            "professor": result["professor"],
            "course": result["course"],
            "subject_id": result["subject_id"],
            "id": result["id"]
        }
        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }
    else:
        # 一致するデータが見つからない場合
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "Subject not found"})
        }

