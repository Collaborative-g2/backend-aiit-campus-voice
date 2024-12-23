def subject_detail(subjects): 
    return [
        {
            "id": str(subject["id"]), 
            "subject_id": subject["subject_id"],
            "term": subject["term"],
            "rating": subject["rating"],
            "workload": subject["workload"],
            "comment": subject["comment"],
            "created": subject["created"]
        }
        for subject in subjects
    ]


