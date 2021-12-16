import json
from abc import ABC, abstractmethod


class ICourse(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @property
    @abstractmethod
    def program(self):
        pass

    @program.setter
    @abstractmethod
    def program(self, program):
        pass


class ITeacher(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass


class ICourseFactory(ABC):
    @abstractmethod
    def create_local_course(self, name, teacher, *program):
        pass

    @abstractmethod
    def create_offsite_course(self, name, teacher, *program):
        pass

    @abstractmethod
    def create_teacher(self, name):
        pass


class ILocalCourse(ICourse):
    @property
    @abstractmethod
    def name(self):
        pass

    @ICourse.name.setter
    @abstractmethod
    def name(self, name):
        pass

    @property
    @abstractmethod
    def program(self):
        pass

    @ICourse.program.setter
    @abstractmethod
    def program(self, program):
        pass


class IOffsiteCourse(ICourse):
    @property
    @abstractmethod
    def name(self):
        pass

    @ICourse.name.setter
    @abstractmethod
    def name(self, name):
        pass

    @property
    @abstractmethod
    def program(self):
        pass

    @ICourse.program.setter
    @abstractmethod
    def program(self, program):
        pass


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

    def to_dict(self):
        return json.loads(json.dumps(self, default=vars))


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

    def to_dict(self):
        return json.loads(json.dumps(self, default=vars))


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
    with open("courses.json") as courses_file:
        courses = json.load(courses_file)
    courses.append(course.to_dict())
    with open("courses.json", 'w') as courses_file:
        json.dump(courses, courses_file, indent=4)


if __name__ == "__main__":
    factory = CourseFactory()
    teacher1 = factory.create_teacher("Jack Nicholson")
    course1 = factory.create_local_course("Test", teacher1, "Topic1", "Topic2")
    course2 = factory.create_offsite_course("Test2", teacher1, "Topic3", "Topic4")
    print(course1)
    print(course2)
    course_to_json(course1)
    course_to_json(course2)
