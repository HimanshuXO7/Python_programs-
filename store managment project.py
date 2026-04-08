import pickle
import os


# A METHOD TO ADD A CUSTOMER INFORMATION:

def addcostumer():
    file = open('costumer.bin','ab')
    cid = input("\n\t\tenter costumer id : ")
    cname = input("\t\tenter costumer name : ")
    caddress = input("\t\tenter costumer address :")
    cmobile = input("\t\tenter costumer mobile :")
    pickle.dump(cid, file)
    pickle.dump(cname, file)
    pickle.dump(caddress, file)
    pickle.dump(cmobile, file)
    print("\n\t\t costumer added successfully !!!")
    file.close()
    input("\n\t press enter to continue.... :")

# A METHOD TO VIEW ALL CUSTOMER's INFORMAION:





def viewallcostumer():
    file = open('costumer.bin','rb')
    try:
        while True:
            print("\n\t cid id:", pickle.load(file))
            print("\t cname :", pickle.load(file))
            print("\t caddress:", pickle.load(file))
            print("\t cmobile:", pickle.load(file))
            print("\t ****************")
    except:
        print("\n\t\t Here is all your products !!")
    file.close()
    input("\t\t press enter to continue....")


   

# A METHOD TO DELETE CUSTOMER's INFORMATION :

def deletecustomer():
    file1 = open('costumer.bin','rb')
    file2 = open('temp.bin','wb')   
    flag = 0
    cid = input("\n\tEnter Customer ID To Delete : ")

    try:
        while True:
            id = pickle.load(file1)
            name = pickle.load(file1)
            address = pickle.load(file1)
            mobile = pickle.load(file1)

            if id == cid:
                flag = 1   
            else:
                pickle.dump(id, file2)
                pickle.dump(name, file2)
                pickle.dump(address, file2)
                pickle.dump(mobile, file2)

    except EOFError:
        pass

    if flag == 0:
        print("\n\tCustomer Not Found!")
    else:
        print("\n\tCustomer Deleted Successfully!")

    file1.close()
    file2.close()

    os.remove('costumer.bin')
    os.rename('temp.bin','costumer.bin')

    input("\tPress Enter To Continue...")
          

# A METHOD TO ADD NEW PRODUCT's INFORMATION:


def addproduct():
    file = open('product.bin','ab')
    pid = input("\n\t\t enter product id :")
    pname = input("\t\t enter product name:")
    pprice = input("\t\t enter product price :")
    pickle.dump(pid,file)
    pickle.dump(pname,file)
    pickle.dump(pprice,file)
    print("\n\t\t product added succefully !")
    file.close()
    input("\n\t\t Press Enter To Continue...")



# A METHOD TO VIEW ALL PRODUCT's INFORMAION:

def viewallproduct():
    file = open('product.bin','rb')
    try:
        while True:
            print("\n\t product id:", pickle.load(file))
            print("\tproduct name :", pickle.load(file))
            print("\t product pprice :", pickle.load(file))
            print("\t ****************")
    except:
        print("\n\t\t Here is all your products !!")
    file.close()
    input("\t\t press enter to continue....")


# A METHOD TO UPDATE PRODUCT:

def updateproduct():
    file1 = open('product.bin','rb')
    file2 = open('temp.bin','ab')
    flag = 0
    pid = input("\n\tEnter Product ID To Update Price : ")
    try:
        while True:
            data = pickle.load(file1)
            if data==pid:
                pickle.dump(data,file2)
                name = pickle.load(file1)
                pickle.dump(name,file2)
                print("\tProduct Name : ",name)
                print("\tOld Price : ",pickle.load(file1))
                price = input("\tEnter New Price : ")
                pickle.dump(price,file2)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        if flag==1:
            print("\n\tPrice Updated Successfully!")
        else:
            print("\n\tProduct Not Found!")
    file1.close()
    file2.close()
    os.remove('product.bin')
    os.rename('temp.bin','product.bin')
    input("\tPress Enter To Continue...")

# A METHOD TO GET THE INFORMATION OF A CUSTOMER
def getCustomer(id_):
    cus = []
    file = open('customer.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if data==id_:
                cus.append(data)
                cus.append(pickle.load(file))
                cus.append(pickle.load(file))
                cus.append(pickle.load(file))
    except:
        pass
    file.close()
    return cus

# A METHOD TO GET THE INFORMATION OF A PRODUCT
def getProduct(id_):
    pro = []
    file = open('product.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if data==id_:
                pro.append(data)
                pro.append(pickle.load(file))
                pro.append(pickle.load(file))
    except:
        pass
    file.close()
    return pro

# A METHOD TO PLACE AN ORDER
def placeAnOrder():
    cid = input("\n\tEnter CID To Place Order : ")
    cus = getCustomer(cid)
    if len(cus)>0:
        print("\tCustomer Name :",cus[1])
        print("\tCustomer Address :",cus[2])
        pid = input("\n\tEnter Product ID To Order : ")
        pro = getProduct(pid)
        if len(pro)>0:
            print("\tProduct Name :",pro[1],)
            print("\tProduct Price :",pro[2],)
            qty = input("\n\tEnter Quantity : ")
            print("\tTotal Bill :",int(pro[2])*int(qty))
            print("\n\tOrder Placed Successfully!")
            file = open('order.bin','ab')
            pickle.dump(cid,file)
            pickle.dump(pid,file)
            pickle.dump(qty,file)
            file.close()
        else:
            print("\n\tProduct Not Found!")
    else:
        print("\n\tCustomer Not Found!")
    input("\tPress Enter To Continue...")

# A METHOD TO VIEW ALL ORDER's DETAILS
def viewAllOrders():
    file = open('order.bin','rb')
    oid = 1001
    try:
        while True:
            cus = getCustomer(pickle.load(file))
            pro = getProduct(pickle.load(file))
            qty = int(pickle.load(file))
            print("\tOrder ID :",oid)
            print("\tCustomer Name :",cus[1])
            print("\tCustomer Address :",cus[2])
            print("\tProduct Name :",pro[1])
            print("\tProduct Price :",pro[2])
            print("\tQuantity :",qty)
            print("\n\tTotal Bill :",int(pro[2])*qty,'/-')
            print("\t-----------------------\n")
            oid+=1
    except:
        print("\n\tHere is all the details")
    file.close()
    input("\tPress Enter To Continue...")

 # A METHOD TO VIEW ORDERS BY CID
def viewOrderByCID():
    file = open('order.bin','rb')
    cid = input("\n\tEnter CID To Display Orders : ")
    try:
        while True:
            cus = getCustomer(pickle.load(file))
            pro = getProduct(pickle.load(file))
            qty = int(pickle.load(file))
            if cus[0]==cid:
                print("\tCustomer Name :",cus[1])
                print("\tCustomer Address :",cus[2])
                print("\tProduct Name :",pro[1])
                print("\tProduct Price :",pro[2])
                print("\tQuantity :",qty)
                print("\n\tTotal Bill :",int(pro[2])*qty,'/-')
                print("\t-----------------------\n")
    except:
        print("\n\tHere is all the details")
    file.close()
    input("\tPress Enter To Continue...")

    
#DASHBOARD:

while True:
    print("\n\t\t STORE MANAGEMENT SYSTEM")

    print("""
                    1. Add costumer
                    2. view all costumer
                    3. delete a costumer
                    4. add a product
                    5. view all product
                    6. update product
                    7. place an order
                    8. view all order 
                    9. view all order by costumer id
                    0. exit """)
    ch = int(input("\n\t\t enter your choice :"))

    if ch==0:
        print("\n\t\t bye bye admin!!! ")
        break
    elif ch==1:
        addcostumer()
    elif ch==2:
        viewallcostumer()
    elif ch==3:
        deletecustomer()
    elif ch==4:
        addproduct()
    elif ch==5:
        viewallproduct()
    elif ch==6:
        updateproduct()
    elif ch==7:
        placeAnOrder()
    elif ch==8:
        viewAllOrders()
    elif ch==9:
        viewOrderByCID()
    else:
        input("\n\tWrong Entered! Try Again!")

