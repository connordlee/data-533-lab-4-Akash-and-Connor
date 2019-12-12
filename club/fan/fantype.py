#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Module: Domestic (Inherits Fan Properties)
Attributes:
    hasSeasonTickets
Functions:
    Initialize Domestic Fan
updateTicketStatus
Module: International (Inherits Fan Properties)
Attributes:
Home Country
Functions:
Initialize Domestic Fan
'''

from club.fan.fan import fan
from club.fan.fantypeExceptions import ViewsException, TicketException

viewMethod = ["Online", "TV", "online", "tv", "ONLINE", "Tv"]

class domestic(fan):
    def __init__(self, name, favouritePlayer, purchasedMerchandise, currentCity, hasSeasonTickets, yearsSinceFan):
        fan.__init__(self, name, favouritePlayer, purchasedMerchandise, currentCity)
        self.hasSeasonTickets = hasSeasonTickets
        self.yearsSinceFan = yearsSinceFan

    def updateTicketStatus(self, newTicketStatus):
        try:
            if isinstance(newTicketStatus, str) == True:
                raise(TicketException(newTicketStatus))
            if isinstance(newTicketStatus, int) == True:
                raise(ValueError)
        except TicketException as texc:
            print("Message: ", texc)
        except ValueError:
            print("Incorrect Value Type")
            
        else:
            self.hasSeasonTickets = newTicketStatus
    
    def asList(self):
        return([self.name, self.getFavouritePlayer(), self.getPurchasedMerchandise(), self.getCurrentCity(), 
                self.hasSeasonTickets, self.yearsSinceFan])

    def display(self):
        fan.display(self)
        print("   Has Season Tickets: {}\n      Years Since Fan: {}".format(self.hasSeasonTickets, self.yearsSinceFan))

class international(fan):
    def __init__(self, name, favouritePlayer, purchasedMerchandise, currentCity, country, viewMatches):
        fan.__init__(self, name, favouritePlayer, purchasedMerchandise, currentCity)
        self.country = country
        self.viewMatches = viewMatches
    
    def updateViewMatches(self, newViewMatches):
        try:
            if newViewMatches not in viewMethod:
                raise(ViewsException(newViewMatches))
            if isinstance(newViewMatches, str) != True:
                raise(ValueError)
        except ViewsException as vexc:
            print("Message: ", vexc)
        except ValueError:
            print("Error! Wrong input type!")
        else:
            self.viewMatches = newViewMatches
    
    def display(self):
        fan.display(self)
        print("              Country: {}\n        Views Matches: {}".format(self.country, self.viewMatches))

    def asList(self):
        return([self.name, self.getFavouritePlayer(), self.getPurchasedMerchandise(), self.getCurrentCity(), 
                self.country, self.viewMatches])
