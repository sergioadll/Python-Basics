def fizz_buzz():
    # your code here
    for i in range(1,101):
        num=i
        if num %3 ==0 and num %5==0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizz_buzz()