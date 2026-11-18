number = [10,20,30,40]
first_element = number[0]
last_element = number[-1]
number[1] = 25
total_elements = len(number)
number.append(50)
number.insert(2,35)
number.extend([60,70])
print("First element:", first_element)
print("Last element:", last_element)
print("Total elements:", total_elements)
print("Updated list:", number)
removed_element = number.pop(3)
print("Removed element:", removed_element)
position = number.index(25)
print("Position of 25:", position)
occurrence = number.count(50)
print("Occurrence of 50:", occurrence)

doubled = [x *2 for x in number]
print("Doubled list:", doubled)
filtered = [x for x in number if x <50]
print("Filtered list (elements < 50):", filtered)

number.sort()
print("Sorted list:", number)
values = [1,2,3,4,5,6,7,8,9,10,11,12]
rows ,cols =3,4
matrix = [[values[i * cols + j] for j in range(cols)] for i in range(rows)]
print("Matrix:", matrix)

val = matrix[1][2]
print("Value at row 1, column 2:", val)
matrix[1][2] = 5
print("Updated matrix:", matrix)

