for i in range(1,n+1):
    if i%15==0:
        print("FizzBuzz")
    else:
        if i%3*i%5==0:
            if i%5==0:
                print("Buzz")
            else:
                print("Fizz")
        else:
            print(i)
