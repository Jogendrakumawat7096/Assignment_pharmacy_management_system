import mysql.connector
import datetime

def create_conn(): #create connection with mysql
    return mysql.connector.connect(
        host ="localhost",
        username ="root",
        password= "",
        database= "pharmacy_system"
    )


#Class For Admin Role
class Admin:
    def __init__(self,username,password,name,mobile):
        self.username= username
        self.password= password
        self.name= name
        self.mobile= mobile
    #Function For Register Admin  
    def admin_register(self):
        conn = create_conn()
        cursor = conn.cursor()
        query = "insert into adminregister(username,pass,name,mobile) values(%s,%s,%s,%s)"
        args = (self.username, self.password, self.name, self.mobile)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        print("Admin Register Successfully")
    
    #Function For Login Admin
    def LoginAdmin(self):
        conn = create_conn()
        cursor = conn.cursor()
        query = "select * from adminregister where username=%s"
        args = (self.username,)
        cursor.execute(query,args)
        row = cursor.fetchone()
        return row
     
    #View All Manager        
    def view_all_manager(self):
        conn = create_conn()
        cursor = conn.cursor()
        query = "select * from manager"
        cursor.execute(query)
        rows = cursor.fetchall()
        
        for row in rows:
            print(f"SR.No :{row[0]},Username: {row[1]}, Name: {row[3]}, PharmacyName: {row[4]}")
        
        conn.close()        
    
    #View All Medicine
    def view_all_medicine(self):
        conn = create_conn()
        cursor = conn.cursor()
        query = "select * from medicine"
        cursor.execute(query)
        rows = cursor.fetchall()
        
        for row in rows:
            if not row:
                print("No Medicine Available")
                
            else:     
                print(f"(SR.No :{row[0]},Medicine Name: {row[1]},Qty : {row[2]},Added Date : {row[3]},Added BY : {row[4]},Price : {row[5]})\n")

       
        
#Class For Manager
class Manager():
    
    def __init__(self):
        pass

    #manager Register Function   
    def manager_register(self,username,password,name,pharmacy):
        conn = create_conn()
        cursor = conn.cursor()
        query = "insert into manager(username,pass,Manager_name,Pharmacy_name) values(%s,%s,%s,%s)"
        args = (username, password, name, pharmacy)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        print("Manager Register Successfully")
    
    #login manager
    def manager_login(self,username):
        conn = create_conn()
        cursor = conn.cursor()
        query = "select * from manager where username=%s"
        args = (username,)
        cursor.execute(query,args)
        row = cursor.fetchone()
        return row
     
    #Add Medicine
    def add_medicine(self, SR_number, medicine_name, qty, Added_date, Added_by ,price):
        conn = create_conn()
        cursor = conn.cursor()
        query = "insert into medicine(SR_No, Medicine_Name, Qty, Added_Date, Added_By, price) values(%s,%s,%s,%s,%s,%s)"
        args = (SR_number, medicine_name, qty, Added_date, Added_by, price)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        print("Add Medicine Successfully")
   
    #View medicine              
    def view_medicine(self,medicine_srno):
        conn = create_conn()
        cursor = conn.cursor()
        query = "select * from medicine where SR_No=%s"
        args = (medicine_srno,)
        cursor.execute(query,args)
        rows = cursor.fetchall()
        
        for row in rows:
            if not row:
                print("No Medicine Available")
                
            else:     
                print(f"(SR.No :{row[0]},Medicine Name: {row[1]},Qty : {row[2]},Added Date : {row[3]},Added BY : {row[4]},Price : {row[5]})\n")
        
        conn.close()
    
    #Delete medicine    
    def delete_medicine(self,medicine_srno):
        conn = create_conn()
        cursor = conn.cursor()
        query = "DELETE FROM `medicine` WHERE SR_No=%s"
        args = (medicine_srno,)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        

while True:
    print(" "*20,"WELCOME PHARMACY MANAGEMENT SYSTEM")
    print("")
    print(" "*30,"1) Admin")
    print(" "*30,"2) Pharmacy Manager")
    print(" "*30,"3) Exit")
    
    Role = input("Enter Your Role : ") #Select Role
    try:
        Role = int(Role)
    except ValueError:
        print("Error Caught : Enter Role As A  Numberical Value ")

#Admin Role 
    if Role == 1:
        while True:
            print("")
            print(" "*30,"Welcome Admin Page")
            print("")
            print(" "*30,"1) Register")
            print(" "*30,"2) Login")
            print(" "*30,"3) Exit Admin Page")
            
            choice= input("Enter Your Choice : ")
            try:
                choice = int(choice)
            except ValueError:
                    print("Error Caught : Enter choice As A  Numberical Value ")
            
            #Admin Register
            if choice==1:
                print(" "*30,"Admin Register Page")
                user_name= input("Enter User Name : ")
                conn = create_conn()
                cursor = conn.cursor()
                query = "select * from adminregister where username=%s"
                args = (user_name,)
                cursor.execute(query,args)
                row = cursor.fetchone()
                
                if row is None or user_name!=row[1]:
                    user_pass =input("Enter Your Password : ")
                    name=input("Enter Your Name : ") 
                    mobile = input("Enter Mobile Number : ")
                    register=Admin(user_name,user_pass,name,mobile)
                    register.admin_register()                  

                    
                else:
                    print("User Name Already Exist")
                    continue
            
            #Admin Login
            elif choice==2:
                while True:
                    print(" "*30,"Admin Login Page")
                    user_name= input("Enter User Name : ")
                    user_pass=input("Enter Password : ")

                    loginadmin=Admin(user_name,user_pass,None,None)
                    row=loginadmin.LoginAdmin()

                    
                    if row is None or (user_name!=row[1] and user_pass!=row[2]):
                        print("Enter Correct Username And Password")
                        continue
                    
                    else:
                        print("")
                        print("Admin Login Successfully")
                        print("")
                        while True:
                            print(" "*30,"1) View All Manager")
                            print(" "*30,"2) View All Medicine")
                            print(" "*30,"3) Back Admin Main Page")
                            
                            choice = input("Enter Your Choice : ")
                            
                            try:
                                choice = int(choice)
                            except ValueError:
                                    print("Error Caught : Enter choice As A  Numberical Value ")                       
                            
                            
                            #View All Managers
                            if choice ==1:
                                viewmanager = Admin(None,None,None,None)
                                viewmanager.view_all_manager()
                            
                            #view All Medicines  
                            elif choice ==2:
                                viewmanager = Admin(None,None,None,None)
                                viewmanager.view_all_medicine()                         
                            
                            elif choice==3:
                                break
                                
                            else:
                                print("Enter Correct Choice ")
                                continue
                              
                            
                            perform = input('Do you want to perform more operations Press "y" for yes or "n" for no: ')
                            if perform.lower()!= 'y':
                                break 
                        break   
                            
            elif choice==3:
                break        
            else:
                print("Enter Correct Choice")
                continue
            
            perform = input('Go Back Admin Page press "y" for yes or "n" for no: ')
            if perform.lower()!= 'y':
                break 
        
#Manager Role    
    elif Role==2:
          
        while True:
            print("")
            print(" "*30,"Welcome manager Page")
            print("")
            print(" "*30,"1) Register")
            print(" "*30,"2) Login")
            print(" "*30,"3) Exit Manager page")
            
            choice= input("Enter Your Choice : ")
            try:
                choice = int(choice)
            except ValueError:
                    print("Error Caught : Enter choice As A  Numberical Value ")
            
            
            #Manager Register
            if choice==1:
                print(" "*30,"Manager Register page")
                user_name= input("Enter User Name : ")
                conn = create_conn()
                cursor = conn.cursor()
                query = "select * from manager where username=%s"
                args = (user_name,)
                cursor.execute(query,args)
                row = cursor.fetchone()
                
                if row is None or user_name!=row[1]:
                    user_pass =input("Enter Your Password : ")
                    manager_name=input("Enter Your Manager Name : ") 
                    pharmacy = input("Enter Pharmacy Name : ")
                    register=Manager()
                    register.manager_register(user_name,user_pass,manager_name,pharmacy)
                    
                 

                    
                else:
                    print("User Name Already Exist") #when Name Already Exist in database the show error
                    continue
                
            #Manager Login       
            elif choice==2:
                print(" "*30,"Manager Login page")            
                user_name= input("Enter User Name : ")
                user_pass=input("Enter Password : ")

                login=Manager()
                row=login.manager_login(user_name)

                
                if row is None or (user_name!=row[1] and user_pass!=row[2]):
                    print("Enter Correct Username And Password")
                    continue
                else:
                    print("")
                    print("Manager Login Successfully")
                    
                    while True:

                        print("")
                        print(" "*30,"1) Add Medicine")
                        print(" "*30,"2) View Medicine")
                        print(" "*30,"3) Delete Medicine")
                        print(" "*30,"4) Back Manager Main Page")
                        
                        
                        #Select Choice for  Perform By manager
                        choice = input("Enter Your Choice : ")
                        try:
                            choice = int(choice)
                        except ValueError:
                                print("Error Caught : Enter choice As A  Numberical Value ")
                        
                        
                        # Add Medicine
                        if choice ==1:
                            
                            SR_number= input("Enter Medicine SR Number : ")
                            conn = create_conn()
                            cursor = conn.cursor()
                            query = "select * from medicine where SR_No=%s"
                            args = (SR_number,)
                            cursor.execute(query,args)
                            row = cursor.fetchone()

                            if row is None or SR_number!=row[0]:
                                medicine_name=input("Enter Medicine Name : ") 
                                qty = input("Enter medicine QTY : ")
                                try:
                                    qty = int(qty)
                                except ValueError:
                                    print("Error Caught : Enter qty As A  Numerical Value ")
                                    continue

                                Added_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")                               
                                Added_by = input("Enter Added By : ")
                                price = input("Enter Medicine Price : ")
                                try:
                                    price = float(price)
                                except ValueError:
                                    print("Error Caught : Enter qty As A  Numerical Value ")
                                    continue

                                medicine=Manager()
                                medicine.add_medicine(SR_number,medicine_name,qty,Added_date,Added_by,price)               

                            else:
                                print("SR Number Already Exist") #when Sr No Already Exist in database then show error
                                continue

                        
                        #View Medicine   
                        elif choice ==2:
                            
                            medicine_srno=input("Enter Medicine SR Number : ")
                            
                            
                            if medicine_srno==" ":
                                print("Please Enter Sr No")
                            else:
                                conn = create_conn()
                                cursor = conn.cursor()
                                query = "select * from medicine where SR_No=%s"
                                args = (medicine_srno,)
                                cursor.execute(query,args)
                                row = cursor.fetchone()
                                
                                if row is None or medicine_srno!=row[0]:
                                    print("Enter Correct Sr Number") #when Name Already Exist in database the show error                                  
                                    continue
                                else:
                                    
                                    viewmedicine = Manager()
                                    viewmedicine.view_medicine(medicine_srno) 

                        
                        #Delete Medicine   
                        elif choice ==3:
                            medicine_srno=input("Enter Medicine SR Number : ")
                            
                            if medicine_srno==" ":
                                print("Please Enter Sr No")
                            else:
                                deletemedicine = Manager()
                                deletemedicine.delete_medicine(medicine_srno)
                                print("Delete medicine Successfully")
                            
                        else:
                            print("Enter Correct Choice ")
                            continue
                    
                        perform = input('Do you want to perform more operations Press "y" for yes or "n" for no: ')
                        if perform.lower()!= 'y':
                            break  
                            
            elif choice==3:
                break    
            else:
                print("Enter Correct Choice")
                continue
            
            perform = input('Go Back Manager Page press "y" for yes or "n" for no: ')
            if perform.lower()!= 'y':
                break          
    
    elif Role==3:
        break
    else:
        print("Enter Correct Role")
        continue

