import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	# YOUR CODE HERE
    chamber_position = spin_chamber()
    if chamber_position==bullet_position:
        print("You are dead!")
    else:
        print("Keep playing!")
    return None


print(fire_gun())