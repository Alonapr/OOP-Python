"""
Includes class Lesson.
"""

class Lesson:
    """
    Keeps information about lesson, namely classroom, class_type, week, day_of_week and num_of_class,
    checks its correctness.
    """
    def __init__(self, classroom=None, class_type=None, week=None, day_of_week=None, num_of_class=None):
        self.__classroom = classroom
        self.__class_type = class_type
        self.__week = week
        self.__day_of_week = day_of_week
        self.__num_of_class = num_of_class

    def set_lesson(self, classroom, class_type, week, day_of_week, num_of_class):
        """
        Is responsible for error output if objects are not correct.
        """
        if self.correct(classroom, class_type, week, day_of_week, num_of_class):
            self.__classroom = classroom
            self.__class_type = class_type
            self.__week = week
            self.__day_of_week = day_of_week
            self.__num_of_class = num_of_class
        else:
            print("***** program aborted *****")
            return False

    def get_classroom(self):
        """
        Gets value of classroom.
        """
        return self.__classroom

    def get_class_type(self):
        """
        Gets value of class_type.
        """
        return self.__class_type

    def get_week(self):
        """
        Gets value of week.
        """
        return self.__week

    def get_day_of_week(self):
        """
        Gets value of day_of_week.
        """
        return self.__day_of_week

    def get_num_of_class(self):
        """
        Gets value of num_of_class.
        """
        return self.__num_of_class

    def correct(self, classroom, class_type, week, day_of_week, num_of_class):
        """
        Checks if all 5 methods return True.
        """
        if self.check_classroom(classroom) and self.check_toccupation(class_type) and self.check_nweek(week) \
                and self.check_nday(day_of_week) and self.check_num_of_class(num_of_class):
            return True
        else:
            return False

    def check_toccupation(self, toccupation):
        """
        Checks if toccupation is correct.
        """
        s = ["лекц.", "п", "Seminar", "лаб."]
        if toccupation in s:
            return True
        else:
            return False

    def check_nweek(self, nweek):
        """
        Checks if nweek is correct.
        """
        try:
            int(nweek) and 1 <= len(nweek) <= 19
            return True
        except ValueError:
            return False

    def check_nday(self, nday):
        """
        Checks if nday is correct.
        """
        try:
            int(nday) and 1 <= len(nday) <= 5
            return True
        except ValueError:
            return False

    def check_num_of_class(self, value):
        """
        Checks if num_of_class is correct.
        """
        try:
            int(value) and 1 <= len(value) <= 4
            return True
        except ValueError:
            return False

    def check_classroom(self, classroom):
        """
        Checks if classroom is correct.
        """
        try:
            int(classroom) and int(classroom) > 0
            return True
        except ValueError:
            return False



