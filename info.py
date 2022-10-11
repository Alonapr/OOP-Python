"""
Includes class Info.
"""

from lesson import Lesson
from output import Output
from student import Student
from subject import Subject


class Info:
    """
    Takes all rows in csv and json files,
    converts them to objects.
    """
    def __init__(self):
        self.__student_list = list()
        self.__i = 0
        self.__information = list()
        self.__average_miss = 0

    def __iter__(self):
        return self

    def next(self):
        """
        Is responsible for iteration.
        """
        if self.__i < len(self.__information):
            self.__i += 1
            return self.__information[self.__i - 1]
        else:
            raise StopIteration

    def set_information(self, info):
        """
        Sets value of information.
        """
        self.__information = info

    def print_all_info(self, fname):
        """
        Prints every row of information.
        """
        for str1 in self.__information:
            print(str1)

    def clear(self):
        """
        Drops data and nullifies the field with average_pass.
        """
        self.__information.clear()
        self.__student_list.clear()
        self.__average_miss = 0

    def info_count(self):
        """
        Counts number of rows in scv file.
        """
        return len(self.__information) - 1

    def lecture_count(self):
        """
        Counts number of lectures in csv file.
        """
        lesson_dict = set()
        for column in self.__information:
            if "лекц.".lower() in column[1].lower():
                lesson_dict.add(column[9])
        return len(lesson_dict)

    def check_student(self, s: Student):
        """
        Checks if student already exist.
        """
        for student in self.__student_list:
            if student.get_surname() == s.get_surname() and student.get_group_code() == s.get_group_code():
                return False
        return True

    def parse_data(self):
        """
        Transforms rows from information into objects of classes Lesson, Subject and Student,
        ensures writing for every student list of subjects.
        """
        for r in self.__information:
            lesson = Lesson()
            lesson.set_lesson(r[0], r[1], r[5], r[6], r[7])
            subject = Subject()
            subject.set_subjects(r[4], r[8], r[9], lesson)
            student = Student()
            student.set_student(r[2], r[3], r[8], r[9], subject)
            if self.check_student(student):
                self.__student_list.append(student)
            else:
                for stud in self.__student_list:
                    if stud.get_surname() == student.get_surname() and \
                            stud.get_group_code() == student.get_group_code():
                        stud.set_to_subject_list(subject)

    def processing(self, fname):
        """
        Checks average_miss and visit.
        """
        self.check_average_miss()
        self.check_visit(fname)

    def check_average_miss(self):
        """
        Calculates average number of missed lessons - average_miss.
        """
        max_miss: int = 0
        for stud in self.__student_list:
            max_miss += stud.calculate_miss()
        self.__average_miss = max_miss/len(self.__student_list)

    def check_visit(self, fname):
        """
        Checks students, who missed lessons no more than average.
        """
        print("output " + fname + ":", end=" ")
        open(fname, "w").close()
        for s in self.__student_list:
            if s.calculate_miss() <= self.__average_miss:
                s.write_student_info(fname, self.__average_miss)
                s.write_subject_info(fname)
        print("OK")

