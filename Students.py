import json
import datetime
data_one=[]


def register():
    print("==============================")
    print("*           Register         *")
    print("==============================")
    while True:
        try:
            uid=input("Enter Your ID: ")
            if uid.isalnum():
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
            if age.isdigit():
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
            if address.isalnum():
                break
            else:
                raise ValueError ("Invalid Addresss")
        except Exception as adrs:
            print("Please Alphabet Value Only!")
        with open("System.log",'a') as add:
            add.write(f"[{str(datetime.datetime.now())}] [EROOR] - Invalid Your Address!!! {uid}\n")
    while True:
        try:
            country=input("Enter Your Country: ")    
            if country.isalpha():
                break
            else:
                raise ValueError("Invalid country")
        except Exception as count:
            print("Plsease Correct Your Country")
        with open("System.log",'a') as cou:
            cou.write(f"[{str(datetime.datetime.now())}] [ERROR] - Invalid Your Country!!! {uid}\n")
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
            with open("Students_.json",'w') as student_registration:
                json.dump(data_one,student_registration,indent=4)
            with open("System.log",'a') as reg:
                reg.write(f"[{str(datetime.datetime.now())}] [INFO] - Registration Successful {uid}\n")    
            print("Registeration Successful!")
def update():
    print("==============================")
    print("*         Update Menu        *")
    print("==============================")
    while True:
            print("1. Name Update")
            print("2. Age Update")
            print("3. Address Update")
            print("4. Country Update")
            print("5. Back")
            choice_update=input("please Enter Your update choice: ")
            update_uid=input("Enter UID ID: ")
            for update_data in data_one:
                if update_data["uid"] == update_uid:
                    if choice_update=="1":
                        try:                        
                            new_name=input("Enter You New Name: ")
                            if new_name.isalpha():
                                update_data["name"]=new_name
                                with open("Students_.json","w") as one_name:
                                    json.dump(data_one,one_name,indent=4)
                                print("Your Name Is Update")
                                break
                            else:
                                print("Invalid name")
                            with open("System.log",'a') as n_one:
                                n_one.write(f"[{str(datetime.datetime.now())}] [INFO] - Student Name Updated {update_uid}")
                        except Exception as one:
                            print("Invalid [Error]")
                    elif choice_update=="2":
                        try:
                            new_age=input("Enter your new age: ")
                            if new_age.isdigit():
                                update_data["age"]=new_age
                                with open("Students_.json","w") as one_age:
                                    json.dump(data_one,one_age,indent=4)
                                print("Your Age Is Update")
                                break
                            else:
                                print("Invalid Age")
                            with open("System.log",'a') as a_one:
                                a_one.write(f"[{str(datetime.datetime.now())}] [INFO] - Student Age Updated {update_uid}")
                        except Exception as two:
                            print(f"Invalid [Error] {two}")
                    elif choice_update=="3":
                        try:
                            new_address=input("Enter you new address: ")
                            if new_address.isalnum():
                                update_data["address"]=new_address
                                with open("Students_.json","w") as one_address:
                                    json.dump(data_one,one_address,indent=4)
                                print("Your Address Is Update")
                                break
                            else:
                                print("Invalid Address")
                            with open("System",'a') as add_one:
                                add_one.write(f"[{str(datetime.datetime.now())}] [INFO] - Student Address Updated {update_uid}")
                        except Exception as three:
                            print("Invalid [Error]")
                    elif choice_update=="4":
                        try:
                            new_country=input("Enter you new country: ")
                            if new_country.strip():
                                update_data["address"]=new_country
                                with open("Students_.json","w") as one_country:
                                    json.dump(data_one,one_country,indent=4)
                                print("Your Country Is Update")
                                break
                            else:
                                print("Invalid Country")
                            with open("System.log",'a') as c_one:
                                c_one.write(f"[{str(datetime.datetime.now())}] [INFO] - Student Country Updated {update_uid}")
                        except Exception as four:
                            print("invalid [Error]")
                    elif choice_update=="5":
                        menu()
                else:
                    print("Invalid Choice!")
            else:
                print("UID Not Found")
def delete():
    print("==============================")
    print("*           Delete           *")
    print("==============================")
    one_uid=input("Enter Your UID: ")
    print("==============================")
    print("*           Yes/No           *")
    print("==============================")
    print("1. yes")
    print("2. no")
    delete_choice=input("Enter Your Choice (yes/no): ")
    if delete_choice=="yes":
        for delete_data in data_one:
            if delete_data["uid"]==one_uid:
                data_one.remove(delete_data)
                with open("Students_.json","w") as one_file:
                    json.dump(data_one,one_file,indent=4)
                with open("System.log",'a') as d:
                    d.write(f"[{str(datetime.datetime.now())}] [WARNNING] - Student Deleted {one_uid}")
                print("Student Deleted Successful!")
        else:
            print("UID Not Found")
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