import POM as pom

#this cannot be executed with pytest due to presence of __new__ method in base class

class Test_Case01A(pom.PageObjectModel):
    
    def __init__(self):
        super().__init__() #in this case it won't do anything despite super() because of singleton design pattern

    @classmethod
    def test_execution(cls):
        print("Executing test case 01")

        print(f'Is DB connected = {cls.get_isconnected(cls)}\n')  # should be True

        #query execution
        cls.run_query("SELECT * FROM users")

        print(cls())  # will print current values of __cursor, __connection and __isConnected variables

        #disconnecting from database
        cls.disconnect()

        print(f'Is DB connected = {cls.get_isconnected(cls)}\n')  # should be False

        #query execution wont work as database is disconnected
        cls.run_query("SELECT * FROM users")

        print('\n\n\n')






#this can be executed with pytest due to lack of __init__ and __new__ method
#but won't be due to need for test_user parameter, which is providec in __main__ section
class Test_Case01D(pom.LoginToUIType01):
    def test_execution(self, test_user):
        print("Executing test case 02")
        self.pom_factory().login(test_user) #will print that UI Type 01 is logged in
        self.pom_factory().logout(test_user)  #will print that UI Type 01 is logged out
        self.pom_factory().logout(test_user)  #will print that UI Type 01 is logged out already

class Test_Case01C(pom.LoginToUIType02):
    def test_execution(self, test_user):
        print("Executing test case 03")
        self.pom_factory().login(test_user) #will print that UI Type 02 is logged in
        self.pom_factory().logout(test_user)  #will print that UI Type 02 is logged out
        self.pom_factory().logout(test_user)  #will print that UI Type 02 is logged out already


if __name__ == "__main__":
    #------------ for testing singleton pattern in Test_Case01
    obj_01 = Test_Case01A()
    obj_02 = Test_Case01A()
        
    print(f'Is only one instance = {id(obj_01) == id(obj_02)}\n')  # True, both variables point to the same instance
    #only one initialization message will be printed

    obj_01.test_execution()




    #---------------- for testing factory pattern in Test_Case02 and Test_Case03
    obj3 = Test_Case01D()
    obj3.test_execution("Test John")

    obj4 = Test_Case01C()
    obj4.test_execution("Test Alicja")


