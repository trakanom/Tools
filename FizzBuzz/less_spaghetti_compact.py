print(*[[[str(i),["Fizz","Buzz"][i%5==0]][i%3*i%5==0],"FizzBuzz"][i%15==0] for i in list(range(1,1+int(input())))], sep="\n")
