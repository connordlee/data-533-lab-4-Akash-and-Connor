class NationException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return(repr(self.value+' is an invalid nation'))
    
class SalaryException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        if self.value < 50000:
            return(repr('Minimum possible salary is $50000 you input: $'+str(self.value)))
        elif self.value > 10000000:
            return(repr('Maximum possible salary is $10000000 you input: $'+str(self.value)))
        else:
            return(repr('Invalid Salary'))