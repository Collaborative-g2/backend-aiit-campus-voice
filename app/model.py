import boto3

# DynamoDBクライアントの作成
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SubjectTable')

def get_subjects():
    response = table.scan()
    return response.get("Items", [])