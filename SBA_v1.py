# Module import
import csv
import re

# Global variable
admin_name = ["admin"]
admin_pw = ["123"]
seller_name = ["Garden"]
seller_pw = ["Garden123"]
customer_name = ["Tommy"]
customer_pw = ["5212023"]
permission_stat = 0 # 1:customer 2:Shopper 3:Admin
p_name = "" # the name of the user
flag_bit = True

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
        while current_pos >= start and raw_list[current_pos][index] < raw_list[current_pos-1][index] :
            raw_list[current_pos][index] , raw_list[current_pos-1][index] = raw_list[current_pos-1][index] ,  raw_list[current_pos][index]
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
    with open("D:\Python\Book1.csv","r", newline='', encoding='utf-8-sig') as goods_info :
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
        return True
    else :
        print("Please fill in S / C !")
        new_user()
            

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
    pw_double_check = str(input("Please input the password again ")) # data verificaton by entering the data twice
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
    global p_name
    login_name = str(input("Hi Customer , Your username is : "))
    if login_name in customer_name :
        location = find(customer_name,login_name)
        login_pw = str(input("Hi Customer , Your password is : "))
        if customer_name[location] == login_name and customer_pw[location] == login_pw : # check if the account matches with the password
            print("")
            print("Welcome Customer {} !".format(login_name))
            p_name = login_name
            return True
        else :
            print("Your password is NOT correct , please try again")
    else :
        print("Username does NOT exist , please try again")
    return False

# Main Menu
def menu() : # showing the commands available for different roles
    print("")
    for i in range(50) : print("*" , end="")
    print("\nWelcome to the Control Menu ,{}   Enjoy your time in our supermarket ! \n"
          "Here are the Commands for our online market : \n"
          "V - View the available goods in our market \n"
          "SN - Sort the goods by Name \n"
          "SP - Sort the goods by Price \n"
          "SID - Sort the goods by the ID\n"
          "S - Search for specific goods by name\n"
          "SWID - Search for specific goods with the goods ID\n"
          "F - Filter the goods with unwanted brand".format(p_name))
    if permission_stat == 3 : # admin can edit without limitation
        print("AE - Admin Editing the goods")
    elif permission_stat == 2 : # seller cannot use shopping cart but can change and add their goods
        print("M - Modify the status of goods by YOUR brand \n"
              "D - Delete the goods by YOUR brand")
    elif permission_stat == 1 : # customer can use shopping cart to buy goods
        print("VC - View your shopping Cart \n"
              "EC - Edit your shopping Cart"
              "CO - Check Out of your shopping cart")
    print("QUIT - Quit this application")   
 
def menu_control(access) :
    global flag_bit
    control = str(input("Your command is : "))

    if control in ["V","SN","SP","SID","S","SWID"] :
        sorting_show(control)

    elif control == "AE" :
        if access == 3 :
            pass
        else :
            print("ACCESS DENIED : Admin ONLY")
    elif control == "QUIT" :
        flag_bit = False


def view(data) :
    for i in range(58) : print("-" , end="")
    print("")
    for row in data :
        print('| {:>8} | {:>4} | {:>12} | {:>10} | {:>8} | '.format(row[0],row[1],row[2],row[3],row[4]))
    for i in range(58) : print("-" , end="")

# Main Loop
if __name__ == "__main__" :
    login()
    while flag_bit :
        menu()
        menu_control(permission_stat)

