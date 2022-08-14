"""
Class method:
- called on the class itself, not on an object instance
- can only access your class variables
<<class>>.<<class_method>>

"""
"""

Static method:
- general utility methods that perform tasks in isolation
- dont take self or cls parameters
- bound to class but not the object of the class

Access restrictions:
private only accessible within the class (use __ to make it private)
public is accessible everywhere: within the class, inheritance, objects


"""

class Student:
    study_type = "remote"
    def __init__(self, name, age, cohort):
        self.name = name
        self.age = age
        self.__cohort = cohort #__ means it is private variable
    def print_std(self):
        print(f"name: {self.name}\nage: {self.age} \ncohort: {self.__cohort}\nstudy type: {self.study_type}")

    def __myprivate_var(self):
        print("I am private")

    @classmethod #decorator
    def set_study_type(cls, mode):
            cls.study_type = mode

    @staticmethod
    def is_weekend(day):
        return day in [5,6]
    @staticmethod
    def sample_std():
        print(f"name: sample\nage: 10\nstudy type: hybrid")


std1= Student ("name", 28, "DS1")
std1.print_std()
Student.set_study_type("Hybrid")
std1.print_std()
Student.sample_std()
std1.sample_std()
