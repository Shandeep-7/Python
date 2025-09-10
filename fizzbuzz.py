#Game : FizzBuzz
for i in range(1,101,1):
    if(i%5==0 and i%3==0):
        print(i,"fizzbuzz")
    elif(i%5==0):
        print(i,"fizz")
    elif(i%3==0):
        print(i,"buzz")