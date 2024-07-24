# tee ratkaisusi tänne
class Course:
    def __init__(self, name: str, grade: int, credits: int) -> None:
        self.name = name
        self.grade = grade
        self.credits = credits

    @property
    def name(self) -> str:
        return self.__name

    @property
    def grade(self) -> int:
        return self.__grade

    @property
    def credits(self) -> int:
        return self.__credits

    @name.setter
    def name(self, new_name: str) -> None:
        if not new_name:
            raise ValueError('Empty value is not valid!')

        self.__name = new_name

    @grade.setter
    def grade(self, new_grade: int) -> None:
        if new_grade < 0:
            raise ValueError('Negative grade is not valid')

        self.__grade = new_grade

    @credits.setter
    def credits(self, new_credits: int) -> None:
        if new_credits < 0:
            raise ValueError('Negative credits is not valid')

        self.__credits = new_credits

    def __str__(self) -> str:
        return f'{self.__name} ({self.__credits} cr) grade {self.__grade}'


class CourseRecordsApplication:
    def __init__(self) -> None:
        self.__courses = {}

    @property
    def records(self) -> None:
        return self.__courses

    def add_course(self, name, grade, credits) -> None:
        if name not in self.__courses:
            course: Course = Course(name, grade, credits)
            self.__courses[name] = course
        else:
            course: Course = self.__courses[name]
            if grade > course.grade:
                course.grade = grade

    def get_course(self, name: str) -> None:
        # course: Course = self.__courses[name]
        # course: Course = self.__courses.get(name, None)
        try:
            course: Course = self.__courses[name]
        except KeyError:
            course = None

        if course == None:
            print('no entry for this course')
        else:
            print(course)

    def get_statistics(self) -> None:
        completed_courses: int = 0
        total_credits: int = 0
        mean: int = 0
        grade_distribution: dict = { 5: '', 4: '', 3: '', 2: '', 1: '' }

        for course in self.__courses.values():
            completed_courses += 1
            total_credits += course.credits
            mean += course.grade
            grade_distribution[course.grade] += 'x'

        print(f'{completed_courses} completed courses, a total of {total_credits} credits')
        print(f'mean {(mean / completed_courses):.1f}')
        print('grade distribution')

        for key, value in grade_distribution.items():
            print(f'{key}: {value}')


class UserInterface:
    def __init__(self) -> None:
        self.__records = CourseRecordsApplication()

    def __help(self) -> None:
        print('1 add course')
        print('2 get course data')
        print('3 statistics')
        print('0 exit')

    def run(self) -> None:
        self.__help()

        while True:
            print('')
            command = input('command: ')

            if command == '0':
                break
            elif command == '1':
                name: str = input('course: ')
                grade: int = int(input('grade: '))
                credits: int = int(input('credits: '))

                self.__records.add_course(name, grade, credits)
            elif command == '2':
                name: str = input('course: ')

                self.__records.get_course(name)
            elif command == '3':
                self.__records.get_statistics()
            else:
                self.__help()


ui = UserInterface()
ui.run()
