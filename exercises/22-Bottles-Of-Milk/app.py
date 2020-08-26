def number_of_bottles():
    lyrics=""
    for i in range(99,1,-1):
        num1=i-1
        num1=str(num1)
        num=str(i)
        lyrics= lyrics + (num + " bottles of milk on the wall, " + num + " bottles of milk. Take one down and pass it around, "+num1+" bottles of milk on the wall.")
    lyrics= lyrics + "1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall."
    print(lyrics)
number_of_bottles()