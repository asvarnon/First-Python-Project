#Example

# class NameOfClass():

#     #constructor
#     def __init__(self, param1, param2):
#         self.param1
#         self.param2
    
#     #type self as param to connect it. 
#     def someMethod(self):
#         print(self.param1)




class Dog():

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots
    

myDog = Dog('Poodle', 'Joey', True)
print(myDog.breed)
print(myDog.name)
print(myDog.spots)
    
    


