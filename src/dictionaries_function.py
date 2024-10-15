strings = ["welcome", "to", "python", "programming", "language", "in", "data", "engineering"]
a = [s.upper() for s in strings]
print(a)

longest_string = max(strings, key=len)
shortest_string = min(strings, key=len)
print(longest_string)
print(shortest_string)

c = '-'.join(strings)
print(c)

student_list = {'lucky': 99, 'jo': 88, 'sathwik': 77, 'sasi': 66, 'sai': 55}
highest = max(student_list, key=student_list.get)
highest_score = student_list[highest]
lowest = min(student_list, key=student_list.get)
lowest_score =student_list[lowest]
print(f"{highest} :{highest_score}")
print(f"{lowest} :{lowest_score}")

student_list = {'lucky': 99, 'jo': 88, 'sathwik': 77, 'sasi': 66, 'sai': 55}
student_list['vijay'] = 44
print(student_list)

if 'sasi' in student_list:
    del student_list['sasi']
print(student_list)