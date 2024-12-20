# モックデータ
MOCK_SUBJECTS = [
    {"subject_id": "1", "subject_name": "コラボレイティブ開発特論", "teacher_name": "中鉢 欣秀", "reviews": ["グループワーク主体の講義"]},
    {"subject_id": "2", "subject_name": "ネットワークシステム特別講義", "teacher_name": "飛田 博章", "reviews": ["楽しい講義"]},
    {"subject_id": "3", "subject_name": "セキュアシステム管理運用特論", "teacher_name": "真鍋 敬士", "reviews": ["資料が豊富", "課題が多かった"]},
]

def get_subjects():
    # DynamoDBの代わりにモックデータを返す
    return MOCK_SUBJECTS