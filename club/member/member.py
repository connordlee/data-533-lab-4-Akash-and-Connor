from club.member.userexceptions import NationException, SalaryException

countries = ['Afghanistan','Albania','Algeria','America','Andorra','Angola','Antigua','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bissau','Bolivia','Bosnia','Botswana','Brazil','British','Brunei','Bulgaria','Burkina','Burma','Burundi','Cambodia','Cameroon','Canada','Cape Verde','Central African Republic','Chad','Chile','China','Colombia','Comoros','Congo','Costa Rica','country debt','Croatia','Cuba','Cyprus','Czech','Denmark','Djibouti','Dominica','East Timor','Ecuador','Egypt','El Salvador','Emirate','England','Eritrea','Estonia','Ethiopia','Fiji','Finland','France','Gabon','Gambia','Georgia','Germany','Ghana','Great Britain','Greece','Grenada','Grenadines','Guatemala','Guinea','Guyana','Haiti','Herzegovina','Honduras','Hungary','Iceland','in usa','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Ivory Coast','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Korea','Kosovo','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia','Montenegro','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria','Norway','Oman','Pakistan','Palau','Panama','Papua','Paraguay','Peru','Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','Samoa','San Marino','Sao Tome','Saudi Arabia','scotland','scottish','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon','Somalia','South Africa','South Sudan','Spain','Sri Lanka','St. Kitts','St. Lucia','St Kitts','St Lucia','Saint Kitts','Santa Lucia','Sudan','Suriname','Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand','Tobago','Togo','Tonga','Trinidad','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Kingdom','United States','Uruguay','USA','Uzbekistan','Vanuatu','Vatican','Venezuela','Vietnam','Wales','welsh','Yemen','Zambia','Zimbabwe']

class member:
    def __init__(self, name, nationality, salary, yearsWClub):
        self.name = name
        self.nationality = nationality
        self.__salary = salary
        self.yearsWClub = yearsWClub
            
        
        
    def updateNationality(self, newNationality):
        try:
            if isinstance(newNationality, str) != True:
                raise(ValueError)
            if newNationality not in countries:
                # user defined exception (see userexceptions.py for exception definition)
                raise(NationException(newNationality))
        except NationException as nExcept:
            print("Error: ", nExcept)
        except ValueError:
            print("Error: Incorrect Data Type") 
        else:
            self.nationality = newNationality
        
    def setSalary(self, newSalary):
        try:
            if int(newSalary) <= 10000000 and int(newSalary) >= 50000:
                self.__salary = newSalary
            else:
                raise(SalaryException(newSalary))
        except ValueError:
            print("Salaries must be integer values")
        except SalaryException as sExcept:
            print("Error: ", sExcept)
        
    def getSalary(self):
        return self.__salary
    
    def newYear(self):
        self.yearsWClub += 1

    def display(self):
        print("           Name: {}\n    Nationality: {}\nYears With Club: {}".format(self.name, self.nationality, self.yearsWClub))

