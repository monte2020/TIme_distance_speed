x = input("What variable do you not know? s- for speed. t- for time. d- for distance.")
if "s" == x:
    d = input("What is your distance? ")
    t = input("What is your time? ")
    print (str(d/t) + "is speed") 
elif "t" == x:
    d = input("What is your distance? ")
    s = input("What is your speed? ")
elif "d" == x:
    s = input("What is your speed? ")
    t = input("What is your time? ")
