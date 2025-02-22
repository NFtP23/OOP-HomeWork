class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('Some', 'Lecturer')
cool_reviewer = Reviewer('Some', 'Reviewer')

cool_lecturer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Python']
