print("+--------------------------------------+")
print("|HELLO WE WELCOME YOU TO SIDI SUPERMART|")
print("+--------------------------------------+")
print("|  COUSTOMER or ADMIN or EXIT          |")
print("+--------------------------------------+")
op=input("PLEASE ENTER YOUR OPTION BELOW\n")  
def login():
    if op == "coustomer":
        coustomer_name=input("enter your name:")
        number=input("enter your number")
        print("hello"+coustomer_name+"welcome to SIDI GROCERY")
    elif op =="admin":
        admin_name=input("enter your name:")
        password=input("enter the password:")
    elif op!="coustomer" && op!="admin" && op!="exit" :
        print("enter a valid option")
    else :
        exit()
def products():
    product_name=input("enter the product name:")
    product_mrp=int(input("enter the product mrp:"))
    product_qty=int(input("enter the product quantity adding:"))
def billing():
    print("+----------------------------------------------------+");
    print("|    name     |     qty    |    mrp    |    price    |");
    print("+----------------------------------------------------+");
    print("    "+product_name+"        "+str(product_qty)+"        "+str(product_mrp)+"        "+str(product_mrp*0.9));
    print("+-----------------------------------------------------+");
def toy_store():
    print(product_name+"    |    "+str(product_mrp));
    
    
    
    
