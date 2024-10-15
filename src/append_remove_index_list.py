list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 1, 3, 5, 2, 5]
list.append(10)
list.remove(9)
list.sort(reverse=True)
print("Descending order:", list)

list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 1, 3, 5, 2, 5]
index_1 = list.index(1)
list.insert(index_1 + 1, 5)
print("updated list is:", list)