def average_handler(event, context):
    # reviewsリスト
    reviews = event.get("reviews", [])
    
    # 各レビューrating
    ratings = [review.get("rating", 0) for review in reviews]
    
    # 平均値を計算
    average_rating = round(sum(ratings) / len(ratings), 2) if ratings else 0
    
    # 出力用JSONを作成
    result = {
        "average": average_rating,
        "reviews": reviews  
    }
    
    # 結果JSON形式
    return {
        "statusCode": 200,
        "body": json.dumps(result, ensure_ascii=False)
    }
