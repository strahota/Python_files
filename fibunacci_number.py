def fibonaci():
    x = 0
    y = 1
    result = 0
    count = 0
    print(x)
    while y < 128:
        count += 1
        x = y
        y = result
        result = x + y
        print(result)

fibonaci()

######################################

n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum)
  count += 1
  a = b
  b = sum
  sum = a + b
