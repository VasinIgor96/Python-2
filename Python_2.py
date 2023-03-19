num = int(input('Введіть число яке бажаєте перевернути:'))
reverse_num = 0

reverse_num = reverse_num * 10 + num % 10
num = num // 10

reverse_num = reverse_num * 10 + num % 10
num = num // 10

reverse_num = reverse_num * 10 + num % 10
num = num // 10

reverse_num = reverse_num * 10 + num % 10
num = num // 10

print(reverse_num)
