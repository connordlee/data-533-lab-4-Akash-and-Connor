import unittest
from club import club
from club.member.member import member

class TestMember(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initializing members with changes
        cls.vazquez = member('Roberto Vazquez', 'Spain', 3200000, 1)
        cls.zidane = member('Zinedine Zidane', 'France', 5500000, 9)
        
    def setUp(self):
        # Initializing members to be reset each time
        self.ramos = member('Sergio Ramos', 'Spain', 1500000, 14)
        self.benzema = member('Karim Benzema', 'France', 7920000, 10)

    @classmethod
    def tearDownClass(cls):
        # Deleting Members created in setUpClass
        del cls.zidane
        del cls.vazquez

    def tearDown(self):
        # Deleting Members created in setUp
        del self.ramos
        del self.benzema

    def test_updateNationality(self):
        # Updating the nationalities for the members
        self.ramos.updateNationality('Canada')
        self.benzema.updateNationality('Germany')
        self.vazquez.updateNationality('Canada')
        self.zidane.updateNationality('Germany')
        # Testing that the nationalities updated (4 assertions)
        self.assertEqual(self.ramos.nationality,'Canada')
        self.assertEqual(self.benzema.nationality, 'Germany')
        self.assertEqual(self.vazquez.nationality,'Canada')
        self.assertEqual(self.zidane.nationality, 'Germany')
        # Testing that the nationalities are all of type string (4 assertions)
        self.assertIsInstance(self.ramos.nationality, str)
        self.assertIsInstance(self.benzema.nationality, str)
        self.assertIsInstance(self.vazquez.nationality, str)
        self.assertIsInstance(self.zidane.nationality, str)
        # Testing Incorrect Inputes
        self.ramos.updateNationality('blarg')
        self.assertEqual(self.ramos.nationality,'Canada')
        self.ramos.updateNationality(4)
        self.assertEqual(self.ramos.nationality,'Canada')        
        
    def test_setSalary_getSalary(self):
        # Setting the salaries to something new for the members
        self.ramos.setSalary(50000)
        self.benzema.setSalary(2000000)
        self.vazquez.setSalary(3500000)
        self.zidane.setSalary(400000)
        # Testing that the setSalary worked and that the getSalary pulls the correct information (4 assertions)
        self.assertEqual(self.ramos.getSalary(), 50000)
        self.assertEqual(self.benzema.getSalary(), 2000000)
        self.assertEqual(self.vazquez.getSalary(), 3500000)
        self.assertEqual(self.zidane.getSalary(), 400000)
        # Testing that the getSalary method pulls integers
        self.assertIsInstance(self.ramos.getSalary(), int)
        self.assertIsInstance(self.benzema.getSalary(), int)
        self.assertIsInstance(self.vazquez.getSalary(), int)
        self.assertIsInstance(self.zidane.getSalary(), int)
        # Testing inptu type
        self.ramos.setSalary('test')
        self.assertEqual(self.ramos.getSalary(), 50000)

    def test_newYear(self):
        # Storing temporary variables for years before running newYear method
        ramosYrs = self.ramos.yearsWClub
        benzemaYrs = self.benzema.yearsWClub
        vazquezYrs = self.vazquez.yearsWClub
        zidaneYrs = self.zidane.yearsWClub
        # Running the newYear method
        self.ramos.newYear()
        self.benzema.newYear()
        self.vazquez.newYear()
        self.zidane.newYear()
        # Testing if the new year method increased the value by 1 (4 assertions)
        self.assertEqual(self.ramos.yearsWClub, ramosYrs+1)
        self.assertEqual(self.benzema.yearsWClub, benzemaYrs+1)
        self.assertEqual(self.vazquez.yearsWClub, vazquezYrs+1)
        self.assertEqual(self.zidane.yearsWClub, zidaneYrs+1)
        # Testing if the new year method keeps data as integer (4 assertions)
        self.assertIsInstance(self.ramos.yearsWClub, int)
        self.assertIsInstance(self.benzema.yearsWClub, int)
        self.assertIsInstance(self.vazquez.yearsWClub, int)
        self.assertIsInstance(self.zidane.yearsWClub, int)

unittest.main(argv=[''], verbosity=2, exit=False)