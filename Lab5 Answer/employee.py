from database import get_db_connection as get_connection

class Employee:
    
    all_employees = []
    def __init__(self, first_name, last_name, age, department, salary):
     self.first_name = first_name
     self.last_name = last_name
     self.age = age
     self.department = department
     self.salary = salary
     
     Employee.all_employees.append(self)
     self.insert_into_db()

    def insert_into_db(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO employee (first_name, last_name, age, department, 
            salary) VALUES (%s, %s, %s, %s, %s)
        """, (self.first_name, self.last_name, self.age, self.department, self.salary))
        conn.commit()
        cur.close()
        conn.close()
        
    def transfer(self, new_department):
            self.department = new_department
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                UPDATE employee SET department = %s WHERE id = %s
            """, (new_department, self.id,))
            conn.commit()
            cur.close()
    def fire(self):
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                DELETE FROM employee WHERE id = %s
            """, (self.id))
            conn.commit()
            cur.close()
            conn.close()
    def show(self):
            print(f"{self.first_name} {self.last_name}, Age: {self.age}, Dept: {self.department}, Salary: {self.salary}")
        
    @staticmethod
    def list_employees():
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
            SELECT first_name, last_name, age, department, salary FROM employee
            WHERE is_manager = FALSE
            """)
            for row in cur.fetchall():
                print(f"{row[0]} {row[1]}, Age: {row[2]}, Dept: {row[3]}, Salary: {row[4]}")
            cur.close()
            conn.close()
            
class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department = managed_department
        self.update_to_manager()
    
    def update_to_manager(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            UPDATE employee SET is_manager = TRUE, managed_department = %s
            WHERE first_name = %s AND last_name = %s
            """, (self.managed_department, self.first_name, self.last_name))
        conn.commit()
        cur.close()
        conn.close()

    def show(self):
        print(f"{self.first_name} {self.last_name}, Age: {self.age}, Dept: {self.department}, Salary: confidential, Manages: {self.managed_department}")