import pandas as pd

from club.member.userexceptions import NationException, SalaryException

countries = pd.read_csv('countries.csv', encoding = "utf-16", )

class member:
    def __init__(self, name, nationality, salary, yearsWClub):
        try:
            if countries.loc[countries.Countries==nationality].values == nationality:
                pass
            else:
                raise(NationException(nationality))
            if salary > 10000000 or salary < 50000:
                raise(SalaryException(salary))
        except NationException as nExcept:
            print("Error: ", nExcept)
        except SalaryException as sExcept:
            print("Error: ", sExcept)
        else:
            self.name = name
            self.nationality = nationality
            self.__salary = salary
            self.yearsWClub = yearsWClub
            
        
        
    def updateNationality(self, newNationality):
        self.nationality = newNationality
        
    def setSalary(self, newSalary):
        self.__salary = newSalary
        
    def getSalary(self):
        return self.__salary
    
    def newYear(self):
        self.yearsWClub += 1

    def display(self):
        print("           Name: {}\n    Nationality: {}\nYears With Club: {}".format(self.name, self.nationality, self.yearsWClub))

