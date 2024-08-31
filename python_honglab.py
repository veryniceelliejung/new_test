# # string slicing
# a = "ABCDEFGHIJKLMNO"
# print(a[::-1]) # backward
#
# print(a[-1:0:-2]) # OMKIGEC
# print(a[-1::-2]) # OMKIGECA
#
# a[:]
# b = a[:]
# print(id(a))
# print(id(b)) # same id
#
# # change one character
# a = a[:7] + "Z" + a[7:]
# print(a)
#
# a = "ABCDEFGHIJKLMNO"
# # string method
# print(a.ljust(20), "ZZ") # left align the string, using a specified character (space is default) as the fill character
#
# print("{a} {b}".format(a = "Ellie", b = "Jung"))
#
# print("{0:8}{1:8}".format("Ellie", "Jung")) # 칸조절
#
# print(" {0:<10} | {1:^12} | {2:^12} |".format("Left", "Center", "Right"))
#
# print("The result is:{0:10.4f}.".format(123.456789)) # float precision
# num = 123.456789
# print(f"The result is {num:{10}.{6}}.") # 10은 빈칸 포함 수, 6은 출력 글자수
#
# name = "Ellie"
# print(f"I am {name}.")
#
# # list
# my_list = [1, 2, 3]
# print(id(my_list))
# my_list = my_list * 2
# print(id(my_list))
#
# my_list = [1, 2, 3]
# print(id(my_list))
# my_list *= 2
# print(id(my_list))
#
# my_list.append(4)
# print(id(my_list))
#
# print(my_list)
# my_list.reverse()
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)
#
# # Nested List
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [7, 8, 9]
#
# new_matrix = [a, b, c]
# print(new_matrix)
# print(new_matrix[0][0])
# print(new_matrix[0][2])
#
# # tuple unpacking
# t = (123, 456, "hello")
# x, y, z = t
# print(x)
# print(y)
# print(z)
#
# # set
# A = {0, 2, 4, 6, 8}
# B = {1, 2, 3, 4, 5}
# print("union: ", A | B)
# print("intersection: ", A & B)
# print("difference: ", A - B)
# print("symmetric difference: ", A ^ B)
#
# # dictionary
# new_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}
# print(list(new_dict.items()))
# print(list(new_dict.keys()))
# print(list(new_dict.values()))
#
# for item in new_dict.items():
#     print(item)
#
# for item in sorted(new_dict):
#     print(f"{item}: {new_dict[item]}")
#
# # identity operator
# a = 123
# b = a
# c = 123.0
#
# print("a is b", a is b)
# print("a is c", a is c) # is: same id
# print("a == c", a == c) # ==: same value
#
# # isinstance()
# # The isinstance() function returns True if the specified object is of the specified type, otherwise False.
#
# # iteration
# print("a", end=" ")
# print("b", end=" ") # 줄바꿈 없이 이어쓰기
# print()
#
# # iteration 가능 확인
# from collections.abc import Iterable
#
# print(isinstance([1, 2, 3], Iterable))
#
# my_list = [[1], [2], [3]]
# for i in my_list:
#     i *= 2
#     print(i)
# print(my_list)
#
# my_list = [[1], [2], [3]]
# for i in my_list:
#     i[0] *= 2
#     print(i)
# print(my_list)
#
# t = ([100], [200], [300])
# for i in range(len(t)):
#     t[i][0] *= 2
# print(t)
#
# # enumerate
# my_list = ["apple", "banana", "cherry"]
# for index, item in enumerate(my_list):
#     print(f"{index}: {item}")
#
# my_list = [1, 2, 3]
# for index, _ in enumerate(my_list):
#     my_list[index] *= 2
#
# print(my_list)
#
# # 무한 루프
# # break
# while True:
#     user_input = input("> ")
#     if user_input == "quit":
#         break
#     print(user_input)
#
# # Walrus Operator
# print(word := "Hello")
#
# while (word := input()) != "quit":
#     print(word)

# # List Comprehensions
# my_list = []
# for x in range(1, 11):
#     my_list.append(x**2)
# print(my_list)
#
# my_list = [x**2 for x in range(1, 11)]
# print(my_list)
#
# even_numbers = [x for x in range(11) if x % 2 == 0]
# print(even_numbers)
#
# combinations = []
# for x in [1, 2]:
#     for y in ["a", "b"]:
#         combinations.append((x, y))
# print(combinations)
#
# combinations = [(x, y) for x in [1, 2] for y in ["a", "b"]]
# print(combinations)
#
# new_combo = [(x, y) for x in range(1, 7) for y in range(1, 7) if x + y == 6]
# print(new_combo)
#
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([num for sub_list in nested_list for num in sub_list])
#
# # set comprehension
# print({v * v for v in [1, 2, 3]})
#
# # dict comprehension
# print({key: val for key, val in enumerate('ABCD') if val not in 'CB'})
#
# # type hinting
# def repeat_print(message: str, count: int) -> None:
#     for _ in range(count):
#         print(message)
#
# print(repeat_print("Hello", 3))

# lambda expression
my_func = lambda x, y: x + y
print(my_func(1, 2))

add_100 = lambda x: x + 100
print(list(map(add_100, [1, 2, 3, 4])))
print(list(map(lambda x, y: x + y, [1, 2, 3, 4], [5, 6, 7, 8])))
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))

from functools import reduce
add = lambda x, y: x + y
print(reduce(add, [1, 2, 3, 4]))

my_dict = {"apple": 3, "Alpha": 100, "Drive": 10, "data": 33, "Billy": 50}
print(dict(sorted(my_dict.items(), key=lambda item: item[1])))
print(dict(sorted(my_dict.items(), key=lambda item: item[0])))