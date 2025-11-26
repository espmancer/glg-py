aisles = ['2A', '3AP', '1B']
letters = []
numbers = []

# CASES
# Index is number but next index isn't a number
# Index is letter but next index isn't a letter
# Index is number AND next index is a number
# Index is a letter AND next index is a letter 
for aisle in aisles:
    for i in range(len(aisle)):
        if i+1 == len(aisle):
            break

        if aisle[i].isdigit():
            if aisle[i+1].isdigit():
                numbers.append((int) (aisle[i] + aisle[i+1]))
            else:
                numbers.append((int) (aisle[i]))
        
        if aisle[i].isalpha():
            if aisle[i+1].isalpha():
                letters.append(aisle[i] + aisle[i+1])
            else:
                letters.append(aisle[i])

print(numbers)
print(letters)