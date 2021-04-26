class Person:
    name = None
    age = None
    hometown = None
    stays = None

    def __init__(self):
        self.__gender = None

    def addYear(self):
        age += 1

    def setGender(self, pGender):
        self.__gender = pGender

    def getGender():
        return self.__gender


class Student(Person):
    def __init__(self):
        super().__init__()
        self.__schoolName = ""
        self.__year = 0

    def setSchoolName_Year(self, sName, sYear):
        self.__schoolName = sName
        self.__year = sYear

    def getSchoolName(self):
        return self.__schoolName

    def getYear(self):
        return self.__year


class Worker(Person):
    def __init__(self):
        super().__init__()
        self.__org = ""
        self.__year = 0
        self.__salary = 0

    def setOrg_Year_Salary(self, orgName, startYear, orgSalary):
        self.__org = orgName
        self.__year = startYear
        self.__salary = orgSalary

    def getOrg(self):
        return self.__org

    def getYear(self):
        return self.__year

    def getSalary(self):
        return self.__salary


class StudentWorker(Student, Worker):
    def __init__(self, pName, pAge):
        super().__init__()
        self.name = pName
        self.age = pAge


def main():
    #Object code goes here

if __name__ == __main__:
    main()
