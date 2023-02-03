def FindMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    final_array = []
    for i in range(1, n[-1]):
      if i not in numbers:
        final_array.append(i)
    return final_array

list_of_numbers = [1,3,6,7,9,10,13,15,30,40]
print(FindMissingNumbers(list_of_numbers))