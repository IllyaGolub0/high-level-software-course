import os

folder_path = "student_marks"
required_files = ["math.txt", "statistics.txt", "physics.txt", "student_names.txt"]

files_in_dir = os.listdir(folder_path)

print(" Перевірка файлів у папці '" + folder_path + "' ")
for file_name in required_files:
    if file_name in files_in_dir:
        print("Файл існує:", file_name)
    else:
        print("Помилка! Файл відсутній:", file_name)

names_file_path = os.path.join(folder_path, "student_names.txt")
f_names = open(names_file_path, "r", encoding="utf-8")
students_list = []
for line in f_names:
    name = line.strip()
    if name != "":
        students_list.append(name)
f_names.close()

subjects = ["math", "statistics", "physics"]
grades_data = {}

for subj in subjects:
    subj_file_path = os.path.join(folder_path, subj + ".txt")
    f_subj = open(subj_file_path, "r", encoding="utf-8")
    grades_list = []
    for line in f_subj:
        val = line.strip()
        if val != "":
            grades_list.append(int(val))
    f_subj.close()
    grades_data[subj] = grades_list

students_dict = {}
for i in range(len(students_list)):
    student_name = students_list[i]
    students_dict[student_name] = {
        "math": grades_data["math"][i],
        "statistics": grades_data["statistics"][i],
        "physics": grades_data["physics"][i]
    }


print("\n Статистика по кожному студенту ")
avg_scores = {}
for student, subj_grades in students_dict.items():
    total = 0
    for subj, score in subj_grades.items():
        total += score
    avg = total / len(subj_grades)
    avg_scores[student] = avg
    print("студент:", student, ", середня оцінка:", round(avg, 2))

print("\n Топ-3 студенти з найвищими оцінками ")
student_avg_list = []
for name, avg in avg_scores.items():
    student_avg_list.append((name, avg))

for i in range(len(student_avg_list)):
    for j in range(i + 1, len(student_avg_list)):
        if student_avg_list[i][1] < student_avg_list[j][1]:
            student_avg_list[i], student_avg_list[j] = student_avg_list[j], student_avg_list[i]

for i in range(min(3, len(student_avg_list))):
    print("Студент " + str(i + 1) + ": " + student_avg_list[i][0])

print("\n Загальна статистика ")
print("Загальна кількість студентів:", len(students_list))

for subj in subjects:
    scores = grades_data[subj]
    subj_avg = sum(scores) / len(scores)
    subj_min = min(scores)
    subj_max = max(scores)
    print("предмет:", subj, ", середня оцінка", round(subj_avg, 2), ", min оцінка:", subj_min, ", max оцінка:", subj_max)

print("\n Найвищий бал по кожному предмету ")
for subj in subjects:
    best_student = ""
    max_val = -1
    for student, subj_grades in students_dict.items():
        if subj_grades[subj] > max_val:
            max_val = subj_grades[subj]
            best_student = student
    print("Предмет: " + subj + " | студент: " + best_student + " , оцінка: " + str(max_val))

print("\n Студенти з оцінкою нижче 50 ")
low_students = []
for student, avg in avg_scores.items():
    if avg < 50:
        low_students.append(student)

print("Кількість студентів з оцінкою нижче 50:", len(low_students))
for s in low_students:
    print(s)