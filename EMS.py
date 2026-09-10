employees=[]

#To add Employee

def add_employee():
    emp_id=input("Enter Employee ID:")
    name=input("Enter Employee Name:")
    department=input("Enter department:")
    
    try:
        salary=float(input("Enter Salary:"))
    except ValueError:
        print("invalid salary.please enter a number.")
        return

    employee={
        "id":emp_id,
        "name":name,
        "department":department,
        "salary":salary
        }
    employees.append(employee)
    print("Employee added successfully!")


# To view the Employee

def view_employees():
    if not employees:
        print("No Employee Found.")
        return
    print("\n----Employee list---")

    for employee in employees:
        print("ID:", employee["id"])
        print("Name:",employee["name"])
        print("department:",employee["department"])
        print("salary:",employee["salary"])
        print("------------------------")

#To search Employee
        
def search_employee():
    emp_id=input("Enter Employee ID to search:")

    for employee in employees:
        if employee["id"]==emp_id:
            print("\n Employee Found!")
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            print("Department:", employee["department"])
            print("salary:", employee["salary"])
            return
        
        print("Employee not Found.")

#To Update employee

def update_employee():
    emp_id=input("Enter Employee ID to Update:")

    for employee in employees:
        if employee["id"]==emp_id:
            print("Leave blank if you don't want to change the field:")

            name=input("Enter New Name:")
            department=input("Enter new Department:")
            salary=input("Enter New salary:")
            if name:
                employee["name"]=name
            if department:
                employee["department"]=department
            if salary:
                employee["salary"]=salary
            print("Employee updated succesfully!")
            return
        
        print("Employee not found.")

# To delete Employee

def delete_employee():
    emp_id=input("Enter Employee ID to Delete:")

    for employee in employees:
        if employee["id"]==emp_id:
            employees.remove(employee)
            print("Employee Deleted successfully!")
            return
    print("Employee not Found.")

while True:
    print("\n====Employee Management System====")
    print("1.Add Employee")
    print("2.view Employees")
    print("3.Search Employee")
    print("4.Update Employee")
    print("5.Delete Employee")
    print("6.Exit")

    choice=input("Enter your Choice:")

    if choice=="1":
        add_employee()
        
    elif choice=="2":
        view_employees()

    elif choice=="3":
        search_employee()

    elif choice=="4":
        update_employee()

    elif choice=="5":
        delete_employee()

    elif choice=="6":
        print("thank you")
        break

    else:
        print("invalid choice. Please try again.")

    
            
                 

                 
                 
                
           



    



        


    
