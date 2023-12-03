import os

print("WELCOME TO THE CALCULATOR")

st1 = float(input("Enter the 1st number: "))
os.system("cls")
nd2 = float(input("Enter the 2nd number: "))
os.system("cls")
process = input("+" "-" "/" "*" " " ":")
os.system("cls")

if process == "+":
    print("conclusion: " + str(st1 + nd2))

elif process == "-":
    print("conclusion: " + str(st1 - nd2))

elif process == "/":
    print("conclusion: " + str(st1 / nd2))

elif process == "*":
    print("conclusion: " + str(st1 * nd2))

else:
    print("Wrong dialing")
