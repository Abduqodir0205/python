number_char = ["vsf", "ppp", "xxx"]

car_number = input("Enter car number ->")

car_text = ''
for i in car_number:
    if i.isdigit():
        continue
    else:
        car_text += i.lower()

for j in range(len(car_text)):
    if car_text[j] == ".":
        car_text = car_text.replace(car_text[j],' ')
        
res =  car_text.replace(" ", "")

count = 0
for element in number_char:
    if element == res:
        count += 1

if count > 0:
    print("Bu raqam egasiga jarima yozish mumkin emas!")
else:
    print("Bu raqam egasiga jarima yozsa bo'ladi.")

