"""
Includes class Output.
"""


class Output:
    """
    Keeps data that must be outputted in second row:
    week, day_of_week, num_of_class, classroom, subject, class_type.
    Writes them to txt file.
    """
    def __init__(self, week, day_of_week, num_of_class, classroom, subject, class_type):
        self.__class_type = class_type
        self.__subject = subject
        self.__classroom = classroom
        self.__num_of_class = num_of_class
        self.__day_of_week = day_of_week
        self.__week = week

    def set_class_type(self, class_type):
        """
        Sets value of class_type.
        """
        self.__class_type = class_type

    def set_subject(self, subject):
        """
        Sets value of subject.
        """
        self.__subject = subject

    def set_classroom(self, classroom):
        """
        Sets value of classroom.
        """
        self.__classroom = classroom

    def set_num_of_class(self, num_of_class):
        """
        Sets value of num_of_class.
        """
        self.__num_of_class = num_of_class

    def set_day_of_week(self, day):
        """
        Sets value of day_of_week.
        """
        self.__day_of_week = day

    def set_week(self, week):
        """
        Sets value of subject.
        """
        self.__week = week

    def get_class_type(self):
        """
        Gets value of class_type.
        """
        return self.__class_type

    def get_subject(self):
        """
        Gets value of subject.
        """
        return self.__subject

    def get_classroom(self):
        """
        Gets value of classroom.
        """
        return self.__classroom

    def get_num_of_class(self):
        """
        Gets value of num_of_class.
        """
        return self.__num_of_class

    def get_day_of_week(self):
        """
        Gets value of day_of_week.
        """
        return self.__day_of_week

    def get_week(self):
        """
        Gets value of week.
        """
        return self.__week

    def print(self):
        """
        Prints week, day_of_week, num_of_class, classroom, subject, class_type.
        """
        print(self.__week + " " + self.__day_of_week + " " + self.__num_of_class + " " + self.__classroom
              + " " + self.__subject + " " + self.__class_type)

    def get_string(self):
        """
        Gets value of week, day_of_week, num_of_class, classroom, subject, class_type.
        """
        return str(self.__week) + " " + str(self.__day_of_week) + " " + str(self.__num_of_class) + \
            " " + str(self.__classroom) + " " + str(self.__subject) + " " + str(self.__class_type)

    def write_to_file(self, fname):
        """
        Writes printed data from the second row to txt file.
        """
        text = self.get_string()
        f = open(fname, "a", )
        f.write(text + '\n')
        f.close()
