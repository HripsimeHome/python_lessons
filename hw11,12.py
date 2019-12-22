# 1. Create a class for representing book with some attributes (author, owner, pages, price, current page)
# and behavior (change owner, increase price, change current page), create several books and perform operations on them

class Book:
    def __init__(self, b_author, b_owner, b_pages, b_price, b_current_page):
        self.author = b_author
        self.owner = b_owner
        self.pages = b_pages
        self.price = b_price
        self.current_page = b_current_page

book1 = Book("Author1", "Owner1", 180, 1000, 5)
book2 = Book("Author2", "Owner2", 210, 2000, 15)
book3 = Book("Author3", "Owner3", 320, 3000, 35)

print(book1.author)
print(book2.owner)
print(book3.price)


# 2. Create a class for representing shop with some attributes (employees names, products names and prices, income, owner)
# and behavior (add employee, remove employee, add products, find product by name,
# find products cheaper than some specific value, change owner, increase income), create several shops and perform operations on them

class Shop:
    def __init__(self, employee_name, product_name, product_price, shop_income, shop_owner):
        self.emp_name = employee_name
        self.prod_name = product_name
        self.prod_price = product_price
        self.income = shop_income
        self.owner = shop_owner

# find product by name
    def find_product(self):
        if self.prod_name == "Shirt":
            print("This product name is " + self.prod_name)
        else:
            print("There is no such as product.")

#find products cheaper than some specific value
    def cheaper_product(self, value):
        self.value = value
        for price in self.prod_price:
            if price < 50:
                print("There is cheaper product")
            else:
                print("There is no cheaper product.")

shop1 = Shop("Melissa", "Dress", 100, 80, "David")
shop2 = Shop("Sam", "Shirt", 50, 30, "Bob")
shop3 = Shop("Andrew", "Shoes", 150, 10, "Brandon")

shop2.find_product()
#shop3.cheaper_product()
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
# check how many movies are created
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
movie3.rating = 5
print(movie3.rating)


# 10. Create class Person with attributes (name, height that should be more than 30, sex that should be male or female)
# and some behavior, control the values, create objects and use them

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