
x = int(input('Введіть число:'))

x_1 = int(x/1000)

x_2 = int(x/100)%10

x_3 = int(x/10)%10

x_4 =int(x%10)

print(x_1)
print(x_2)
print(x_3)
print(x_4)

print(x_1*x_2*x_3*x_4)
