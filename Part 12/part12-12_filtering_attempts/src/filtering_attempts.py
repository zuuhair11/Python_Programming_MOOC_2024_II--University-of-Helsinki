class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f'{self.student_name}, grade for the course {self.course_name} {self.grade}'


def accepted(attempts: list) -> list:
    """First attempt - using named function"""
    def at_least_one(course: CourseAttempt) -> bool:
        return course.grade > 0

    return filter(at_least_one, attempts)

    """Second attempt - using lambda"""
    return filter(lambda course: course.grade > 0, attempts)

    """Third attempt - using list comprehension"""
    return [course for course in attempts if course.grade > 0]


def attempts_with_grade(attempts: list, grade: int) -> list:
    """First attempt - using lambda"""
    # return filter(lambda course: course.grade == grade, attempts)

    """Second attempt - using named function"""
    def check_grade(course: CourseAttempt) -> bool:
        return course.grade == grade

    return filter(check_grade, attempts)

    """Third attempt - using list comprehension"""
    return [course for course in attempts if course.grade == grade]

    """Fourth attempt - using list comprehension with named function"""
    def check_grade(course: CourseAttempt) -> bool:
        return course.grade == grade

    return [course for course in attempts if check_grade(course)]


if __name__ == '__main__':
    s1 = CourseAttempt('Peter Python', 'Introduction to Programming', 3)
    s2 = CourseAttempt('Olivia C. Objective', 'Introduction to Programming', 5)
    s3 = CourseAttempt('Peter Python', 'Introduction to AI', 3)
    s4 = CourseAttempt('Olivia C. Objective', 'Data Structures and Algorithms', 3)

    for attempt in attempts_with_grade([s1, s2, s3, s4], 3):
        print(attempt)
