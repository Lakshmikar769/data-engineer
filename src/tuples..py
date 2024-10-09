t= (10, 15, 55, 4.3, 3.14, True, "welcome", False, "to", "Python")
x = t[2]
print(x)
# slice the tuple to retrive the last 3 elements
y = t[-3::]
print(y)

#finding the index of a particular element
t.index(3.14)

#count how many times the element is repeated
t.count(55)

#add an element to existing tuple
a = t+(100,)
print(a)

x = list(t)
x.append(100)
y= tuple(x)
print(y)

#remove an element from a tuple
x = list(t)
x.remove(55)
y= tuple(x)
print(y)

#pack a tuple
names = ("India", "America", "Mexico")

#unpack the tuple
names = ("India", "America", "Mexico")
(Hindi, English, Spanish) = names
print(Hindi)
print(English)
print(Spanish)

#using the 4 operations
k = {1,2,3,4,5,6}
j = {4,5,6,7,8,9}
print(k | j)
print(k & j)
print(k - j)
print(k ^ j)

#list created and duplicates removed and add and remove elements
l= [4,3,5,3,2,5,3,6,7,8,3,5,2,1,6,7]
m = list(set(l))
print(m)
set(l)
l.remove(5)
l.append(10)
