from abc import ABC, abstractmethod

# ---------------- Person ----------------
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @abstractmethod
    def get_role(self):
        pass

# ---------------- Student ----------------
class Student(Person):
    def __init__(self, student_id, name, age):
        super().__init__(name, age)
        self.student_id = student_id
        self.enrolled_courses = []
    
    def get_role(self):
        return 'Student'

    def get_enrolled_courses(self):
        print(self.enrolled_courses)

    def add_course(self, course):
        self.enrolled_courses.append(course)

# ---------------- Teacher ----------------
class Teacher(Person):
    def __init__(self, teacher_id, name, age):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.assigned_courses = []
    
    def get_role(self):
        return 'Teacher'

    def get_assigned_courses(self):
        print(self.assigned_courses)

    def add_assigned_course(self, course):
        self.assigned_courses.append(course)

# ---------------- Course ----------------
class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.teacher = None
        self.students = []

    def set_teacher(self, teacher):
        self.teacher = teacher
        teacher.add_assigned_course(self.course_name)

    def enroll_student(self, student):
        self.students.append(student)
        student.add_course(self.course_name)

    def course_info(self):
        print(f"\nCourse: {self.course_name} ({self.course_code})")
        print(f"Teacher: {self.teacher.name if self.teacher else 'Not Assigned'}")
        print("Students Enrolled:")
        for s in self.students:
            print(f"- {s.name} (ID: {s.student_id})")


# ---------------- Department ----------------
class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def list_courses(self):
        print(f"\nCourses in {self.dept_name} Department:")
        for c in self.courses:
            print(f"- {c.course_name} ({c.course_code})")


# ---------------- Administration ----------------
class Administration:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.departments = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added.")

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"Teacher {teacher.name} added.")

    def add_department(self, department):
        self.departments.append(department)
        print(f"Department {department.dept_name} added.")

# Student enrolled courses
st1 = Student(1, 'Anwar', 22)
st1.add_course("Python")
st1.add_course("HTML")
st1.add_course("CSS")
st1.get_enrolled_courses()

# Teacher assigned courses
t1 = Teacher(101, 'Ravi', 25)
t1.add_assigned_course("Python")
t1.add_assigned_course("HTML")
t1.add_assigned_course("CSS")
t1.get_assigned_courses()

# Create Administration
admin = Administration()

# Create Department
cs = Department("Computer Science")
admin.add_department(cs)

# Create Courses
course1 = Course("Python Programming", "CS101")
course2 = Course("Web Development", "CS102")
cs.add_course(course1)
cs.add_course(course2)

# Create Teacher
t2 = Teacher(102, "Alice", 30)
admin.add_teacher(t2)

# Assign teacher to a course
course1.set_teacher(t2)

# Create Students
st2 = Student(2, "Rahul", 21)
st3 = Student(3, "Megha", 23)
admin.add_student(st2)
admin.add_student(st3)

# Enroll students into courses
course1.enroll_student(st2)
course1.enroll_student(st3)
course2.enroll_student(st2)

# Show Outputs
t2.get_assigned_courses()
st2.get_enrolled_courses()
st3.get_enrolled_courses()

course1.course_info()
course2.course_info()
cs.list_courses()




