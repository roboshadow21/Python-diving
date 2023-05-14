import csv
from descriptor import Validator
from pathlib import Path


class Student:

    """Class Student. Stores information about students, subjects studied, grades, and test results."""

    name = Validator()
    surname = Validator()
    path = Path('subjects.csv')
    GRADE_MIN = 2
    GRADE_MAX = 5
    TEST_RESULT_MIN = 0
    TEST_RESULT_MAX = 100

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        with open(self.path, 'r', newline='', encoding='utf-8') as f:
            self.__subject_grade = {}
            self.__test_result = {}
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                self.__subject_grade[str(*row)] = 0
                self.__test_result[str(*row)] = 0

    def __str__(self):
        return f'Student "{self.name} {self.surname}" subject grades: {self.__subject_grade}, ' \
               f'test result: {self.__test_result}'

    def set_subject_grade(self, subject: str, grade: int) -> dict[str, int]:
        """The method allows you to enter and store grades for the subject being studied"""
        if subject in self.__subject_grade and self.GRADE_MIN <= grade <= self.GRADE_MAX:
            self.__subject_grade[subject] = grade
        elif subject not in self.__subject_grade:
            raise KeyError(f'Subject {subject} is not exist')
        elif self.GRADE_MAX < grade or grade < self.GRADE_MIN:
            raise ValueError(f'Grade should be between {self.GRADE_MIN} and {self.GRADE_MAX}')
        return self.__subject_grade

    def set_test_result(self, subject: str, grade: int) -> dict[str, int]:
        """The method allows you to enter and store test results for the subject being studied"""
        if subject in self.__test_result and self.TEST_RESULT_MIN <= grade <= self.TEST_RESULT_MAX:
            self.__test_result[subject] = grade
        elif subject not in self.__test_result:
            raise KeyError(f'Subject {subject} is not exist')
        elif self.TEST_RESULT_MAX < grade or grade < self.TEST_RESULT_MIN:
            raise ValueError(f'Grade should be between {self.TEST_RESULT_MIN} and {self.TEST_RESULT_MAX}')
        return self.__test_result

    def calculate_average(self):
        """Method for calculating the average score of grades and test results in all subjects"""
        spam = 0
        eggs = 0
        for grade in self.__subject_grade.values():
            spam += grade
        average_grade = spam // len(self.__subject_grade)
        for test in self.__test_result.values():
            eggs += test
        average_test = eggs // len(self.__test_result)
        return f'Student {self.name} {self.surname} has average grade = {average_grade}, average test = {average_test}'


if __name__ == '__main':
    s = Student('John', 'Doe')
    print(s.name, s.surname)
    print(s)
    s.set_subject_grade('math', 4)
    # s.set_subject_grade('geography', 4)
    s.set_subject_grade('history', 3)
    s.set_subject_grade('biology', 5)
    s.set_subject_grade('chemistry', 5)
    s.set_test_result('math', 87)
    s.set_test_result('biology', 90)
    s.set_test_result('history', 65)
    s.set_test_result('chemistry', 90)

    print(s)
    print(s.calculate_average())
