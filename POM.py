from abc import ABC, abstractmethod
import abc

#Page Object Model (POM) implementation for database connection and query execution
#Singelton design pattern
class PageObjectModel:
    __instance = None
    __isConnected = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(PageObjectModel,cls).__new__(cls)

            #some code to login and connect to database 

            cls.__cursor = None  # Placeholder for database cursor
            cls.__connection = None  # Placeholder for database connection
            cls.__isConnected = True
            print('Logged to Database XYZ')
        return cls.__instance
    
    @property #cannot be called, just as demonstration 
    def isconnected(self): 
        return self.__isConnected
    
    @staticmethod
    def get_isconnected(self): #getter for __isConnected variable
        return self.__isConnected

    def __str__(self):
        return (f'Current vars: {self.__cursor}, {self.__connection}, {self.__isConnected}')

    @classmethod
    def disconnect(cls):
        if cls.get_isconnected(cls) == True:

            #some code to disconnect from database

            cls.__isConnected = False
            print('Disconnected from Database XYZ')
        else:
            print('Database disconected already')
    
    @classmethod
    def run_query(cls, query):
        if cls.get_isconnected(cls) == True:

            #executing __curson.execute(query) or __connection.something()

            print(f'Running query: {query}')
        else:
            print('Database disconected, cannot run query')
    






#Factory design pattern
class PageObjectModelFactory(ABC):

    @abc.abstractmethod
    def pom_factory(cls):
        #some code to login as an user
        print('Logged as an user')


class PageObjectModelFactory_Interface(ABC):

    @abc.abstractmethod
    def __islogged__(cls):
        pass

    @abc.abstractmethod
    def logout(cls):
        pass
    
    @abc.abstractmethod
    def login(cls, username):
        pass




class LoginToUIType01(PageObjectModelFactory):
    
    def pom_factory(self):
        return LoginToUIType01_Interface()


class LoginToUIType01_Interface(PageObjectModelFactory_Interface):
    __isLogged = None
    __UI_type = 'UI Type 01'

    def __islogged__(cls):
        return cls.__isLogged

    def logout(cls, username):
        if cls.__islogged__() == True:

            #some code to log out

            cls.__isLogged = False
            print(f'Logged out from {cls.__UI_type}')
        else:
            print(f'Logged out already from {cls.__UI_type}')
    
    def login(cls, username):
        #executing some logging in code
        print(f'Logging in as user: {username} to {cls.__UI_type}')



class LoginToUIType02(PageObjectModelFactory):
    
    def pom_factory(self):
        return LoginToUIType02_Interface()

class LoginToUIType02_Interface(PageObjectModelFactory_Interface):
    __isLogged = None
    __UI_type = 'UI Type 02'

    def __islogged__(cls):
        return cls.__isLogged

    def logout(cls, username):
        if cls.__islogged__() == True:

            #some code to log out

            cls.__isLogged = False
            print(f'Logged out from {cls.__UI_type}')
        else:
            print(f'Logged out already from {cls.__UI_type}')
    
    def login(cls, username):
        #executing some logging in code
        print(f'Logging in as user: {username} to {cls.__UI_type}')










#TODO example facade design pattern