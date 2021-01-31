# Forgot GLAFireAuth Pass


def forgortPass():
    
    print(f"_____GLA FireAuth Password Recovery_____\n")
    
    fullName = input(f"Enter Your Full Name : ")
    phoneNumber = input("Enter Your Phone Number: ")
    
    print(f"\nUsers name is {fullName} and Users Phone Number is {phoneNumber}\n")
    
    Digits_4_5 = phoneNumber[3:5]
    Digits_9_10 = phoneNumber[8:10]
    Surname_last_two = fullName[-2:]
    
    l = ['@','.','_']

    print(f"____________User Passwords may be the given below_____________\n\n")
    count = 0
    for item in l:
        count += 1
        print(f"TEST Case-{count} => {Digits_4_5}{item}B{Digits_9_10}{Surname_last_two}\n")

while True:
    forgortPass()
    print("\n\n")