class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        print("Number of toys - "+str(self.number_of_toys))

miley_cyrus = Child("Cyrus", "Blue", 5)
miley_cyrus.show_info()

##billy_cyrus = Parent("Cyrus", "blue")
##billy_cyrus.show_info()

##print(miley_cyrus.last_name)
##print(miley_cyrus.number_of_toys)
##print(billy_cyrus.last_name)

'''
1. initialize the variables (last name & eye_color) for the parent
2. the init fn will recieve a couple of values as arguments 
3. create an instance of class parent called billy_cyrus
Note - would keep the parent and the instance in separate files usually
Next - we make class child which will inherit from class Child
4.syntax: class child will now inherit everything everything in parent class
5.initial the parents class variables
6. create an instanse of the class child

Part II. 
1. define an simple instance method inside class parent eg. show_info
2.call tihs instance

'''
