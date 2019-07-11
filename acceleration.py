x = input("Which variable do you want to know. S1- starting speed, S2- end speed, T2- end time, A- Acceleration ")
if x == "S1":
    S2 = float(input("What is your end speed? "))
    T2 = float(input("What is your end time? "))
    A = float(input("What is your acceleration? "))
    print("Your start speed is " + str((S2) - (A * T2)) + " m/s")
elif x == "S2":
    S1 = float(input("What is your start speed? "))
    T2 = float(input("What is your end time? "))
    A = float(input("What is your acceleration? "))
    print("Your end speed is " + str(S1 + (A * T2)) + " m/s")
elif x == "T2":
    S1 = float(input("What is your start speed? "))
    S2 = float(input("What is your end speed? "))
    A = float(input("What is your distance? "))
    print("Your end time is " + str((S2/A) - (S1/A)) + " s")
elif x == "A":
    S1 = float(input("What is your start speed? "))
    S2 = float(input("What is your end speed? "))
    T2 = float(input("What is your end time? "))
    print("Your acceleration is " + str((S2/T2) - (S1/T2)) + " m/s^2")
else:
    print("Error! Invalid input variables ")