# 5. Create a class for representing a movie with some attributes (title, director, duration, actors, rating)
# and behavior (find if movie director name starts with specific symbol, find if some person is an actor, change rating),
# create several movies and perform operations on them, check how many movies are created

class Movie:
    counter = 0
    def __init__(self, title, director, duration, actor, rating):
        self.title = title
        self.director = director
        self.duration = duration
        self.actor = actor
        self.rating = rating
        Movie.counter += 1
    def check_rating(self):
         if self.rating == 5:
             print("yes")
    def movie_director(self):
        if self.director.startswith('M'):
            print("His name starts with \"M\".")



movie1 = Movie("The first", "Miller", 2, "Kevin", 5)
movie2 = Movie("The second", "Brown.", 1, "Robert", 4)
movie3 = Movie("The third", "Wilson", 3, "Jessica", 3)

movie1.check_rating()
movie1.movie_director()

print("There are ", Movie.counter, "movies.")



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

person1 = Person("Robert", 180, "male")
person2 = Person("Melissa", 167, "female")
person3 = Person("Kevin", 175, "male")
person4 = Person("Anna", 165, "female")

print(person1.name)
print(person2.height)
print(person3.sex)
person4.speak()