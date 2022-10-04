class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
        
    
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def grade_1(self):
        sum_grades = 0
        amount = 0
        for i in self.grades.values():
            for grade in i:
                sum_grades += grade
                amount += 1
        average_rating = sum_grades / amount
        return round(average_rating, 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Невозможно сравнить")
            return
        return self.grade_1() < other.grade_1()

    def __str__(self):
        res = f"Имя: {self.name}\n"\
              f"Фамилия: {self.surname}\n"\
              f"Средняя оценка за домашние задания: {self.grade_1()}\n"\
              f"Курсы в процессе изучения: {self.courses_in_progress}\n"\
              f"Завершенные курсы: {self.finished_courses}"
        return res
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades_lecturer = {}
        

    def __str__(self):
        res = f"Имя: {self.name} \n"\
              f"Фамилия: {self.surname} \n"\
              f"Средняя оценка за лекции: {self.grade_2()}"
        return res

    def grade_2(self):
        sum_grades = 0
        amount = 0
        for i in self.grades_lecturer.values():
            for grade in i:
                sum_grades += grade
                amount += 1
        average_rating = sum_grades / amount
        return round(average_rating, 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Невозможно сравнить")
            return
        return self.grade_2() < other.grade_2()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        res = f"Имя: {self.name}\n"\
              f"Фамилия: {self.surname}"
        return res


student1 = Student('Иван', 'Потапов', 'м')
student1.finished_courses += ['GIT']
student1.courses_in_progress += ['Python']

student2 = Student('Дарья', 'Романова', 'ж')
student2.finished_courses += ['GIT']
student2.courses_in_progress += ['Python']
 
lecturer1 = Lecturer('Владимир', 'Попов')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Андрей', 'Козлов')
lecturer2.courses_attached += ['Python']

reviewer1 = Reviewer('Анатолий', 'Лопатов')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Виктория', 'Шпак')
reviewer2.courses_attached += ['Python']

student_list = [student1, student2]
lecturer_list = [lecturer1, lecturer2]


def average_hw(students, course_name):
    sum_grade = 0
    amount = 0
    for student in students:
        for key, value in student.grades.items():
            if course_name in key:
                sum_grade += sum(value) / len(value)
                amount += 1
    return sum_grade / amount

def average_lecture(lecturers, course_name):
    sum_grade = 0
    amount = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades_lecturer.items():
            if course_name in key:
                sum_grade += sum(value) / len(value)
                amount += 1
    return sum_grade / amount

#Оценки
student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer2, 'Python', 3)
student2.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Python', 4)

reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 3)
reviewer2.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 4)

print(f'Средняя оценка за домашнюю работу по Python: {average_hw(student_list, "Python")}')
print(f'Средняя оценка за лекции по Python: {average_lecture(lecturer_list, "Python")}')
print(f'Средняя оценка за домашнюю работу у Потапова выше чем у Романовой {student1 < student2}')
print(f'Средняя оценка за лекцию у Попова выше чем у Козлова {lecturer1 < lecturer2}')

#__str__
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)