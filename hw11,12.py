# 1. Create a class for representing book with some attributes (author, owner, pages, price, current page)
# and behavior (change owner, increase price, change current page), create several books and perform operations on them

class Book:
    def __init__(self, b_author, b_owner, b_pages, b_price, b_current_page):
        self.author = b_author
        self.owner = b_owner
        self.pages = b_pages
        self.price = b_price
        self.current_page = b_current_page
    # def increase_price(self, _price):
    #     self.price = 15

    # def change_owner(self, owner_name):
    #     self.owner = owner_name



book1 = Book("Author1", "Owner1", 180, 1000, 5)
book2 = Book("Author2", "Owner2", 210, 2000, 15)
book3 = Book("Author3", "Owner3", 320, 3000, 35)

print(book3.author)
print(book3.price)


# 2. *Create a class for representing shop with some attributes (employees names, products names and prices, income, owner)
# and behavior (add employee, remove employee, add products, find product by name,
# find products cheaper than some specific value, change owner, increase income), create several shops and perform operations on them


class Shop:
    def __init__(self, employee_name, product_name, product_price, shop_income, shop_owner):
        self.emp_name = employee_name
        self.prod_name = product_name
        self.prod_price = product_price
        self.income = shop_income
        self.owner = shop_owner


# add employee ???????????
    def add_employee(self, value):
        self.add_emp = value
        self.emp_name.append(self.add_emp)


# remove employee ???????????
    def remove_employee(self):
        del shop2.emp_name


# add products ???????????

    def add_product(self, value):
        self.add_prod = value
        self.prod_name.append(self.add_prod)


# find product by name
    def find_product(self):
        if self.prod_name == "Shirt":
            print("This product name is " + self.prod_name)
        else:
            print("There is no such as product.")

#find products cheaper than some specific value - ???????????
    def cheaper_product(self, value):
        self.value = value
        for price in self.prod_price:
            if price < 50:
                print("Cheaper product price is", prod_price)
            else:
                print("There is no cheaper product.")


# change owner ???????????
    def change_owner(self, value):
        self.value = value


# increase income???????????
    def increase_income(self):
        self.income += 2


shop1 = Shop("Melissa", "Dress", 100, 80, "David")
shop2 = Shop("Sam", "Shirt", 50, 30, "Bob")
shop3 = Shop("Andrew", "Shoes", 150, 10, "Brandon")

shop1.add_employee("Sarah")
shop2.remove_employee()
shop3.add_product()
shop2.find_product()
shop2.cheaper_product()
shop1.change_owner()
shop3.increase_income()
print(shop2.owner)






# 5. Create a class for representing a movie with some attributes (title, director, duration, actors, rating)
# and behavior (find if movie director name starts with specific symbol, find if some person is an actor, change rating),
# create several movies and perform operations on them, check how many movies are created

class Movie:
    counter = 0
    def __init__(self, title, director, duration, actors, rating):
        self.title = title
        self.director = director
        self.duration = duration
        self.actors = actors
        self.rating = rating
        Movie.counter += 1

# find if movie director name starts with specific symbol
    def check_director(self):
        if self.director.startswith('M'):
            print("There is name starts with \"M\".")
        else:
            print("There is no no name starts with \"M\".")

#find if some person is an actor
    def check_actor(self):
        if self.actors == "Robert":
            print("Yes, there is Robert.")
        else:
            print("No, there is no Robert.")

#create several movies and perform operations on them, check how many movies are created

movie1 = Movie("The first", "Miller", 2, "Kevin", 5)
movie2 = Movie("The second", "Brown.", 1, "Robert", 4)
movie3 = Movie("The third", "Wilson", 3, "Jessica", 3)
print("There are ", Movie.counter, "movies.")

movie1.check_director()
movie2.check_actor()

#change rating
movie3.rating = 5
print(movie3.rating)





# 10. Create class Person with attributes (name, height that should be more than 30, sex that should be male or female)
# and some behavior, control the values, create objects and use them

# NExt presentation ?????????????????????????????????????????????????????????????????????
class Person:
    def __init__(self, name, height, sex):
        self.name = name
        self.height = height
        self.sex = sex
    def speak(self):
        print("Hello" + " " + self.name + "!")

person1 = Person("Sam", 180, "male")
person2 = Person("Melissa", 167, "female")
person3 = Person("Kevin", 175, "male")
person4 = Person("Anna", 165, "female")

print(person1.name)
print(person2.height)
print(person3.sex)
person4.speak()