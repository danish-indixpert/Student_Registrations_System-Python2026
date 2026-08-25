import datetime
import json
student=[]
data_=[]


def students():
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
            county=input("Enter Your Country: ")    
            if county.isalnum():
                break
            else:
                raise ValueError("Invalid country")
        except Exception as count:
            print("Plsease Correct Your Country")
        with open("System.log",'a') as cou:
            cou.write(f"[{str(datetime.datetime.now())}] [ERROR] - Invalid Your Country\n")
    data=uid,name,age,email,address,county
    student.append(data)
    with open("students_output.txt",'a') as register:
        
            register.write(f"{uid} | {name} | {age} | {email} | {address} | {county}\n")

            student_data={
                        "uid":uid,
                        "name":name,
                        "age":age,
                        "email":email,
                        "address":address,
                        "country":county

            }
            data_.append(student_data)
            with open("Students_.json",'w') as s:
                json.dump(data_,s,indent=4)
            
                print("Student Registeration Successful!")

    with open("System.log",'a') as stu:
            stu.write(f"[{str(datetime.datetime.now())}] [INFO] - Student Accepted Successful {uid}\n")
# def stu_update():
#         # u_uid=input("Please Enter UID: ")
        # for u_update in data_:
        #     if u_update["uid"]==u_uid:
        #         update_choice=input("Enter Your Choice (yes/no): ")
        #         if update_choice=="yes":
def stu_update():
    print("====================")
    print("*      Update      *")
    print("====================")
    while True:
        print("1. Name Update")
        print("2. Age Update")
        print("3. Address Update")
        print("4. Country Update")
        print("5. Back")
        update_choice=input("Enter Your Update Choice: ")
        new_uid=input("Enter Your UID: ")
        for update_i in data_:
            if update_i["uid"]==new_uid:
                if update_choice=="1":
                    try:
                        new_name=input("Please Enter New Name: ")
                        if new_name.isalpha():
                            update_i["name"]=new_name
                            break
                        else:
                            print("Invalid Name")
                        
                        with open("Students_.json",'w') as new_name_:
                            json.dump(data_,new_name_,indent=4)
            
                        with open("System.log",'a') as t:
                            t.write(f"[{str(datetime.datetime.now())}] [INFO] - Student Name Updated {new_uid}\n")
                            print("Name Update Successful")
                    except Exception as tt:
                        print("Invalid Your Name!")
            
                elif update_choice=="2":
                
                    try:
                        new_age=input("Please Enter New Age: ")
                        if new_age.isdigit():
                            update_i["age"]=new_age
                            break
                        else:
                            print("Invalid Age")
                        
                        with open("Students_.json",'w') as new_age_:
                            json.dump(data_,new_age_,indent=4)
                        with open("System.log",'a') as uta:
                            uta.write(f"[{str(datetime.datetime.now())}] [INFO] - Student Age Updated {new_uid}")
                            print("Age Update Successful")
                    except Exception as uc:
                        print("Invalid Your Age!")
                elif update_choice=="3":
                    try:
                        new_address=input("Please Enter New Address: ")
                        if new_address.isdigit():
                            update_i["address"]=new_address
                            break
                        else:
                            print("Invalid Address")
                        
                        with open("Students_.json",'w') as new_address_:
                            json.dump(data_,new_address_,indent=4)
                        with open("System.log",'a') as utadd:
                            utadd.write(f"[{str(datetime.datetime.now())}] [INFO] - Student Address Updated {new_uid}")
                            print("Address Update Successful")
                    except Exception as uc:
                        print("Invalid Your Age!")
                elif update_choice=="4":
                    try:
                        new_country=input("Please Enter New Country: ")
                        if new_country.isalpha():
                            update_i["country"]=new_country
                            break
                        else:
                            print("Invalid Country")
                        
                        with open("Students_.json",'w') as new_country_:
                            json.dump(data_,new_country_,indent=4)
                        with open("System.log",'a') as utl:
                            utl.write(f"[{str(datetime.datetime.now())}] [INFO] - Student Country Updated {new_uid}")
                            print("Country Update Successful")
                    except Exception as uc:
                        print("Invalid Your Country!")
                elif update_choice==5:
                    option()
            else:
                print("Invalid Your Update Choice!!!")
                break
        else:
            print("UID Not Found")
        
def stu_delete():
    pass
def option():
    while True:
        print("====================")
        print("*       Menu       *")
        print("====================")
        print("1. Register")
        print("2. Update")
        print("3. Delete")
        print("4. Exit")
        your_choice=input("Enter Your Option: ")
        if your_choice=="1":
            students()
        elif your_choice=="2":
            stu_update()
        elif your_choice=="3":
            stu_delete()
        elif your_choice=="4":
            print("Thank Your User!")
            break
        else:
            print("Invalid Your Choice!")
option()

