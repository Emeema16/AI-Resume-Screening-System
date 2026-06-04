resume = input("Enter resume skills: ")
job = input("Enter required skills: ")

resume_skills = set(resume.lower().split(","))
job_skills = set(job.lower().split(","))

matched = resume_skills.intersection(job_skills)

score = (len(matched) / len(job_skills)) * 100

print(f"Match Score: {score:.2f}%")
print("Matched Skills:", matched)
