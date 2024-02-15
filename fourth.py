#list
my_list = [1,2,3,4]


#tuple

# my_tuple = (1,) tupleda faqat bitta element saqlash kerak bo'lsa (1,) vergul ham qo'tib ketish kerak sababi buni tuple ekanligi ajratib turadi

# my_tuple = tuple((1)) bunda vergul shart emas

my_tuple = (1,2,3,4,5)

#set

my_set = {1,2,3,4,5,True, "true",}

#set amallari

set1 = {1,2,3,4}
set2 = {5,6,7,8}

temp_set = set1.union(set2)#ikkalasidagi sonlarni bitta to'plam qilib beradi

temp_set = set1 | set2 #ikkalasidagi sonlarni bitta to'plam qilib beradi



temp_set = set1.intersection(set2) # ikkalasida borini olib beradi 


temp_set = set1.difference(set2) # ikkalasida yo'g'larini olib beradi

temp_set = set1 - set2 # ikkalasida yo'g'larini olib beradi



#dictionary

my_dictonary = {
    "Name": "Abduqodir",
    "lastname": "Abdusattorov",
}

print(my_dictonary["lastname"])
print(my_dictonary.get("name"))
