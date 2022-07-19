import csv
import getpass

def is_in_my_db(column,text): # cheack if the text is in the coulmn 
    is_in = False
    with open("DB.csv", "r") as f:
        my_db = csv.reader(f)
        for row in my_db:
            if (row[column] == text):
                is_in = True
    return is_in  
def log_in():# log in to a user and return a list of the user
     with open("DB.csv", "r") as f:
            my_db = csv.reader(f)           
            while True:
                user_name = input("Enter your user name: ")
                password = getpass.getpass(prompt = "Enter yout password: ")
                print("") 
                f.seek(0)
                next(f)      
                for row in my_db:
                    if row[0] == user_name and row[1] == password:
                        return row
                print("Uncorrect user name or password, try again") 
def is_only_numbers(text):# cheack if the text contain only numbers
    try:
        x = float(text)
        return True
    except:
        return False 
def is_fine_parameteres(user, password, balance, role): # cheack if all paramters is valid
    is_fine = True
    if is_in_my_db(0, user):
        is_fine = False
        print("This user name is taken")
    if is_in_my_db(1, password):
        is_fine = False
        print("This password is taken")
    if not is_only_numbers(balance):
        is_fine = False
        print("balance must contain only numbers")
    if not (role == "simple" or role == "manager"):
        is_fine = False
        print("role must to be manager or simple")
    return is_fine
def remove_user(user): # remove user 
    is_removed = True
    if  is_in_my_db(0, user):
        with open("DB.csv", "r") as rf:
            lines = rf.readlines()
        with open("DB.csv", "w") as wf: 
            for line in lines:
                if not user == line[:len(user)]:
                    wf.write(line)  
    else: 
        print("this user does'nt exist, try again") 
        is_removed = False
    return is_removed 
def create_user():  # create user
    user = input("Enter the user name: ")
    password = input("Enter the user password: ")
    balance = input("Enter the user balance(only numbers): ")
    role = input("Enter the user role(manager or simple): ")
    if is_fine_parameteres(user, password, balance, role):
        with open("DB.csv", "a") as af: 
            af.write("{},{},{},{}\n".format(user, password, float(balance), role)) 
    else:
        print("worng parameters, try again")
def basic_actions(action, list): # actions 1-3
    if action == '1':  
        print("Your balance is: " + list[2])
    
    elif action == '2': 
        amount = input("Enter the withdraw sum: ")
        if is_only_numbers(amount):
            list[2] = str(float(list[2]) - float(amount))
            print('The operation was performed')
        else:
            print("Your withdraw sum is illegal, try again")        
    
    elif  action == '3': 
        amount = input("Enter the deposite sum: ")
        if is_only_numbers(amount):
            list[2] = str(float(list[2]) + float(amount))
            print('The operation was performed')
        else:
             print("Your withdraw sum is illegal, try again")
def simple_operation(list):  # the simple user menu
    action = input("Enter the num of your operation: \n1.check your balance\
                     \n2.withdraw money \n3.Deposit money\n")    
    if int(action) > 0 and int(action) < 4:
        basic_actions(action,list)
    else:         
        print("anvalid operation")

    a = input("For another operation press 1, else for exit ")
    if a =='1':
        return(simple_operation(list))
    else :
        return list 
def manager_operation(list):# the manager user menu
    action = input("Enter the num of your operation: \n1.check your balance \
                   \n2.withdraw money \n3.Deposit money\n4.create new user \
                   \n5.delete user\n6.edit a user\n7.change the role of a user\n")

    if int(action) > 0 and int(action) < 4:
            basic_actions(action, list)
    if  action == '4': #create new user        
        create_user()    
    elif  action == '5': #delete user 
        user = input("Enter the user name to remove: ")
        remove_user(user)
  
    elif  action == '6': #edit a user        
        prev_user = input("Enter the user name which you want to edit: ")
        if remove_user(prev_user):       
            create_user() 
      
    elif  action == '7': #change the role of a user
        user = input("Enter the user name to change his role: ")       
        if is_in_my_db(0,user):
            with open("DB.csv", "r") as f:
                lines = f.readlines()
                f.seek(0)
                my_db = csv.reader(f)
                for row in my_db:
                    if row[0] == user:
                        user_list = row               
              
            if user_list[3] == "simple":
               user_list[3] = "manager"
            else:
               user_list[3] = "simple"

            remove_user(user_list[0])
            with open("DB.csv", "a") as af:               
                af.write("{},{},{},{}\n".format(user_list[0],user_list[1],\
                        user_list[2], user_list[3])) 
        else:
            print("user is'nt exist, try again")
    else:
        print("anvalid operation")

    print("")
    a = input("For another operation press 1, else for exit ")
    if a =='1':
        return(manager_operation(list))
    else :
        return list
def main():
    the_account =  log_in()
    if the_account[3] == 'simple':
        update_account = simple_operation(the_account)    
        remove_user(the_account[0])
        with open("DB.csv", "a") as af:
            af.write("{},{},{},{}\n".format(update_account[0],update_account[1],\
                         update_account[2], update_account[3]))
  
    if the_account[3] == 'manager':
        update_account = manager_operation(the_account)     
        remove_user(the_account[0])
        with open("DB.csv", "a") as af:
            af.write("{},{},{},{}\n".format(update_account[0],update_account[1],\
                         update_account[2], update_account[3]))
  
main()