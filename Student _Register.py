import uuid
import json
data=[]

def register():
    print("==============================")
    print("*           Register         *")
    print("==============================")
    email=input("Enter Student Email ID: ")
    name=input("Enter Student Name: ")
    age=int(input("Enter Student Age: "))
    mobile=int(input("Enter Student Mobile Number: "))
    address=input("Enter Student Address: ")
    pincode=int(input("Enter Student Pincode: "))
    qualification=input("Enter Student Qualification: ")
    one_=str(uuid.uuid4())[:11]
    
    registeration={
        "uid":one_,
        "email":email,
        "name":name,
        "age":age,
        "mobile":mobile,
        "address":address,
        "pincode":pincode,
        "qualification":qualification
        
    }
    data.append(registeration)    
    with open("students.json",'w')as student_registration:
        json.dump(data,student_registration,indent=4)
        print("Registeration Successful!")
def update():
    print("==============================")
    print("*           Update           *")
    print("==============================")
    update_email=input("Enter Email ID: ")
    for update_data in data:
        if update_data["email"] == update_email:
            choice_mobile=input("You Are Mobile Number Update (yes/no): ")
            if choice_mobile=="yes":
                new_mobile=input("Enter You New Mobile Number: ")
                update_data["mobile"]=new_mobile
                with open("students.json","w") as one_file:
                    json.dump(data,one_file,indent=4)
                    print("Your Data is Updated Successful!")
                    break
            elif choice_mobile=="no":
                print("Your Data No Update!")
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
                with open("students.json","w") as one_file:
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