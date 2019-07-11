x = input("What variable do you not know? s- for speed. t- for time. d- for distance.")
if "s" == x:
    d = float(input("What is your distance? "))
    t = float(input("What is your time? "))
    print (str(d/t) + "m/s is your speed") 
elif "t" == x:
    d = float(input("What is your distance? "))
    s = float(input("What is your speed? "))
    print (str(d/s) + "s is your time") 

elif "d" == x:
    s = float(input("What is your speed? "))
    t = float(input("What is your time? "))
    print (str(s*t) + "m is your distance") 
else:
    print("Error input invalet")
    
#dts = 0