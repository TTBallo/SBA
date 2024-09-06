# Module import
import csv
import re
import time
import datetime
import random
import uuid

### Global variable
permission_stat = 0 # 1:customer 2:Shopper 3:Admin
p_name = "" # the name of the user
p_bday = "" # the birthday of the user
flag_bit = True
goods_data = "D:\SBA\SBA\goods_info.csv"
pickup_data = "D:\SBA\SBA\pickup_data.csv"

# admin information
admin_name = ["admin"]
admin_pw = ["123"]

# seller information
seller_name = ["Garden"]
seller_pw = ["Garden123"]

# customer information
customer_name = ["Tommy"]
customer_pw = ["5212023"]
customer_bday = [datetime.datetime(2023,5,21)]
shopping_cart = [["NAME","ID","PRICE","Quantity","Total cost"]]

# goods information
age_required = ["066"]

# Searching
def binary_search(matrix,target) : # Binary search 
    high = len(matrix)-1
    low = 0
    mid = 0
    while low <= high :
        mid = (high + low)//2
        if matrix[mid] == target :
            return mid
        elif target > matrix[mid] :
            low = mid +1
        else :
            high = mid -1
    return False

def find(matrix,target) : # To find the index of an item in a list
    for pos , item in enumerate(matrix) :
        if item == target :
            return pos
    return False

def searching(raw_list,index,item) :
    new_list = []
    new_list.append(raw_list[0])
    for row in raw_list :
        if item in row[index] and row != raw_list[0]:
            new_list.append(row)
    return new_list

# Sorting with 2d array
def selection_sort(raw_list,index,start) : #find the smallest item and switch
    for i in range(start,len(raw_list)-1) :
        pos = i 
        for j in range(i+1,len(raw_list)) :
            if raw_list[j][index] < raw_list[pos][index] :
                pos = j
        raw_list[i],raw_list[pos] = raw_list[pos],raw_list[i]

def bubble_sort(raw_list,index,start) : #switch the nearby items 
    for i in range(start,len(raw_list)) :
        current_pos = i
        while current_pos >= start and float(raw_list[current_pos][index]) < float(raw_list[current_pos-1][index]) :
            raw_list[current_pos] , raw_list[current_pos-1] = raw_list[current_pos-1] ,  raw_list[current_pos]
            current_pos -=1 

def insertion_sort(raw_list,index,start) : #pull the item back until find a correct place
    for i in range(start,len(raw_list)) :
        store2d = raw_list[i]
        store = raw_list[i][index]
        next = i-1
        while next >= 0 and raw_list[next][index] > store :
            raw_list[next+1] = raw_list[next]
            next -=1
        raw_list[next+1] = store2d

def sorting_show(way) :
    with open(goods_data,"r", newline='', encoding='utf-8-sig') as goods_info :
            goods = list(csv.reader(goods_info))     
            if way == "SID" :
                insertion_sort(goods,1,2) 
            elif way == "SP" :
                bubble_sort(goods,3,2)
            elif way == "SN" :
                selection_sort(goods,0,1)
            elif way == "S" :
               view(searching(goods,0,str(input("The name of the good you want ( Case Sensitive ): "))))
               return None
            elif way == "SWID" :
               view(searching(goods,1,str(input("The ID of the good you want : "))))
               return None
            view(goods)

# Login
def new_user() :
    new_role = str(input("Register : S-Seller / C-Customer : "))
    if new_role == "S" : # Create new seller
        new_name = str(input("Your name is : ")) 
        if new_name not in seller_name : # check if the new name does not repeat 
            seller_name.append(new_name)
        else :
            print("Your name has been used , try again !")
            return False
        new_pw = str(input("Your password is : "))
        while pw_check(new_pw) is False : # data validation
            new_pw = str(input("Your password is : "))
        seller_pw.append(new_pw)
        return True
    elif new_role == "C" :
        new_name = str(input("Your name is : "))
        if new_name not in customer_name :
            customer_name.append(new_name)
        else :
            print("Your name has been used , try again !")
            return False
        new_pw = str(input("Your password is : "))
        while pw_check(new_pw) is False :
            new_pw = str(input("Your password is : "))
        customer_pw.append(new_pw)
        print("Please fill in your birthday for more discount and goods available") # only 18+ can buy alcohol
        customer_bday.append(date_input())
        return True
    else :
        print("Please fill in S / C !")
        new_user()

def date_input() :
    try :
        x,y,z= input("Enter the date (YYYY/MM/DD) :").split("/")
        new_date = datetime.datetime(int(x),int(y),int(z))
        return new_date
    except ValueError: # error handling
        print("RANGE of Date must between 1/1/1 to 9999/12/31 and The inputs must be INTEGER")
        date_input()    

def pw_check(pw) :
    if len(pw) <8:
        print("Your password must be at least 8 characters long !")
        return False
    if len(pw) >20 :
        print("Your password must not exceed 20 characters ! ")
        return False
    if any(char.isupper() for char in pw) :
        pass
    else :
        print("There should be at least one capital letter")
        return False
    if any(char.isdigit() for char in pw) :
        pass
    else :
        print("There should be at least one number")
        return False
    if pw.count(' ') > 0 :
        print("No spaces are allowed")
        return False
    pw_double_check = str(input("Please input the password again :")) # data verificaton by entering the data twice
    while pw_double_check != pw :
        print("The second password is NOT the same with the first one")
        pw_double_check = str(input("Please input the password again : "))
    return True

def login() : # Main log in
    global permission_stat
    for i in range(50) : print("=" , end="")
    role = str(input("\n You are : A - Admin / S - Seller / C - Customer / NEW - New account registration( Please fill in short form ) : "))
    if role == "A" : # Admin log in
        while admin_login() == False :
            pass
        permission_stat = 3
    elif role == "S" : # Seller log in
        while seller_login() == False :
            pass
        permission_stat = 2
    elif role == "C" : # Customer log in
        while customer_login() == False :
            pass
        permission_stat = 1
    elif role == "NEW" : # Creating new account
        while new_user() == False :
            pass
        login()
    else : # Invalid input
        print("Please fill in valid short form (A/S/C/NEW) ! ")
        login()

def admin_login() :
    global p_name
    login_name = str(input("Hi Admin , Your username is : "))
    if login_name in admin_name :
        location = find(admin_name,login_name)
        login_pw = str(input("Hi Admin , Your password is : "))
        if admin_name[location] == login_name and admin_pw[location] == login_pw : # check if the account matches with the password
            print("")
            print("Welcome Admin {} !".format(login_name))
            p_name = login_name
            return True
        else :
            print("Your password is NOT correct , please try again")
    else :
        print("Username does NOT exist , please try again")
    return False

def seller_login() :
    global p_name
    login_name = str(input("Hi Seller , Your username is : "))
    if login_name in seller_name :
        location = find(seller_name,login_name)
        login_pw = str(input("Hi Seller , Your password is : "))
        if seller_name[location] == login_name and seller_pw[location] == login_pw : # check if the account matches with the password
            print("")
            print("Welcome Seller {} !".format(login_name))
            p_name = login_name
            return True
        else :
            print("Your password is NOT correct , please try again")
    else :
        print("Username does NOT exist , please try again")
    return False

def customer_login() :
    global p_bday
    global p_name
    login_name = str(input("Hi Customer , Your username is : "))
    if login_name in customer_name :
        location = find(customer_name,login_name)
        login_pw = str(input("Hi Customer , Your password is : "))
        if customer_name[location] == login_name and customer_pw[location] == login_pw : # check if the account matches with the password
            print("")
            print("Welcome Customer {} !".format(login_name))
            p_name = login_name
            p_bday = customer_bday[location]
            return True
        else :
            print("Your password is NOT correct , please try again")
    else :
        print("Username does NOT exist , please try again")
    return False

# Main Menu
def menu() : # showing the commands available for different roles
    time.sleep(1.5)
    print("")
    for i in range(50) : print("*" , end="")
    print("\nWelcome to the Control Menu , {} Enjoy your time in our supermarket ! \n"
          "Here are the Commands for our online market : \n"
          "V - View the available goods in our market \n"
          "SN - Sort the goods by Name \n"
          "SP - Sort the goods by Price \n"
          "SID - Sort the goods by the ID\n"
          "S - Search for specific goods by name\n"
          "SWID - Search for specific goods with the goods ID\n"
          "F - Filter the goods with unwanted brand".format(p_name)) #<--------------
    if permission_stat == 3 or permission_stat == 2 : # shopper can add , modify , delete their OWN goods while admin can do without limitaton
        print("A - Add goods of YOUR brand \n"
              "M - Modify the status of goods by YOUR brand \n"
              "D - Delete the goods by YOUR brand")
        if permission_stat == 2 :
            print("*** Admin can freely use those command without any limitation")
    elif permission_stat == 1 : # customer can use shopping cart to buy goods
        print("VC - View your shopping Cart \n"
              "AC - Add goods to your shopping Cart \n" #<--------------
              "EC - Edit your shopping Cart\n" #<--------------
              "CO - Check Out of your shopping cart") #<--------------
    print("QUIT - Quit this application")   
 
def menu_control(access) :
    global permission_stat
    global flag_bit
    global p_name
    control = str(input("Your command is : "))

    if control in ["V","SN","SP","SID","S","SWID"] :
        sorting_show(control)

    elif control == "A" :
        if permission_check(permission_stat,2) : # if the user is seller
            while add_goods(permission_stat,p_name) == False : # use the log in name as the company name to add goods
                pass
        elif permission_check(permission_stat,3) :
            add_name = str(input("The name of company of the adding good :")) # admin can choose the name of company by itself
            while add_goods(permission_stat,add_name) == False : # use the log in name as the company name to add goods
                pass
        else :
            print("Access Denied : Seller and Admin ONLY")

    elif control == "M" :
        if permission_check(permission_stat,2) or permission_check(permission_stat,3): # only admin and seller can modify goods 
            change = str(input("The change of the good is (NAME/COMPANY/PRICE/STOCK) :"))
            if change == "COMPANY" and permission_check(permission_stat,2) :
                print("Seller can NOT change the company of goods")
                return False
            input_dicts = {"NAME":0,"COMPANY":2,"PRICE":3,"STOCK":4}
            if change in input_dicts :
                id = str(input("The ID of the good is :"))
                new_value = str(input("The new value of the good is :"))
                modify(p_name,id,input_dicts[change],new_value)
            # The ID should NOT be change by anyone , even for admin
            #elif change == 1 :
            #    print("The ID of the good is NOT allowed to Change")
            else :
                print("INVALID input , please try again")

    elif control == "D" :
        if permission_check(permission_stat,2) or permission_check(permission_stat,3): # only admin and seller can delete goods
            delete_id = str(input("The ID of the good you want to delete is :"))
            delete(p_name,delete_id)

    elif control == "VC" :
        if permission_check(permission_stat,1) : # only customer can use the shopping cart function
            view(shopping_cart)
        else :
            print("Access Denied : Customer ONLY")
            return False
    
    elif control == "AC" :
        if permission_check(permission_stat,1) : # only customer can use the shopping cart function
            try :
                c_id = input("The ID of the goods :")
                c_q = int(input("The quantity of the goods :"))
            except ValueError :
                print("Your input must be a integer") # error handling
                return False
            add_cart(c_id,c_q)
        else :
            print("Access Denied : Customer ONLY")
            return False    

    elif control == "EC" :
        if permission_check(permission_stat,1) :
            try :
                c_id = input("The ID of the goods :")
                c_q = int(input("The NEW quantity of the goods :"))
            except ValueError :
                print("Your input must be a INTEGER") # error handling
                return False
            if c_q <= 0 :
                print("ERROR : quantity can NOT be less than 1")
                return False
            with open(goods_data,"r+", newline='', encoding='utf-8') as goods_info :
                goods = list(csv.reader(goods_info))  
                for x in range(1,len(goods)) :
                    if int(goods[x][4]) < c_q and goods[x][1] == c_id:
                        print("ERROR : Insufficient quantity of goods")
                        return False
            change_cart(c_id,c_q)
        else :
            print("Access Denied : Customer ONLY")
            return False
        
    elif control == "DC" :
        if permission_check(permission_stat,1) :
            c_id = input("The ID of the goods :")
            for x in range(len(shopping_cart)) :
                if shopping_cart[x][1] == c_id :
                    shopping_cart.pop(shopping_cart[x])
                    return True
            print("ERROR : ID not found in the shopping cart")
            return False 
        else :
            print("Access Denied : Customer ONLY")
            return False
        
    elif control == "CO" :
        global flag_bit
        total = check_out()
        print("The total amount will be ${} ".format(total))
        CO_choice = str(input("Delivery and Pickup are available (D/P) :"))
        if CO_choice == "P" :
            view_pickup()
            while not pickup_check() : # to confirm the location and time
                pass
            flag_bit = False
        elif CO_choice == "D" :
            address = str(input("Your address is :"))
            delivery(address)
        else :
            print("Unknown input , please retry")
            return False

    elif control == "QUIT" :
        flag_bit = False

    else :
        print("Commend NOT identified")

def permission_check(p,r) : # check if the permission of the log in allows to use that function
    p_dict = {1:"Access Denied : Customer Only",2:"Access Denied : Seller Only",3:"Access Denied : Admin Only"}
    #if p!=r :
    #    print(p_dict[r])
    return p==r

def view(data) : # output the formatted table-form of data of goods
    for i in range(70) : print("-" , end="")
    print("")
    for row in data :
        print('| {:>19} | {:>3} | {:>12} | {:>10} | {:>10} | '.format(row[0],row[1],row[2],row[3],row[4]))
    for i in range(70) : print("-" , end="")
    for i in range(2) : print("")

def view_pickup() :
    with open(pickup_data,"r", encoding='utf') as pickup_L : # read the location for pickup
        p_L = list(csv.reader(pickup_L)) 
        for i in range(84) : print("-" , end="")
        print("")
        for row in p_L :
            print('| {:>20} | {:>30} | {:>8} | {:>5} | {:>5} | '.format(row[0],row[1],row[2],row[3],row[4]))
        for i in range(84) : print("-" , end="")
        for i in range(2) : print("")

def add_goods(p,c) : # write the new data to the csv file with the company name filled
    n,id,p,s = str(input("Please input the NAME , ID , PRICE , STOCK of the goods\n" # input new data
                         "*Separate by SPACE* e.g.Banana 001 10 1 :")).split(" ")
    with open(goods_data,"r+", newline='', encoding='utf-8') as goods_info :
        goods = list(csv.reader(goods_info))  
        for x in range(1,len(goods)) :
            if id == goods[x][1] :
                print("ERROR : The ID of the good should be UNIQUE ") # search if any repeat of ID
                return False
    if float(p) <0 or float(s) <0 :
        print("The price or stock must NOT less than 0")
        return False
    while age_limit(id) == False :
        pass
    add([n,id,c,p,s]) 
    print("Command ADD has successfully executed")
    return True

def age_limit(id) : # check if the products requires 18 yrs old or above to purchase
    age_limit = str(input("Does your product has AGE LIMITATION (Under the law of Hong Kong, intoxicating liquor must not be sold or supplied to a minor in the course of business.) (Y/N) :"))
    if age_limit == "Y" or age_limit == "N" :
        if age_limit == "Y" :
            age_required.append(id) # add in the list of goods id which requires age verification while purchasing
        return True
    else :
        print("Please fill in either Y/N ")
        return False
    
def age_check(date) :
    today = datetime.datetime.today()
    age = today-date
    if age.days >= 6570 : # Check if the user is above 18 yrs old
        return True
    print("Your age is under 18 \n"
          "Under the law of Hong Kong, intoxicating liquor must not be sold or supplied to a minor in the course of business.\n"
          "We can NOT sell this goods to you")
    return False

def add(data) : # write the new data to the csv file
    with open(goods_data,"a", newline='', encoding='utf-8') as goods_info :
        writer = csv.writer(goods_info)
        writer.writerow(data)

def modify(company,id,new_pos,new_variable) : # changing the data of goods by overwriting the original data of the goods
    finding = False
    with open('D:\Python\Book1.csv',"r", newline='', encoding='utf-8') as f:
        r = csv.reader(f) #read the original data
        lines = list(r) #change the raw data into lists for better indexation
        for pos,row in enumerate(lines) :
                if pos != 0 and (row[2] == company or permission_check(permission_stat,3))and row[1] == id : # if the ID belongs to the company that logged in # Admin can edit without limitation
                    if (new_pos == 2 or new_pos == 3) and float(new_variable) >= 0 :
                        lines[pos][new_pos] = new_variable # Change the data
                        finding = True # end the finding process
                    else :
                        print("ERROR : The price or stock must NOT less than 0")
        if not finding :
            print("ERROR : The ID does NOT BELONG to YOUR Company or the ID does NOT EXIST")
            return False
    writeData(lines)
    print("Command MODIFY has successfully executed")

def delete(company,id) :
    finding = False
    with open('D:\Python\Book1.csv',"r", newline='', encoding='utf-8') as f:
        r = csv.reader(f) #read the original data
        lines = list(r) #change the raw data into lists for better indexation
        for pos,row in enumerate(lines) :
                if pos != 0 and (row[2] == company or permission_check(permission_stat,3)) and row[1] == id : # seller can only delete their OWN goods while admin can delete ALL goods
                    lines.remove(row)
                    finding = True
        if not finding :
            print("The ID does NOT BELONG to YOUR Company or the ID does NOT EXIST")
            return False
    writeData(lines)
    print("Command DELETE has successfully executed")
                
def writeData(lines) :
    with open(goods_data,"w", newline='', encoding='utf-8') as goods_info :
        writer = csv.writer(goods_info) # overwrite the data into the file by replacing old data and writing new data
        writer.writerows(lines)

def add_cart(id,quantity) :
    global shopping_cart
    finding = False
    with open(goods_data,"r+", newline='', encoding='utf-8') as goods_info :
        goods = list(csv.reader(goods_info))  
        for x in range(1,len(goods)) :
            if id == goods[x][1] :
                if id in age_required :
                    if age_check(p_bday) :
                        pass
                    else :
                        return False 
                if int(goods[x][4]) >= quantity > 0: # check if the stock is sufficient for purchase
                    shopping_cart.append([goods[x][0],goods[x][1],goods[x][3],quantity,(float(goods[x][3])*float(quantity))])
                    finding = True
                    print("Command ADD CART has successfully executed")
                    return True
                else :
                    print("ERROR : Insufficient goods for purchase or Invalid amount of purchase")
                    return False
        if finding == False :
            print("ERROR : ID do NOT exists")
            return False

def change_cart(id,quantity) : # changing the data of goods by overwriting the original data of the goods
    finding = False
    for pos,row in enumerate(shopping_cart) : 
        if pos != 0 and row[1] == id : # find the goods 
            shopping_cart[pos][3] = quantity # Change the quantity
            shopping_cart[pos][4] = float("{:.2f}".format(float(shopping_cart[pos][2])*float(shopping_cart[pos][3]))) # change the total 
            finding = True # end the finding process
            print("Command CHANGE CART has successfully executed")
    if not finding :
        print("The ID does NOT in the Shopping cart or the ID does NOT EXIST")
        return False  

def check_out() :
    total = 0
    for pos,row in enumerate(shopping_cart) :
        if pos != 0 : 
            total += float(shopping_cart[pos][4])
    return float("{:.2f}".format(total))

def pickup_check() : # check the pickup location and time are available
    with open(pickup_data,"r") as data :
        times = list(csv.reader(data))
        name = str(input("The name of the pickup store :"))
        pickup_date = date_input()
        if pickup_date < datetime.datetime.now() : # avoid the pickup date is before or in today
            print("The date allocated must be the at least 1 day after the date of ordering")
            return False
        if pickup_date  > datetime.datetime.now()+ datetime.timedelta(days=30) : # avoid the pickup date is after 30 days from now on
            print("The pickup date should be within 30 days from the date of ordering")
            return False
        h,min= input("Please input the time for the pickup\n"
                     "with hours and minutes e.g. :13 30 :").split(" ") # input the desire time
        for x in range(1,len(times)) :
            if times[x][0] == name :
                start = datetime.time(int(times[x][3][:2]), int(times[x][3][2:]), 0)
                end = datetime.time(int(times[x][4][:2]),int(times[x][4][2:]),0)
                need_time =datetime.time(int(h),int(min),0).strftime('%Y-%m-%d %H:%M')
                if start <= end or (start <= need_time or need_time <= end): # return if possible for pickup
                        payment() # pay the money through online method
                        print(f"The pickup will be allocated at {need_time} on {pickup_date.date()}\n"
                        "Please pickup your goods with code given on the booked time at the pickup store\n")
                        return True
                else:
                    print("The store is NOT at service at that time , please try another time within the service hours")
                    return False
        print("Store NOT found , please check the name of the available stores") # if the loop does not return , the store name is not found in the data
        return False

def delivery(address) :
    global flag_bit
    delivery_date = date_input()
    if delivery_date < datetime.datetime.now()+ datetime.timedelta(days=7) :
        print("The date of delivery must be 7 days after the ordering date"
              "If you want to enjoy a faster delivery service , please consider our Delivery Express service")
        return False
    print("The delivery service available from 0900-1200 (AM) and 1400-1800(PM) ")
    delivery_time = str(input("The time for delivery is (AM/PM) :"))
    if delivery_time not in ["AM","PM"] :
        print("Please fill in AM/PM")
        return False
    payment()
    print(f"The address for this delivery is {address} \n"
          f"Your delivery will be arrived on {delivery_date.strftime('%Y-%m-%d %H:%M')} at {delivery_time}")    
    flag_bit = False

def payment() :
    # The simulation of payment
    payment = str(input("Please enter ur credit card number :"))
    v_code = str(input("Please enter ur safety code :"))
    v_date = str(input("Please enter ur expire date :"))
    time.sleep(3)
    print("Payment in process ... ")
    time.sleep(3)
    print("Payment succeed\n"
          f"Your CODE for this purchase is {uuid.uuid4()} \n" # creating an unique purchase code
          "Welcome for your next purchase !")

 # Main Loop
if __name__ == "__main__" :
    login()
    while flag_bit :
        menu()
        menu_control(permission_stat)