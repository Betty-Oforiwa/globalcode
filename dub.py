def get_age():
    age=input("enter your age:")
    return age
    
    


def get_name():
    name=input("enter your name:")
    return name
    
    


def printinfo(name, age):
    "This prints passed into into this function"
    print ("Name:", name)
    print ("Age", age)
    return;
printinfo( get_age(),get_name() )

