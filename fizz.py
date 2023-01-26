
#!This function will take one number as a param
#!And will return as fizz or buzz or fizzbuzz along with the (num), so we know what num's result is printing
def number(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return num, "FizzBuzz"
    elif (num % 3 == 0):
        return num, "Fizz"  
    elif (num % 5 == 0):
        return num, "Buzz"   
    return num, "Not divisible by 3 and/or 5!"

print(number(15))

#!This for loop is calling the function and printing the result for every #s in this list
mylist = [77,6,10,15,22,33,44,55,99,100,123,456,77,88,66,11,333,999,1000]
for num in mylist:
    result = number(num)
    print(result)




