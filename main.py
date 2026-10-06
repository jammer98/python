# students = [
#     {"name": "Asha", "score": 82},
#     {"name": "Ravi", "score": 45},
#     {"name": "Meena", "score": 60},
#     {"name": "Kiran", "score": 91},
# ]

# passed = [s["name"] for s in students if s["score"] >= 60]

# print(passed)

sum_of_all_students = 0 

# for s in students:
#     sum_of_all_students += s["score"]

# average = sum_of_all_students / len(students)

# print(f"average of all students : {round(average,2)}")

# for s in students:
#     if s["score"] >= 90:
#         s["grade"] = "distinction"
#     elif s["score"] >= 60:
#         s["grade"] = "pass"
#     else:
#         s["grade"] = "fail"


# graded = [
#     {**s,
#     "grade":"distinction" if s["score"] >= 90 
#     else "pass" if s["score"] >= 60
#     else "fail"}
#     for s in students
# ]
# print(graded)


from grading import average_score,Student

# data = [
#     {"name": "Asha", "score": 182},
#     {"name": "Ravi"},
#     {"name": "Meena", "score": 150},
#     {"name": "Kiran", "score": 291},
#     {"name": "Dev", "score": "abc"}
# ]

students = []


# try:
#     print(f"Average of valid students is: {average_score(students)}")
# except ValueError as e :
#     print("No average:",e)

import json

try:
    with open("students.json") as f:
        data = json.load(f)

except FileNotFoundError:
    print("File not found")
    data = []

except json.JSONDecodeError:
    print("Invalid JSON")
    data = []

students = []

for d in data:
    try:
        s = Student(d["name"], d["score"])
        students.append(s)
    except (KeyError, ValueError, TypeError) as e:
        print(f"skipping bad record: {d} ({type(e).__name__})")
        continue

results = []

for s in students:
    results.append({
        "name": s.name,
        "score": s.score,
        "grade": s.grade()
    })

with open("graded.json", "w") as f:
    json.dump(results, f, indent=2)

















# a = Student("Ram",93)
# b = Student("Alex",87)

# print(f"{a.name} grade is {a.grade()}")
# print(f"{b.name} grade is {b.grade()}")

# print(f" Average score is {average_score([a,b])}")
# print(f" Average score is {average_score([])}")





    

