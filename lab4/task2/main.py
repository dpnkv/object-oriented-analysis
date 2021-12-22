from classes import CourseFactory, course_to_json

if __name__ == "__main__":
    factory = CourseFactory()
    teacher1 = factory.create_teacher("Jack Nicholson")
    course1 = factory.create_local_course("Python and OOP", teacher1, "Introduction", "Differences", "Similarities")
    course2 = factory.create_offsite_course("Deep Python", teacher1, "Short introduction", "Some great techniques")
    print(course1)
    print(course2)
    course_to_json(course1)
    course_to_json(course2)
