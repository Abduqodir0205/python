soz = "Welcome to our todays class and be ready to code"

print(len(soz))
print(soz[0])
print(soz[11])
print(soz[-2])



#string slicing
print(soz[0:12])
print(soz[:10])
print(soz[0:5])



#string methods
soz = "    Welcome to our todays class and be ready to code    "

print(soz.upper()) #textagi harflarni hammasini katta qilib beradi 
print(soz.lower())  #hariflarni kichkina qilib beradi
print(soz.capitalize()) #texni birinchi harifini katta qilib beradi
print(soz.replace("e", "b", 1)) #e harfini bga faqat birinchi uchraganini almashtirib beradi
print(soz.count("a")) #a necha marta qatnashganini chiqarib beradi
print(soz.strip()) #bo'sh joylarni olib tashlaydi


#math method
print(2 ** 3) #2ning kubi ** bu operator darajaga ko'taradi
print(6 // 2) #qoldiqni eng pastki butun sonni olib beradi

#masala
name = str(input("Ismizi kiriting =>"))
oylig = float(input("oyligizi kiritng =>"))
tax = 3.8

foiz = ((oylig / 100) * 3.8) * 12

res = (oylig * 12) - foiz

print(f"{name} yillik soliq {foiz} va yillik daromadiz {res}")


    




