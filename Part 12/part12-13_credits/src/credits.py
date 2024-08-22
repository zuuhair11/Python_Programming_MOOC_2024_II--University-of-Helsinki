from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f'{self.course_name} ({self.credits} cr) grade {self.grade}'

# Write your solution
def sum_of_all_credits(courses: list) -> int:
    """First attempt - with passing the default value"""
    def sum_helper(acc: int, cur: CourseAttempt) -> int:
        return acc + cur.credits

    return reduce(sum_helper, courses, 0)

    """Second attempt - without passing the default value"""
    def sum_helper(acc: CourseAttempt, cur: CourseAttempt) -> int:
        if type(acc) == CourseAttempt:
            return acc.credits + cur.credits
        return acc + cur.credits

    return reduce(sum_helper, courses)

    """Third attempt - using lambda"""
    return reduce(lambda acc, cur: acc + cur.credits, courses, 0)

    """Fourth attempt - using lambda + without passing the default value"""
    return reduce(lambda acc, cur: (acc.credits if type(acc) == CourseAttempt else acc) + cur.credits, courses)


def sum_of_passed_credits(courses: list) -> int:
    accepted = filter(lambda course: course.grade > 0, courses)
    return reduce(lambda acc, cur: acc + cur.credits, accepted, 0)


def average(courses: list) -> float:
    accepted = list(filter(lambda course: course.grade > 0, courses))
    return reduce(lambda acc, cur: (acc + cur.grade), accepted, 0) / len(accepted)


if __name__ == '__main__':
    s1 = CourseAttempt('Introduction to Programming', 5, 5)
    s2 = CourseAttempt('Advanced Course in Programming', 0, 5)
    s3 = CourseAttempt('Data Structures and Algorithms', 3, 10)

    ag = average([s1, s2, s3])
    print(ag)
