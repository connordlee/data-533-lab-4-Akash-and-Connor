import unittest
from club import club
from club.member.membertypes import player, staff
from club.fan.fantype import domestic, international

class TestClub(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Temproary variables to be stored into the club
        ramos = player('Sergio Ramos', 'Spain', 1500000, 14, 'Right Back', 15)
        benzema = player('Karim Benzema', 'France', 7920000, 10, 'Striker', 9)
        vazquez = staff('Roberto Vazquez', 'Spain', 3200000, 1, 'Goalkeeping Coach')
        zidane = staff('Zinedine Zidane', 'France', 5500000, 9, 'Skipper')
        plist = [ramos.asList(), benzema.asList()]
        slist = [vazquez.asList(), zidane.asList()]
        
        connor = domestic("Connor Lee", "Sergio Ramos", 5, "Madrid", True, 8)
        akash = international("Akash Dhatavkar", "Leo Messi", 4, "Kelowna", "Canada", "TV")
        joe = domestic("Joe Miller", "Eden Hazard", 7, "Valencia", False, 12)
        jane = international("Jane Doe", "Marco Reus", 8, "San Francisco", "US", "Online")
        dlist = [connor.asList(), joe.asList()]
        ilist = [akash.asList(), jane.asList()]
        
        # Initializing club with 2 players, 2 staff, 2 domestic and 2 international
        cls.madrid = club.club(plist, slist, dlist, ilist)
        
    def setUp(self):
        # Initializing members to be reset each time
        self.p1 = player('Player 1', 'Germany', 4000000, 5, 'Midgard', 42)
        self.p2 = player('Player 2', 'Canada', 8300000, 7, 'Center Mid', 22)
        self.s1 = staff('Staff 1', 'Spain', 63000, 23, 'Groundskeeper')
        self.s2 = staff('Staff 2', 'Spain', 83000, 3, 'Accountant')
        
        self.d1 = domestic("Daniel Silva", "Mesut Ozil", 0, "Sevilla", False, 20)
        self.d2 = domestic("Agatha Christie", "Robert Lewandowski", 3, "Barcelona", True, 9)
        self.i1 = international("Haruki Murakami", "Rodrygo", 3, "Tokyo", "Japan", "TV")
        self.i2 = international("Leo Tolstoy", "Alexis Sanchez", 11, "Moscow", "Russia", "Online")


    @classmethod
    def tearDownClass(cls):
        # Deleting the club
        del cls.madrid

    def tearDown(self):
        # Deleting Members created in setUp
        del self.p1
        del self.s1
        del self.p2
        del self.s2
        
        del self.d1
        del self.d2
        del self.i1
        del self.i2

    def test_addPlayer(self):
        # Temporary variable to track original length of list
        origLen = len(self.madrid.members['players'])
        # Adding new player to the club
        name, nationality, salary, yearsWClub, position, jersey = self.p1.asList()
        self.madrid.addPlayer(name, nationality, salary, yearsWClub, position, jersey)
        # Assertions to confirm length change and info update (4 assertions)
        self.assertEqual(len(self.madrid.members['players']), origLen+1)
        self.assertEqual(self.madrid.members['players'][origLen].name, 'Player 1')
        self.assertEqual(self.madrid.members['players'][origLen].nationality, 'Germany')
        self.assertEqual(self.madrid.members['players'][origLen].getSalary(), 4000000)
        # Adding new player to the club
        name, nationality, salary, yearsWClub, position, jersey = self.p2.asList()
        self.madrid.addPlayer(name, nationality, salary, yearsWClub, position, jersey)
        # Assertions to confirm length change and info update (4 assertions)
        self.assertEqual(len(self.madrid.members['players']), origLen+2)
        self.assertEqual(self.madrid.members['players'][origLen+1].yearsWClub, 7)
        self.assertEqual(self.madrid.members['players'][origLen+1].position, 'Center Mid')
        self.assertEqual(self.madrid.members['players'][origLen+1].jersey, 22)
        
    def test_addStaff(self):
        # Temporary variable to track original length of list
        origLen = len(self.madrid.members['staff'])
        # Adding new player to the club
        name, nationality, salary, yearsWClub, title = self.s1.asList()
        self.madrid.addStaff(name, nationality, salary, yearsWClub, title)
        # Assertions to confirm length change and info update (4 assertions)
        self.assertEqual(len(self.madrid.members['staff']), origLen+1)
        self.assertEqual(self.madrid.members['staff'][origLen].name, 'Staff 1')
        self.assertEqual(self.madrid.members['staff'][origLen].nationality, 'Spain')
        self.assertEqual(self.madrid.members['staff'][origLen].getSalary(), 63000)
        # Adding new player to the club
        name, nationality, salary, yearsWClub, title = self.s2.asList()
        self.madrid.addStaff(name, nationality, salary, yearsWClub, title)
        # Assertions to confirm length change and info update (4 assertions)
        self.assertEqual(len(self.madrid.members['staff']), origLen+2)
        self.assertEqual(self.madrid.members['staff'][origLen+1].yearsWClub, 3)
        self.assertEqual(self.madrid.members['staff'][origLen+1].title, 'Accountant')
        
        
    def test_addDomestic(self):
        # Temporary variable to track original length of list
        origLen = len(self.madrid.fans["domestic"])
        # Adding new domestic to the club
        name, favouritePlayer, purchasedMerchandise, currentCity, hasSeasonTickets, yearsSinceFan = self.d1.asList()
        self.madrid.addDomestic(name, favouritePlayer, purchasedMerchandise, currentCity, hasSeasonTickets, yearsSinceFan)
        # Assertions to confirm length change and info update (4 assertions)
        self.assertEqual(len(self.madrid.fans["domestic"]), origLen+1)
        self.assertEqual(self.madrid.fans["domestic"][origLen].name, "Daniel Silva")
        self.assertEqual(self.madrid.fans["domestic"][origLen].getFavouritePlayer(), "Mesut Ozil")
        self.assertEqual(self.madrid.fans["domestic"][origLen].getCurrentCity(), "Sevilla")
        # Adding new domestic to the club
        name, favouritePlayer, purchasedMerchandise, currentCity, hasSeasonTickets, yearsSinceFan = self.d2.asList()
        self.madrid.addDomestic(name, favouritePlayer, purchasedMerchandise, currentCity, hasSeasonTickets, yearsSinceFan)
        # Assertions to confirm length change and info update (4 assertions)
        self.assertEqual(len(self.madrid.fans["domestic"]), origLen+2)
        self.assertEqual(self.madrid.fans["domestic"][origLen+1].getPurchasedMerchandise(), 3)
        self.assertEqual(self.madrid.fans["domestic"][origLen+1].hasSeasonTickets, True)
        self.assertEqual(self.madrid.fans["domestic"][origLen+1].yearsSinceFan, 9)
    
    def test_addInternational(self):
        # Temporary variable to track original length of list
        origLen = len(self.madrid.fans["international"])
        # Adding new international to the club
        name, favouritePlayer, purchasedMerchandise, currentCity, country, viewMatches = self.i1.asList()
        self.madrid.addInternational(name, favouritePlayer, purchasedMerchandise, currentCity, country, viewMatches)
        # Assertions to confirm length change and info update (4 assertions)
        self.assertEqual(len(self.madrid.fans["international"]), origLen+1)
        self.assertEqual(self.madrid.fans["international"][origLen].name, "Haruki Murakami")
        self.assertEqual(self.madrid.fans["international"][origLen].getFavouritePlayer(), "Rodrygo")
        self.assertEqual(self.madrid.fans["international"][origLen].getCurrentCity(), "Tokyo")
        # Adding new international to the club
        name, favouritePlayer, purchasedMerchandise, currentCity, country, viewMatches = self.i2.asList()
        self.madrid.addInternational(name, favouritePlayer, purchasedMerchandise, currentCity, country, viewMatches)
        # Assertions to confirm length change and info update (4 assertions)
        self.assertEqual(len(self.madrid.fans["international"]), origLen+2)
        self.assertEqual(self.madrid.fans["international"][origLen+1].getPurchasedMerchandise(), 11)
        self.assertEqual(self.madrid.fans["international"][origLen+1].country, "Russia")
        self.assertEqual(self.madrid.fans["international"][origLen+1].viewMatches, "Online")

    def test_removePlayer(self):
        # Temporary variable to track original length of list
        origLen = len(self.madrid.members['players'])
        # Delete first player
        self.madrid.removePlayer('Sergio Ramos')
        # Assertions to verify new list length (1 assertion)
        self.assertEqual(len(self.madrid.members['players']), origLen-1)
        # For Loop to get list of remaining players then assertion to check if player still in list (1 assertion)
        remainingPlayers = []
        for player in self.madrid.members['players']:
            remainingPlayers.append(player.name)
        self.assertNotIn('Sergio Ramos', remainingPlayers)
        # Delete Second player
        self.madrid.removePlayer('Karim Benzema')
        # Assertions to verify new list length (1 assertion)
        self.assertEqual(len(self.madrid.members['players']), origLen-2)
        # For Loop to get list of remaining players then assertion to check if player still in list (1 assertion)
        remainingPlayers = []
        for player in self.madrid.members['players']:
            remainingPlayers.append(player.name)
        self.assertNotIn('Sergio Ramos', remainingPlayers)

    def test_removeStaff(self):
        # Temporary variable to track original length of list
        origLen = len(self.madrid.members['staff'])
        # Delete first Staff Member
        self.madrid.removeStaff('Roberto Vazquez')
        # Assertions to verify new list length (1 assertion)
        self.assertEqual(len(self.madrid.members['staff']), origLen-1)
        # For Loop to get list of remaining staff then assertion to check if staff still in list (1 assertion)
        remainingStaff = []
        for staff in self.madrid.members['staff']:
            remainingStaff.append(staff.name)
        self.assertNotIn('Roberto Vazquez', remainingStaff)
        # Delete first Staff Member
        self.madrid.removeStaff('Zinedine Zidane')
        # Assertions to verify new list length (1 assertion)
        self.assertEqual(len(self.madrid.members['staff']), origLen-2)
        # For Loop to get list of remaining staff then assertion to check if staff still in list (1 assertion)
        remainingStaff = []
        for staff in self.madrid.members['staff']:
            remainingStaff.append(staff.name)
        self.assertNotIn('Zinedine Zidane', remainingStaff)
        
        
    def test_removeDomestic(self):
        # Temporary variable to track original length of list
        origLen = len(self.madrid.fans["domestic"])
        # Delete first Domestic Fan
        self.madrid.removeDomestic("Connor Lee")
        # Assertions to verify new list length (1 assertion)
        self.assertEqual(len(self.madrid.fans["domestic"]), origLen-1)
        # For Loop to get list of remaining domestic then assertion to check if domestic still in list (1 assertion)
        remainingDomestic = []
        for domestic in self.madrid.fans["domestic"]:
            remainingDomestic.append(domestic.name)
        self.assertNotIn("Connor Lee", remainingDomestic)
        # Delete Second Domestic Member
        self.madrid.removeDomestic("Joe Miller")
        # Assertions to verify new list length (1 assertion)
        self.assertEqual(len(self.madrid.fans["domestic"]), origLen-2)
        # For Loop to get list of remaining domestic then assertion to check if domestic still in list (1 assertion)
        remainingDomestic = []
        for domestic in self.madrid.fans["domestic"]:
            remainingDomestic.append(domestic.name)
        self.assertNotIn("Joe Miller", remainingDomestic)
        
    def test_removeInternational(self):
        # Temporary variable to track original length of list
        origLen = len(self.madrid.fans["international"])
        # Delete first International Fan
        self.madrid.removeInternational("Akash Dhatavkar")
        # Assertions to verify new list length (1 assertion)
        self.assertEqual(len(self.madrid.fans["international"]), origLen-1)
        # For Loop to get list of remaining international then assertion to check if international still in list (1 assertion)
        remainingInternational = []
        for international in self.madrid.fans["international"]:
            remainingInternational.append(international.name)
        self.assertNotIn("Akash Dhatavkar", remainingInternational)
        # Delete Second International Member
        self.madrid.removeInternational("Jane Doe")
        # Assertions to verify new list length (1 assertion)
        self.assertEqual(len(self.madrid.fans["international"]), origLen-2)
        # For Loop to get list of remaining international then assertion to check if international still in list (1 assertion)
        remainingInternational = []
        for international in self.madrid.fans["international"]:
            remainingInternational.append(international.name)
        self.assertNotIn("Jane Doe", remainingInternational)
        
    def test_updatePlayer(self):
        # Code to test updating each player attribute individually
        self.madrid.updatePlayer('Player 1', nationality='Spain') # Updating nationality
        self.madrid.updatePlayer('Player 1', salary=15000000) # Updating Salary
        self.madrid.updatePlayer('Player 1', yearsWClub=14) # Updating yearsWClub
        self.madrid.updatePlayer('Player 1', position='Right Back') # Updating position
        self.madrid.updatePlayer('Player 1', jersey=15) # Updating jersey        
        # Code to test updating all player attributes at the same time
        self.madrid.updatePlayer('Player 2', 'France', 7920000, 10, 'Striker', 9)
        # Assertions to verify that the individual changes occured as expected (5 assertions)
        self.assertEqual(self.madrid.members['players'][0].nationality, 'Spain')
        self.assertEqual(self.madrid.members['players'][0].getSalary(), 15000000)
        self.assertEqual(self.madrid.members['players'][0].yearsWClub, 14)
        self.assertEqual(self.madrid.members['players'][0].position, 'Right Back')
        self.assertEqual(self.madrid.members['players'][0].jersey, 15)
        # Assertions to verify that the bulk changes occured as expected (5 assertions)
        self.assertEqual(self.madrid.members['players'][1].nationality, 'France')
        self.assertEqual(self.madrid.members['players'][1].getSalary(), 7920000)
        self.assertEqual(self.madrid.members['players'][1].yearsWClub, 10)
        self.assertEqual(self.madrid.members['players'][1].position, 'Striker')
        self.assertEqual(self.madrid.members['players'][1].jersey, 9)
        
    def test_updateStaff(self):
        # Code to test updating each staff attribute individually
        self.madrid.updateStaff('Staff 1', nationality='Spain') # Updating nationality
        self.madrid.updateStaff('Staff 1', salary=3200000) # Updating Salary
        self.madrid.updateStaff('Staff 1', yearsWClub=1) # Updating yearsWClub
        self.madrid.updateStaff('Staff 1', title='Goalkeeping Coach') # Updating position     
        # Code to test updating all staff attributes at the same time
        self.madrid.updateStaff('Staff 2', 'France', 5500000, 9, 'Skipper')
        # Assertions to verify that the individual changes occured as expected (4 assertions)
        self.assertEqual(self.madrid.members['staff'][0].nationality, 'Spain')
        self.assertEqual(self.madrid.members['staff'][0].getSalary(), 3200000)
        self.assertEqual(self.madrid.members['staff'][0].yearsWClub, 1)
        self.assertEqual(self.madrid.members['staff'][0].title, 'Goalkeeping Coach')
        # Assertions to verify that the bulk changes occured as expected (4 assertions)
        self.assertEqual(self.madrid.members['staff'][1].nationality, 'France')
        self.assertEqual(self.madrid.members['staff'][1].getSalary(), 5500000)
        self.assertEqual(self.madrid.members['staff'][1].yearsWClub, 9)
        self.assertEqual(self.madrid.members['staff'][1].title, 'Skipper')
        
    
    def test_updateDomestic(self):
        # Code to test updating each player attribute individually
        self.madrid.updateDomestic("Daniel Silva", favouritePlayer = "Paulo Dybala") # Updating Fav Player
        self.madrid.updateDomestic("Daniel Silva", purchasedMerchandise = 15) # Updating Purchased Merchandise
        self.madrid.updateDomestic("Daniel Silva", currentCity = "Madrid") # Updating Current City
        self.madrid.updateDomestic("Daniel Silva", hasSeasonTickets = True) # Updating Season Tickets
        self.madrid.updateDomestic("Daniel Silva", yearsSinceFan = 21) # Updating Years Since Fan
        # Code to test updating all player attributes at the same time
        self.madrid.updateDomestic("Agatha Christie", "Angel DiMaria", 4, "Gijon", False, 10)
        # Assertions to verify that the individual changes occured as expected (5 assertions)
        self.assertEqual(self.madrid.fans["domestic"][0].getFavouritePlayer(), "Paulo Dybala")
        self.assertEqual(self.madrid.fans["domestic"][0].getPurchasedMerchandise(), 15)
        self.assertEqual(self.madrid.fans["domestic"][0].getCurrentCity(), "Madrid")
        self.assertEqual(self.madrid.fans["domestic"][0].hasSeasonTickets, True)
        self.assertEqual(self.madrid.fans["domestic"][0].yearsSinceFan, 21)
        # Assertions to verify that the bulk changes occured as expected (5 assertions)
        self.assertEqual(self.madrid.fans["domestic"][1].getFavouritePlayer(), "Angel DiMaria")
        self.assertEqual(self.madrid.fans["domestic"][1].getPurchasedMerchandise(), 4)
        self.assertEqual(self.madrid.fans["domestic"][1].getCurrentCity(), "Gijon")
        self.assertEqual(self.madrid.fans["domestic"][1].hasSeasonTickets, False)
        self.assertEqual(self.madrid.fans["domestic"][1].yearsSinceFan, 10)
        
    def test_updateInternational(self):
        # Code to test updating each player attribute individually
        self.madrid.updateInternational("Haruki Murakami", favouritePlayer = "Sergio Aguero") # Updating Fav Player
        self.madrid.updateInternational("Haruki Murakami", purchasedMerchandise = 9) # Updating Purchased Merchandise
        self.madrid.updateInternational("Haruki Murakami", currentCity = "Kelowna") # Updating Current City
        self.madrid.updateInternational("Haruki Murakami", country = "Canada") # Updating Country
        self.madrid.updateInternational("Haruki Murakami", viewMatches = "Online") # Updating views Matches        
        # Code to test updating all player attributes at the same time
        self.madrid.updateInternational("Leo Tolstoy", "Romeu Lukaku", 14, "London", "England", "TV")
        # Assertions to verify that the individual changes occured as expected (5 assertions)
        self.assertEqual(self.madrid.fans["international"][0].getFavouritePlayer(), "Sergio Aguero")
        self.assertEqual(self.madrid.fans["international"][0].getPurchasedMerchandise(), 9)
        self.assertEqual(self.madrid.fans["international"][0].getCurrentCity(), "Kelowna")
        self.assertEqual(self.madrid.fans["international"][0].country, "Canada")
        self.assertEqual(self.madrid.fans["international"][0].viewMatches, "Online")
        # Assertions to verify that the bulk changes occured as expected (5 assertions)
        self.assertEqual(self.madrid.fans["international"][1].getFavouritePlayer(), "Romeu Lukaku")
        self.assertEqual(self.madrid.fans["international"][1].getPurchasedMerchandise(), 14)
        self.assertEqual(self.madrid.fans["international"][1].getCurrentCity(), "London")
        self.assertEqual(self.madrid.fans["international"][1].country, "England")
        self.assertEqual(self.madrid.fans["international"][1].viewMatches, "TV")

unittest.main(argv=[''], verbosity=2, exit=False)