def format_response(subjects):
    return [
        {
            "subject_name": subject.get("subject_name"),
            "professor": subject.get("professor"),
            "course": subject.get("course"),
            "subject_id": subject.get("subject_id"),
            "id": subject.get("id")
        }
        for subject in subjects
    ]

def format_review_response(reviews):
    return [
        {
            "id": review.get("id"),
            "subject_id": review.get("subject_id"),
            "term": review.get("term"),
            "rating": review.get("rating"),
            "workload": review.get("workload"),
            "comment": review.get("comment"),
            "created": review.get("created")
        }
        for review in reviews
    ]