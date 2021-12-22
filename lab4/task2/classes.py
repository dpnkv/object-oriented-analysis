import json
from interfaces import ITeacher, ILocalCourse, IOffsiteCourse, ICourseFactory


class LocalCourse(ILocalCourse):
    def __init__(self, name, teacher, *program):
        self.name = name
        self.teacher = teacher
        self.program = program

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not name:
            raise ValueError("Name cannot be empty")
        self.__name = name

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("Teacher must be a Teacher object")
        if not teacher:
            raise ValueError("Teacher cannot be empty")
        self.__teacher = teacher

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, program):
        if not program:
            raise ValueError("Program cannot be empty")
        if not all(isinstance(topic, str) for topic in program):
            raise TypeError("Each topic must be a string")
        self.__program = list(program)

    def __str__(self):
        return f"Local: {self.name}, teacher: {self.teacher}, program: {self.program}"

    def __iter__(self):
        for key, value in self.__dict__.items():
            i = str(key).find("__")
            if i != -1:
                key = str(key)[i + 2:]
            yield key, value


class OffsiteCourse(IOffsiteCourse):
    def __init__(self, name, teacher, *program):
        self.name = name
        self.teacher = teacher
        self.program = program

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not name:
            raise ValueError("Name cannot be empty")
        self.__name = name

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("Teacher must be a Teacher object")
        if not teacher:
            raise ValueError("Teacher cannot be empty")
        self.__teacher = teacher

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, program):
        if not program:
            raise ValueError("Program cannot be empty")
        if not all(isinstance(topic, str) for topic in program):
            raise TypeError("Each topic must be a string")
        self.__program = list(program)

    def __str__(self):
        return f"Offsite: {self.name}, teacher: {self.teacher}, program: {self.program}"

    def __iter__(self):
        for key, value in self.__dict__.items():
            i = str(key).find("__")
            if i != -1:
                key = str(key)[i + 2:]
            yield key, value


class Teacher(ITeacher):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not name:
            raise ValueError("Name cannot be empty")
        self.__name = name

    def __str__(self):
        return f"{self.name}"


class CourseFactory(ICourseFactory):
    def create_local_course(self, name, teacher, *program):
        return LocalCourse(name, teacher, *program)

    def create_offsite_course(self, name, teacher, *program):
        return OffsiteCourse(name, teacher, *program)

    def create_teacher(self, name):
        return Teacher(name)


def course_to_json(course):
    """Function to serialize course to json."""
    with open("courses.json") as courses_file:
        courses = json.load(courses_file)
    courses.append(dict(course))
    with open("courses.json", 'w') as courses_file:
        json.dump(courses, courses_file, indent=4, default=str)
