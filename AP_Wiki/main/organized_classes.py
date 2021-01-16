import pandas as pd

classes = []
data = pd.read_csv('main/ap-courses.csv', delimiter="_", engine="python")

names = data.Name
subjects = data.Subject
descriptions = data.Description
difficulties = data.Difficulty
values = data.Value

for i in range(len(data)):
    course = {
        "name": names[i],
        "subject": subjects[i],
        "description": descriptions[i],
        "difficulty": difficulties[i],
        "value": values[i]
    }
    classes.append(course)
filtered_classes = []
subjects = ['math', 'science', 'english', 'social studies', 'language', 'arts', 'computer science']
for subject in subjects:
    for course in classes:
        if course["subject"] == subject:
            filtered_classes.append(course)