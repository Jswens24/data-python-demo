# print("Hello World!")

from gc import garbage


first_name = "Jessica"
last_name = "Swenson"
age = 28
age = 2
age = 15

# print(age)

# if age >= 18:
#     print(("I am an adult"))
# elif age < 13:
#     print("I am an infant")
# else:
#     print("I am an alien")


# favorite_numbers = [1, 2, 3, 4, 5, "hello", True, 2.0]
# print(favorite_numbers)

# for num in favorite_numbers:
#     print(num)

# def sum (num_one, num_two):
#     print(num_one + num_two)

# sum(2,3)

open_file = open('FinalGrades.csv')
# total_a = 0
# total_b = 0
# total_c = 0

# for line in open_file:
#     line = line.strip()
#     values = line.split(',')
#     # print(values)
#     for value in values:
#         if value == "A":
#             total_a += 1
#         elif value == "B":
#             total_b += 1
#         elif value == "C":
#             total_c += 1

# print("A's:", total_a)
# print("B's:", total_b)
# print("C's:", total_c)

for line in open_file:
    line = line.strip()
    values = line.split(",")
    print(values[0])

open_file.close()

prime_num = float(1)
print(prime_num)