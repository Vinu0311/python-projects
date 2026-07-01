print("Hello,", "Vinay", "! Welcome.")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

for i in range(1, 11):
    print(i)

numbers = [10, 25, 8, 45, 30]

print("Maximum number:", max(numbers))

my_list = [1, 2, 3, 2, 4, 1, 5]

unique_list = list(set(my_list))

print(unique_list)

def square(num):
    return num * num

print(square(5))

numbers = [2, 3, 4, 2, 5, 2]

count = numbers.count(2)

print("Number 2 appears", count, "times")