# Module import
import csv
import re

# Global variable
admin_name = ["admin"]
admin_pw = ["123"]
shopper_name = ["Garden"]
shopper_pw = ["Garden123"]
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

def login() :
    permission_stat = 0 # 1:customer 2:Shopper 3:Admin
    role = str(input("You are : A-Admin / S-Shopper / C-Customer ( Please fill in short form ,type NEW to make a new account ) : "))
    while role != "A" and role !="S" and role !="C" and role !="NEW":
        if role == "A" :
            while admin_login() == False :
                pass
        elif role == "S" :
            while shopper_login() == False :
                pass
        elif role == "C" :
            while customer_login() == False :
                pass
        elif role == "NEW" :
            
        else :
            print("Please fill in valid short form (A/S/C/NEW) ! ")
            role = str(input("You are : A-Admin / S-Shopper / C-Customer ( Please fill in short form ,type NEW to make a new account ) : "))

def admin_login() :
    login_name = str(input("Hi Admin , Your username is : "))
    if login_name in admin_name :
        location = binary_search(admin_name,login_name)
        if admin_name[location] == admin_pw[location] :
            name = login_name
            print("Welcome Admin {} !".format(name))
            return True
        else :
            print("Your password is NOT correct , please try again")
    else :
        print("Username does NOT exist , please try again")
    return False

def shopper_login() :
    login_name = str(input("Hi Shopper , Your username is : "))
    if login_name in shopper_name :
        location = binary_search(shopper_name,login_name)
        if shopper_name[location] == shopper_pw[location] :
            name = login_name
            print("Welcome Shopper {} !".format(name))
            return True
        else :
            print("Your password is NOT correct , please try again")
    else :
        print("Username does NOT exist , please try again")
    return False

def customer_login() :
    login_name = str(input("Hi Customer , Your username is : "))
    if login_name in customer_name :
        location = binary_search(customer_name,login_name)
        if customer_name[location] == customer_pw[location] :
            name = login_name
            print("Welcome Customer {} !".format(name))
            return True
        else :
            print("Your password is NOT correct , please try again")
    else :
        print("Username does NOT exist , please try again")
    return False

# Main Loop



with open("D:\Python\Book1.csv","r+", newline='') as goods_info :
    goods = csv.reader(goods_info, delimiter=' ', quotechar='|')
    for row in goods :
        print(''.join(row))
        #print(row)