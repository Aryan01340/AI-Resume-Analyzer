def extract_skills(text, skills_data):

    found_skills = []

    text = text.lower()

    for skill in skills_data["skill"]:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills


def calculate_match(resume_skills, job_skills):

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    if len(job_set) == 0:
        return 0

    matched_skills = resume_set.intersection(job_set)

    score = (
        len(matched_skills) / len(job_set)
    ) * 100

    return round(score, 2)


def get_missing_skills(resume_skills, job_skills):

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    missing_skills = job_set - resume_set

    return list(missing_skills)