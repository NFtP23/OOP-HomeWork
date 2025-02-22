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
            raise TypeError("Сравнение возможно только между студентами.")
        return self._get_average_grade() < other._get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Сравнение возможно только между студентами.")
        return self._get_average_grade() <= other._get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Сравнение возможно только между студентами.")
        return self._get_average_grade() == other._get_average_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Сравнение возможно только между студентами.")
        return self._get_average_grade() != other._get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Сравнение возможно только между студентами.")
        return self._get_average_grade() > other._get_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Сравнение возможно только между студентами.")
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
            raise TypeError("Сравнение возможно только между лекторами.")
        return self._get_average_grade() < other._get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Сравнение возможно только между лекторами.")
        return self._get_average_grade() <= other._get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Сравнение возможно только между лекторами.")
        return self._get_average_grade() == other._get_average_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Сравнение возможно только между лекторами.")
        return self._get_average_grade() != other._get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Сравнение возможно только между лекторами.")
        return self._get_average_grade() > other._get_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Сравнение возможно только между лекторами.")
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


# Helper Functions
def calculate_average_hw_grade_for_course(students, course):
    """Calculates the average homework grade for a specific course across all students."""
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    if not total_grades:
        return 0
    return sum(total_grades) / len(total_grades)


def calculate_average_lecture_grade_for_course(lecturers, course):
    """Calculates the average lecture grade for a specific course across all lecturers."""
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    if not total_grades:
        return 0
    return sum(total_grades) / len(total_grades)


# Instances
student1 = Student('Ruoy', 'Eman', 'your_gender')
student2 = Student("Alice", "Smith", "female")
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ["Python", "Java"]

lecturer1 = Lecturer('Some', 'Lecturer')
lecturer2 = Lecturer("Jane", "Doe")
lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ["Java"]

reviewer1 = Reviewer('Some', 'Reviewer')
reviewer2 = Reviewer("John", "Smith")
reviewer1.courses_attached += ['Python', 'Git']
reviewer2.courses_attached += ["Java"]

# Method Calls (with some ratings for demonstration)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Git', 10)
reviewer2.rate_hw(student2, "Java", 8)
student1.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer2, "Java", 9)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

print(f"Average HW grade for Python: {calculate_average_hw_grade_for_course([student1, student2], 'Python')}")
print(f"Average HW grade for Java: {calculate_average_hw_grade_for_course([student1, student2], 'Java')}")
print(f"Average lecture grade for Python: {calculate_average_lecture_grade_for_course([lecturer1, lecturer2], 'Python')}")
print(f"Average lecture grade for Java: {calculate_average_lecture_grade_for_course([lecturer1, lecturer2], 'Java')}")

# Comparison Examples
print(f"student1 > student2: {student1 > student2}")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")