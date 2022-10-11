"""
Includes class Subject.
"""
import re

from output import Output


class Subject:
    """
    Keeps information about subject, namely subject, group_code and container of class Lesson,
    checks its correctness, writes the data to txt file.
    """
    def __init__(self, subject=None, group_code=None):
        self.__subject = subject
        self.__group_code = group_code
        self.__lesson_list = list()

    def set_subjects(self, subject, ncourse, group_code, lesson):
        """
        Is responsible for error output if objects are not correct.
        """
        if self.check_subject(subject) and self.check_ngroup(ncourse, group_code):
            self.set_subject(subject)
            self.set_group_code(group_code)
            self.__lesson_list.append(lesson)
        else:
            print("***** program aborted *****")
            return False

    def set_subject(self, subject):
        """
        Sets value for subject.
        """
        self.__subject = subject

    def set_group_code(self, group_code):
        """
        Sets value for group_code.
        """
        self.__group_code = group_code

    def get_subject(self):
        """
        Gets value of subject.
        """
        return self.__subject

    def get_group_code(self):
        """
        Gets value of group_code.
        """
        return self.__group_code

    def count_of_miss_lesson(self):
        """
        Counts number of missed lessons.
        """
        return len(self.__lesson_list)

    def write_lesson_info(self, fname):
        """
        Writes data in the second row to txt file.
        """
        out_list = []
        for lesson in self.__lesson_list:
            output = Output(lesson.get_week(), lesson.get_day_of_week(), lesson.get_num_of_class(),
                            lesson.get_classroom(), self.__subject, lesson.get_class_type())
            out_list.append(output)
        out_list.sort(key=lambda out: "лекц." < "Seminar" < "п." < "лаб." in out.get_class_type())
        out_list.sort(key=lambda out: out.get_subject())
        out_list.sort(key=lambda out: out.get_week())
        out_list.sort(key=lambda out: out.get_day_of_week())
        out_list.sort(key=lambda out: out.get_num_of_class())
        for el in out_list:
            el.write_to_file(fname)

    def check_subject(self, subject):
        """
        Checks if subject is correct.
        """
        if isinstance(subject, str) and 4 <= len(subject) <= 28:
            return True
        else:
            return False

    def check_ngroup(self, ngroup, ncource):
        """
        Checks if ngroup is correct.
        """
        if re.compile("^[^-_].*[^-_]$").match(ncource):
            return True
        else:
            return False
