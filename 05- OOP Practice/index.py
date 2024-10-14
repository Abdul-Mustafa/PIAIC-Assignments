
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


class Teacher(Human):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


class ClassSection:
    def __init__(self, section_name, start_time, end_time, teachers):
        self.section_name = section_name
        self.start_time = start_time
        self.end_time = end_time
        self.teachers = teachers  # List of teacher objects assigned to this section
        self.students = []  # List to hold students enrolled in this section

    def enroll_student(self, student):
        """Enroll a student in the class section."""
        self.students.append(student)

    def display_class_info(self):
        """Display information about the class section."""
        print(f"Class Section: {self.section_name}")
        print("Teachers: ")
        for teacher in self.teachers:
            print(f"- {teacher.name} ({teacher.subject})")
        print(f"Timings: {self.start_time} - {self.end_time}")
        print("Enrolled Students:")
        for student in self.students:
            print(f"- {student.name} (ID: {student.student_id})")


class University:
    def __init__(self, name):
        self.name = name
        self.students = []  # List to hold all students
        self.teachers = []  # List to hold all teachers
        self.class_sections = []  # List to hold all class sections

    def add_student(self, student):
        """Add a student to the university."""
        self.students.append(student)

    def add_teacher(self, teacher):
        """Add a teacher to the university."""
        self.teachers.append(teacher)

    def add_class_section(self, class_section):
        """Add a class section to the university."""
        self.class_sections.append(class_section)


if __name__ == "__main__":
    # Create a university
    uni = University("National Textile University")


    student1 = Student("Abdul Mustafa", 30, "PIAIC79479")


    teacher1 = Teacher("Abu Hurairah", 25, "Mathematics")
    teacher2 = Teacher("Naveed Sarwar", 32, "Physics")


    uni.add_student(student1)
    uni.add_teacher(teacher1)
    uni.add_teacher(teacher2)

    piaic_class = ClassSection("PIAIC BATCH 65", "2:00 PM", "6:00 PM", [teacher1, teacher2])
    piaic_class.enroll_student(student1)
    

    uni.add_class_section(piaic_class)


    piaic_class.display_class_info()
