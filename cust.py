class Customer:
    def __init__(self,name,place,phone,email):
        self.name = name
        self.place = place
        self.phone = phone
        self.email = email

    def get_details(self):
        print('Name',self.name)
        print('Place',self.place)
        print('Phone',self.phone)
        print('Email',self.email)

    def set_email(self,emaill):
        self.email = emaill
        print(self.email)

        
cust1 = Customer('Ram', 'Calicut', '12345678', 'ram@gmail.com')

cust1.set_email('hjg')
cust1.get_details()