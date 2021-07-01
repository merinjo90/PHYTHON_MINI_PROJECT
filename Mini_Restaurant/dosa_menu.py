def Mini_dosaCorner():
    print("Name: Merin Joseph")
    print("")
    print("Subject: python")
    print("")
    print("TOPIC: Mini Restaurant DosaCorner")
    print("")

    print("$"*40,"WELCOME TO WHITE MINIDOSACORNER","$"*40)
    print("")
    print("$"*30,"SELECT YOUR FAVOURITE AND YUMMY DOSA !!!!!!!!!!!","$"*30)
    print("")
    print("MENU\n")
    print("1 SADA DOSA @ RS.50")
    print("2 CHEESE DOSA @ RS.180")
    print("3 SECHEZWAN DOSA @ RS.150")
    print("4 MASALA DOSA @ RS.90")
    print("5 SWEET CORN DOSA @ RS.120")
    print("6 CHEESE MASALA DOSA @ RS.200")
    print("")

    subtotal=0
    cgst=0
    sgst=0
    total=0

    ch=int(input("Enter your choice: "))
    if ch==1:
        SD=int(input("Enter Quantity:"))
        subtotal=SD*50
        cgst=subtotal*0.05
        sgst=subtotal*0.05
    elif ch==2:
        CD=int(input("Enter Quantity: "))
        subtotal = CD* 180
        cgst = subtotal * 0.05
        sgst = subtotal * 0.05
    elif ch==3:
        SW=int(input("Enter Quantity:"))
        subtotal=SW*150
        cgst=subtotal*0.05
        sgst = subtotal * 0.05
    elif ch ==4:
        MD = int(input("Enter Quantity: "))
        subtotal = MD *90
        cgst = subtotal * 0.05
        sgst = subtotal * 0.05
    elif ch == 5:
        SCD = int(input("Enter Quantity:"))
        subtotal =SCD* 200
        cgst = subtotal * 0.05
        sgst=subtotal * 0.05
    elif ch == 6:
        CMD = int(input("Enter Quantity:"))
        subtotal = CMD * 200
        cgst = subtotal * 0.05
        sgst = subtotal * 0.05
    else:
        print("Entered choice is not available!!!! try again")

    total=subtotal+cgst+sgst
    print("*"*20,"RECIPT","*"*20)
    print("subtotal: ",subtotal)
    print("cgst    : ",cgst)
    print("sgst    : ",sgst)
    print("total   : ",total)
    print("")



Mini_dosaCorner()