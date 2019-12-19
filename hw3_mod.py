from hw3 import *

room_color = "Grey"
print(room_color)

flat_square = room_square + balcony_square
print("The general square is", flat_square)

print("Room number", room_number, "- is free.") if room_number == 15 else print("This is not free room.")