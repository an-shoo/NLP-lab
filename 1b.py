# Lab 3: Check list for exactly two 19s and at least three 5s

def check_list(lst):
    # Count occurrences of 19 and 5
    count_19 = lst.count(19)
    count_5 = lst.count(5)
    return count_19 == 2 and count_5 >= 3

n = int(input("Enter the number of elements in the list: "))

lst = []
for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    lst.append(num)

result = check_list(lst)
print("Result:", result)
