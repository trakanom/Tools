print(*[["","Fizz"][i%3==0]+["","Buzz"][i%5==0]+["",str(i)][((i%5)*(i%3)>0)] for i in list(range(1,1+int(input())))], sep="\n")
