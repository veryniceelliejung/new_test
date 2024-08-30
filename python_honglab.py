# string slicing
a = "ABCDEFGHIJKLMNO"
print(a[::-1]) # backward

print(a[-1:0:-2]) # OMKIGEC
print(a[-1::-2]) # OMKIGECA

a[:]
b = a[:]
print(id(a))
print(id(b)) # same id

# change one character
a = a[:7] + "Z" + a[7:]
print(a)

a = "ABCDEFGHIJKLMNO"
# string method
print(a.ljust(20), "ZZ") # left align the string, using a specified character (space is default) as the fill character

print("{a} {b}".format(a = "Ellie", b = "Jung"))

print("{0:8}{1:8}".format("Ellie", "Jung")) # 칸조절

print(" {0:<10} | {1:^12} | {2:^12} |".format("Left", "Center", "Right"))

print("The result is:{0:10.4f}.".format(123.456789)) # float precision
num = 123.456789
print(f"The result is {num:{10}.{6}}.") # 10은 빈칸 포함 수, 6은 출력 글자수

name = "Ellie"
print(f"I am {name}.")

# list
my_list = [1, 2, 3]
print(id(my_list))
my_list = my_list * 2
print(id(my_list))

my_list = [1, 2, 3]
print(id(my_list))
my_list *= 2
print(id(my_list))

my_list.append(4)
print(id(my_list))

print(my_list)
my_list.reverse()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

# Nested List
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

new_matrix = [a, b, c]
print(new_matrix)
print(new_matrix[0][0])
print(new_matrix[0][2])

# tuple unpacking
t = (123, 456, "hello")
x, y, z = t
print(x)
print(y)
print(z)

# set
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
print("union: ", A | B)
print("intersection: ", A & B)
print("difference: ", A - B)
print("symmetric difference: ", A ^ B)

# dictionary
new_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}
print(list(new_dict.items()))
print(list(new_dict.keys()))
print(list(new_dict.values()))

for item in new_dict.items():
    print(item)

for item in sorted(new_dict):
    print(f"{item}: {new_dict[item]}")

# identity operator
a = 123
b = a
c = 123.0

print("a is b", a is b)
print("a is c", a is c) # is: same id
print("a == c", a == c) # ==: same value
