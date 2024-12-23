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