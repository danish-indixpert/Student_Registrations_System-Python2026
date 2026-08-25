
import json
import datetime
data=[]
data_one=[]
student=[]

def register():
    print("==============================")
    print("*           Register         *")
    print("==============================")
    while True:
        try:
            uid=input("Enter Your ID: ")
            if int(uid.isalnum()):
                break
            else:
                raise ValueError("Invalid Id")
        except Exception as ii:
            print("Wrong Uid!")
        with open("System.log",'a') as uii:
            uii.write(f"[{str(datetime.datetime.now())}] [ERROR] - Invalid Your Uid!!!\n")
    while True:
        try:
            name=input("Enter Your Name: ")
            if name.isalpha():
                break
            else:
                raise ValueError("Invalid Name")            
        except Exception as n:
            print("Please Alphabet Value Only!")
        with open("System.log",'a') as nn:
            nn.write(f"[{str(datetime.datetime.now())}] [ERROR] - Invalid Your Name!!! {uid}\n")
    while True:
        try:
            age=input("Enter Your Age: ")
            if int(age.isdigit()):
                break
            else:
                raise ValueError("Invalid Age")
        except Exception as a:
            print("Please Integer (Digit) Value Only!")
        with open("System.log",'a') as aa:
            aa.write(f"[{str(datetime.datetime.now())}] [ERROR] - Invalid Your Age!!! {uid}\n")
    while True:
        try:
            email=input("Enter Your Email ID: ")
            if "@" in email and ".com" in email:
                break
            else:
                raise ValueError("Invalid email")
        except Exception as e:
            print("Please Correct Email ID!")
        with open("System.log",'a') as ee:
            ee.write(f"[{str(datetime.datetime.now())}] [ERROR] - Invalid Your Email!!! {uid}\n")
    while True:
        try:
            address=input("Enter Your Address: ")
            if address.isalpha():
                break
            else:
                raise ValueError ("Invalid Addresss")
        except Exception as adrs:
            print("Please Alphabet Value Only!")
        with open("System.log",'a') as add:
            add.write(f"[{str(datetime.datetime.now())}] [EROOR] - Invalid Your Address\n")
    while True:
        try:
            country=input("Enter Your Country: ")    
            if country.isalnum():
                break
            else:
                raise ValueError("Invalid country")
        except Exception as count:
            print("Plsease Correct Your Country")
        with open("System.log",'a') as cou:
            cou.write(f"[{str(datetime.datetime.now())}] [ERROR] - Invalid Your Country\n")
    data=uid,name,age,email,address,country
    student.append(data)
    with open("students_output.txt",'a') as register:
            register.write(f"{uid} | {name} | {age} | {email} | {address} | {country}\n")
    
            registeration={
                "uid":uid,
                "name":name,
                "age":age,
                "email":email,
                "address":address,
                "country":country,
            }
            data_one.append(registeration)    
            with open("Students_.json",'w')as student_registration:
                json.dump(data,student_registration,indent=4)
                print("Registeration Successful!")
def update():
    print("==============================")
    print("*           Update           *")
    print("==============================")
    update_uid=input("Enter UID ID: ")
    for update_data in data:
        if update_data["uid"] == update_uid:
            print("====================")
            print("*    Update Menu   *")
            print("====================")
            print("1. Name Update")
            print("2. Age Update")
            print("3. Address Update")
            print("4. Country Update")
            print("5. Back")
            choice_update=input("please Enter Your update choice: ")
            if choice_update=="1":
                new_name=input("Enter You New Name: ")
                update_data["name"]=new_name
                with open("Students_.json","w") as one_name:
                    json.dump(data,one_name,indent=4)
                    print("Your Name is Updated Successful!")
                    break
            elif choice_update=="2":
                new_age=input("Enter your new age: ")
                update_data["age"]=new_age
                with open("Students_.json","w") as one_age:
                    json.dump(data,one_age,indent=4)
                    print("your age is updated successful!")
                    break
            elif choice_update=="3":
                new_address=input("Enter you new address: ")
                update_data["address"]=new_address
                with open("Students_.json","w") as one_address:
                    json.dump(data,one_address,indent=4)
                    print("your address is updated successful!")
                    break
            elif choice_update=="4":
                new_country=input("Enter you new country: ")
                update_data["address"]=new_country
                with open("Students_.json","w") as one_country:
                    json.dump(data,one_country,indent=4)
                    print("your country is updated successful!")
                    break
            elif choice_update=="5":
                menu()
        else:
            print("Invalid Choice!")
    else:
        print("Email Not Found")
def delete():
    print("==============================")
    print("*           Delete           *")
    print("==============================")
    one_email=input("Enter Your Email ID: ")
    print("1. yes")
    print("2. no")
    delete_choice=input("Enter Your Choice: ")
    if delete_choice=="yes":
        for delete_data in data:
            if delete_data["email"]==one_email:
                data.remove(delete_data)
                with open("Students_.json","w") as one_file:
                    json.dump(data,one_file,indent=4)
                print("Student Delete Successful!")
                break
        else:
            print("Email Not Found")
    elif delete_choice=="no":
        print("Your Data is no Delete: ")
    else:
        print("Invalid Choice!")
def menu():
    print("==============================")
    print("*            Menu            *")
    print("==============================")
    while True: 
        print("1. Register")
        print("2. Update")
        print("3. Delete")
        choice=input("Enter Your Choice: ")
        if choice=="1":
            register()
        elif choice=="2":
            update()
        elif choice=="3":
            delete()
            break
        else:
            print("Invalid Choice!")

menu()