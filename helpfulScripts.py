##Random generated list
myList = [x for x in range(1,10)]
##also
myExponentList = [x**2 for x in range(1,11)]

## list with only Evens
myOtherList = [x for x in range(1,11) if x%2 ==0]

##Temp converter (C to F)
celcius = [0,10,20,30,34.4]
fahrenheit = [( (9/5)*temp + 32) for temp in celcius]