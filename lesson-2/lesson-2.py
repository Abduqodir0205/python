#List > Array 
'''

hobbiy = ["Coding", "running", "footboll"] # array 

number = [1,2,3,4,5,6] # array

print(hobbiy[1])

#Listni qo'shish

hobbiy.extend(number) # hobbiy arrayiga number arrayini qo'shib beradi

hobbiy.append("Verual game") # append methodi arrayni ohriga element qo'shadi

hobbiy.insert(0, 11) # arrayni berilgan indexni almashtirib beradi

hobbiy.pop() # pop arrayni oxirgi elementini olib tashlaydi

new_hobbi = hobbiy.copy() # arrayni ikkinchi arrayga nushalab beradi
print(new_hobbi)
'''
# Assesment - 1
'''
xonani_boyi = float(input("Xonani boyi ->"))
xonani_eni = float(input("Xonani eni ->"))
xonani_balandligi = float(input("Xonani balandligi ->"))

derazalar_soni = float(input("derazalar soni ->"))
derazalar_boi = float(input("derazalar boyi ->"))
derazalar_eni = float(input("derazalar eni ->"))

res = 2*(xonani_boyi * xonani_balandligi) + 2*(xonani_balandligi * xonani_eni) - derazalar_soni * (derazalar_boi * derazalar_eni) + (xonani_eni * xonani_boyi)

print(res * 0.45 + "kg")
'''

#assesment - 2
'''
masofa = float(input("Masofani kiriting"))

balon_radius = float(input("Balon radiusini kiriting ->"))

res = (masofa *100000) / (2*3.14*balon_radius)

print(res)

'''