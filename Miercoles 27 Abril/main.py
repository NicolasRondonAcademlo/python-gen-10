# herencia
# Padre -> Hijo

class Vehicle:
    def __init__(self, color, brand, model, year):
        self.color = color
        self.brand = brand
        self.model = model
        self.year = year

    def print_data(self):
        print(f"{self.color} {self.brand} {self.model} {self.year}")


class Car(Vehicle):
    def __init__(self, color, brand, model, year,  doors:int = 4):
        Vehicle.__init__(self, color, brand, model, year)
        self.doors = doors


obj_1 = Car("Rojo", "Toyota", "Corolla", "2020")
print(obj_1.print_data())

# Crea, Instancia, Destruye

class Contact:
    all_contacts = [] # Se comparte en todos los
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
    

class Supplier(Contact):
    def __init__(self, name, email, phone):
        #Contact.__init__(self, name, email)
        super().__init__(name, email)
        self.phone = phone

    def order(self, order):
        print(f"If this were a real system we would send {order} to {self.name}")


c = Contact("Some body", "somebady@email.com")
s = Supplier("Supplier 1", "suplier1@email.com", "123456789")

print(c.name, c.email,)
print(s.name, s.email, s.phone)


class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

c1 = Contact("Some body", "somebady@email.com")
c1 = Contact("Some body", "somebady@email.com")
c3 = Contact("Felipe", "somebady@email.com")
lista_nombres = [c3.name for c in Contact.all_contacts.search("Felipe")]
print(lista_nombres)

