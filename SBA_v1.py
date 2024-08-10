# Module import
import csv
import re

# Global variable
admin_name = ["admin"]
admin_pw = ["123"]
seller_name = ["Garden"]
seller_pw = ["Garden123"]
customer_name = ["Tommy"]
customer_pw = ["fivetwone2023"]


# def 
def binary_search(matrix,target) :
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
def find(matrix,target) :
    for pos , item in enumerate(matrix) :
        if item == target :
            return pos
    return False

def new_user() :
    new_role = str(input("Register : S-Seller / C-Customer : "))
    if new_role == "S" :
        new_name = str(input("Your name is : "))
        if new_name not in seller_name :
            seller_name.append(new_name)
        else :
            print("Your name has been used , try again !")
            return False
        new_pw = str(input("Your password is : "))
        while pw_check(new_pw) is False :
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
    return True

def login() :
    permission_stat = 0 # 1:customer 2:Shopper 3:Admin
    role = str(input("You are : A-Admin / S-Seller / C-Customer ( Please fill in short form ,type NEW to make a new account ) : "))
    if role == "A" :
        while admin_login() == False :
            pass
    elif role == "S" :
        while seller_login() == False :
            pass
    elif role == "C" :
        while customer_login() == False :
            pass
    elif role == "NEW" :
        while new_user() == False :
            pass
        login()
    else :
        print("Please fill in valid short form (A/S/C/NEW) ! ")
        login()

def admin_login() :
    login_name = str(input("Hi Admin , Your username is : "))
    if login_name in admin_name :
        location = find(admin_name,login_name)
        login_pw = str(input("Hi Admin , Your password is : "))
        if admin_name[location] == login_name and admin_pw[location] == login_pw :
            print("Welcome Admin {} !".format(login_name))
            return True
        else :
            print("Your password is NOT correct , please try again")
    else :
        print("Username does NOT exist , please try again")
    return False

def seller_login() :
    login_name = str(input("Hi Seller , Your username is : "))
    if login_name in seller_name :
        location = find(seller_name,login_name)
        login_pw = str(input("Hi Seller , Your password is : "))
        if seller_name[location] == login_name and seller_pw[location] == login_pw :
            print("Welcome Seller {} !".format(login_name))
            return True
        else :
            print("Your password is NOT correct , please try again")
    else :
        print("Username does NOT exist , please try again")
    return False

def customer_login() :
    login_name = str(input("Hi Customer , Your username is : "))
    if login_name in customer_name :
        location = find(customer_name,login_name)
        login_pw = str(input("Hi Customer , Your password is : "))
        if customer_name[location] == login_name and customer_pw[location] == login_pw :
            print("Welcome Customer {} !".format(login_name))
            return True
        else :
            print("Your password is NOT correct , please try again")
    else :
        print("Username does NOT exist , please try again")
    return False

# Main Loop

login()

#with open("D:\Python\Book1.csv","r+", newline='') as goods_info :
#    goods = csv.reader(goods_info, delimiter=' ', quotechar='|')
#    for row in goods :
#        print(''.join(row))
#        #print(row)