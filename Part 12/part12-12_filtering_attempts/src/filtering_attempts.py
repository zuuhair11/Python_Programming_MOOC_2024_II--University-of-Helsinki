class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f'{self.student_name}, grade for the course {self.course_name} {self.grade}'


def accepted(attempts: list) -> list:
    """First attempt - using normal function"""
    def at_least_one(course: CourseAttempt) -> bool:
        return course.grade > 0

    return filter(at_least_one, attempts)

    """Second attempt - using lambda"""
    return filter(lambda course: course.grade > 0, attempts)

    """Third attempt - using list comprehension"""
    return [course for course in attempts if course.grade > 0]


if __name__ == '__main__':
    s1 = CourseAttempt('Peter Python', 'Introduction to Programming', 3)
    s2 = CourseAttempt('Olivia C. Objective', 'Introduction to Programming', 5)
    s3 = CourseAttempt('Peter Python', 'Advanced Course in Programming', 0)

    for attempt in accepted([s1, s2, s3]):
        print(attempt)
