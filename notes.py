# bring in block of code using an import. random is a module that contains a plethora of functions you can use.
import random

print(random.randint(1, 50))


danielle_age = input("How old are you? ")
danielle_age = int(danielle_age)
helen_age = 34


# Boolean has two states, true and false.
# do_i_like_bikes = True

print(danielle_age > helen_age)

if danielle_age > helen_age:
    print("you are older than helen")
elif danielle_age == helen_age:
    print("we're the same age!")
else:
    print("you are NOT older than helen")
