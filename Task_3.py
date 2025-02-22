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
            if 0 <= grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return "Ошибка: Оценка должна быть от 0 до 10."
        else:
            return 'Ошибка: Лектор не ведет этот курс у этого студента, или передан неверный тип объекта.'

    def _get_average_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        courses_in_progress_str = ", ".join(self.courses_in_progress)
        finished_courses_str = ", ".join(self.finished_courses)
        average_grade = self._get_average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade:.1f}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            return "Ошибка: Сравнение возможно только между студентами."
        return self._get_average_grade() < other._get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return "Ошибка: Сравнение возможно только между студентами."
        return self._get_average_grade() <= other._get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return "Ошибка: Сравнение возможно только между студентами."
        return self._get_average_grade() == other._get_average_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            return "Ошибка: Сравнение возможно только между студентами."
        return self._get_average_grade() != other._get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return "Ошибка: Сравнение возможно только между студентами."
        return self._get_average_grade() > other._get_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return "Ошибка: Сравнение возможно только между студентами."
        return self._get_average_grade() >= other._get_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
         return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _get_average_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        average_grade = self._get_average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка: Сравнение возможно только между лекторами."
        return self._get_average_grade() < other._get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка: Сравнение возможно только между лекторами."
        return self._get_average_grade() <= other._get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка: Сравнение возможно только между лекторами."
        return self._get_average_grade() == other._get_average_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка: Сравнение возможно только между лекторами."
        return self._get_average_grade() != other._get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка: Сравнение возможно только между лекторами."
        return self._get_average_grade() > other._get_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка: Сравнение возможно только между лекторами."
        return self._get_average_grade() >= other._get_average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return super().__str__() # Reuse Mentor's __str__


# Example Usage
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

cool_lecturer = Lecturer('Some', 'Lecturer')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Some', 'Reviewer')
cool_reviewer.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Git', 9)

print(cool_reviewer)
print(cool_lecturer)
print(best_student)

# Comparison Examples
student2 = Student("Another", "Student", "female")
student2.courses_in_progress += ["Python"]
cool_reviewer.rate_hw(student2, 'Python', 6)
cool_reviewer.rate_hw(student2, 'Python', 7)

print(f"best_student > student2: {best_student > student2}") # True
print(f"best_student < student2: {best_student < student2}") # False

lecturer2 = Lecturer("Another", "Lecturer")
lecturer2.courses_attached += ["Python"]
best_student.rate_lecturer(lecturer2, "Python", 5)
best_student.rate_lecturer(lecturer2, "Python", 6)

print(f"cool_lecturer > lecturer2: {cool_lecturer > lecturer2}") # True
print(f"cool_lecturer < lecturer2: {cool_lecturer < lecturer2}") # False