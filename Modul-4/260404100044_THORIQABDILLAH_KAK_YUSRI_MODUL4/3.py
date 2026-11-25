n = 100 #batas angka 
a, b = 0, 1

print("Bilangan Fibonacci hingga", n) 
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
