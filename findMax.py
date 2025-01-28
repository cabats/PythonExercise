#Define a function find_max(numbers) that takes a list of numbers and returns the largest number.
def find_max(n:list):
    if len(n) == 0:
        return None
    else:
        return max(n)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_max(list1))