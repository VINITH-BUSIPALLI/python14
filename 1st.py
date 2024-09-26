print("+--------------------------------------+")
print("|HELLO WE WELCOME YOU TO SIDI SUPERMART|")
print("+--------------------------------------+\n+--------------------------------------+\n+--------------------------------------+\n+--------------------------------------+\n+--------------------------------------+\n")
print("|  COUSTOMER or ADMIN or EXIT          |")
print("+--------------------------------------+")
op=input("PLEASE ENTER YOUR OPTION BELOW\n")
if op == "coustomer":
    coustomer_name=input("enter your name:")
    number=input("enter your number")
    print("hello"+str(name)+"welcome to SIDI GROCERY")
elif op =="admin":
    admin_name=input("enter your name:")
    password=input("enter the password:")
    if password == "12345":
        print("hello admin welcome start your billing process")
