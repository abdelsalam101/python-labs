from employee import Employee, Manager

def menu():
    while True:
        print("\n=== Employee Management Menu ===")
        print("add - Add new employee or manager")
        print("fire - Fire an employee")
        print("transfer - Transfer employee")
        print("show - Show employee")
        print("list - List all employees")
        print("q - Quit")

        choice = input("Enter command: ").lower()
        if choice == "add":
            role = input("m for Manager, e for Employee: ").lower()
            fname = input("First Name: ")
            lname = input("Last Name: ")
            age = int(input("Age: "))
            dept = input("Department: ")
            salary = float(input("Salary: "))
            if role == "m":
                managed_dept = input("Managed Department: ")
                Manager(fname, lname, age, dept, salary, managed_dept)
            else:
                Employee(fname, lname, age, dept, salary)
        
        elif choice == "fire":
            fname = input("First Name: ")
            lname = input("Last Name: ")
            for emp in Employee.all_employees:
                if emp.first_name == fname and emp.last_name == lname:
                    emp.fire()
                    print("Fired.")
                    break
        elif choice == "transfer":
            fname = input("First Name: ")
            lname = input("Last Name: ")
            new_dept = input("New Department: ")
            for emp in Employee.all_employees:
                if emp.first_name == fname and emp.last_name == lname:
                    emp.transfer(new_dept)
                    print("Transferred.")
                    break

        elif choice == "show":
            fname = input("First Name: ")
            lname = input("Last Name: ")
            for emp in Employee.all_employees:
                if emp.first_name == fname and emp.last_name == lname:
                    emp.show()
                    break

        elif choice == "list":
            Employee.list_employees()

        elif choice == "q":
            print("Goodbye!")
            break

        else:
            print("Invalid command.")

if __name__ == "__main__":
    menu()