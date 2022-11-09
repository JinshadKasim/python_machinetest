class Employee:
    def __init__(self,name,age,empCode,gender,phoneNo):
        self.name = name
        self.age = age
        self.empCode = empCode
        self.gender = gender
        self.phoneNo = phoneNo

    def viewEmployee(self):
        print("Name :",self.name)
        print("age :",self.age)
        print("salary :",self.empCode)
        print("gender :",self.gender)
        print("special :",self.phoneNo)

    def get_age(self):
        print(self.age)
        print('Getter Method Called')

    def set_age(self,a):
        self.age = a
        print('Setter Method Called')

    def calculate_salary(self):
        salary = 50000 - (50000 * 5/100)
        print('Salary:',salary)

# ob = Employee('kasim',20 , 1234,'male', '122323434')

# ob.viewEmployee()
# ob.set_age(10)
# ob.viewEmployee()
# ob.get_age()

# ob.calculate_salary()


class Permanent_employee(Employee):
    def __init__(self,name, age, empCode, gender, phoneNo):
        Employee.__init__(self,name, age, empCode, gender, phoneNo)

    def calculate_salary(self,pf=0,gratuity=0):
        if pf > 0:
            emi = (50000 * 5/100)
            salary = 50000 - (50000 * 5/100) - pf
            print('PF:',pf)
            print('Gratuity:',gratuity)
            print('Insurance EMI:',emi)
            print('Salary:',salary)
        elif gratuity > 0:
            emi = (50000 * 5/100)
            salary = 50000 - (50000 * 5/100) - gratuity
            print('Gratuity:',gratuity)
            print('Insurance EMI:',emi)
            print('Salary:',salary)

        elif gratuity > 0 and pf > 0:
            emi = (50000 * 5/100)
            salary = 50000 - (50000 * 5/100) - gratuity - pf
            print('PF:',pf)
            print('Gratuity:',gratuity)
            print('Insurance EMI:',emi)
            print('Salary:',salary)
        
        else:
            emi = (50000 * 5/100)
            salary = 50000 - (50000 * 5/100)
            print('Insurance EMI:',emi)
            print('Salary:',salary)
        

    def get_salary(self):
        salary = 50000 - (50000 * 5/100)
        print('Salary:',salary)

    def set_salary(self,a):
        self.salary = a
        print('salary', self.salary)
        



class Contract_employee(Employee):
    def __init__(self,name, age, empCode, gender, phoneNo):
        Employee.__init__(self,name, age, empCode, gender, phoneNo)
   

    def calculate_salary(self,fine=0):
        if fine > 0:
            emi = (30000 * 8/100)
            salary = 30000 - (30000 * 8/100) 
            salary = salary - fine
            print('Fine:',fine)
            print('Insurance EMI:',emi)
            print('Salary:',salary)
        else:
            emi = (30000 * 8/100)
            salary = 30000 - (30000 * 8/100) 
            print('Insurance EMI:',emi)
            print('Salary:',salary)
        


    
    def get_salary(self):
        salary = 30000 - (30000 * 8/100)
        print('Salary:',salary)

    def set_salary(self,a):
        self.salary = a
        print('salary', self.salary)
        



    
pemp = Permanent_employee('John', 35, 1001, 'male', '12345')

pemp.calculate_salary()


# cemp = Contract_employee('Mary', 24, 1002, 'Female', '456789')

# cemp.calculate_salary()