"""
Includes class Student.
"""
import re

class Student:
    """
    Keeps information about student, namely surname, name, course, group_code and container of class Subject,
    checks its correctness, writes the data to txt wile.
    """
    def __init__(self, surname=None, name=None, course=None, group_code=None):
        self.__group_code = group_code
        self.__course = course
        self.__surname = surname
        self.__name = name
        self.__subject_list = list()

    def set_student(self, surname, name, course, group_code, subject):
        """
        Is responsible for error output if objects are not correct.
        """
        if self.check_surname(surname) and self.check_name(name) and self.check_n_cource(course) \
                and self.check_group_code(group_code):
            self.__group_code = group_code
            self.__name = name
            self.__surname = surname
            self.__course = course
            self.__subject_list.append(subject)
        else:
            print("***** program aborted *****")
            return False

    def get_course(self):
        """
        Gets value of course.
        """
        return self.__course

    def get_group_code(self):
        """
        Gets value of group_code.
        """
        return self.__group_code

    def get_surname(self):
        """
        Gets value of surname.
        """
        return self.__surname

    def get_name(self):
        """
        Gets value of name.
        """
        return self.__name

    def calculate_miss(self) -> int:
        """
        Calculates number of missed lessons for each student.
        """
        count_of_miss: int = 0
        for sub in self.__subject_list:
            count_of_miss += sub.count_of_miss_lesson()
        return count_of_miss

    def set_to_subject_list(self, subject):
        """
        Sets value of subject_list.
        """
        self.__subject_list.append(subject)

    def print_subject_info(self, fname):
        """
        Prints information about subject.
        """
        for subject in self.__subject_list:
            subject.print_lesson_info(fname)

    def write_student_info(self, fname, average_miss):
        """
        Writes data in the first row to txt file.
        """
        text = self.__surname + " " + self.__name + " " + str(self.calculate_miss()) + " " + str(round(average_miss, 1))
        f = open(fname, "a", )
        f.write(text + '\n')
        f.close()

    def write_subject_info(self, fname):
        """
        Writes information about subject to txt file.
        """
        for subject in self.__subject_list:
            subject.write_lesson_info(fname)

    def check_surname(self, surname):
        """
        Checks if surname is correct.
        """
        if re.compile("^[А-Яа-яёЁЇїІіЄєҐґ]+$").match(surname) and 4 <= len(surname) <= 29:
            return True
        else:
            return False

    def check_name(self, name):
        """
        Checks if name is correct.
        """
        if re.compile("^[А-Яа-яёЁЇїІіЄєҐґ]+$").match(name) and 4 <= len(name) <= 28:
            return True
        else:
            return True

    def check_n_cource(self, value):
        """
        Checks if n_course is correct.
        """
        try:
            int(value) and 1 <= len(value) <= 4
            return True
        except ValueError:
            return False

    def check_group_code(self, ncource):
        """
        Checks if group_code is correct.
        """
        if re.compile("^[^-_].*[^-_]$" ).match(ncource):
            return True
        else:
            return False
