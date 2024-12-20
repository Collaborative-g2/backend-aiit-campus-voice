def format_response(subjects):
    return [
        {
            "subject_name": subject.get("subject_name"),
            "teacher_name": subject.get("teacher_name"),
            "reviews": subject.get("reviews"),
        }
        for subject in subjects
    ]