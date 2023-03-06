
#Create first .txt file and write sorted integers into this
numbers1 = [1, 3, 2, 4, 6, 5, 7, 8, 10, 9]

with open("numbers1.txt", "w") as f:
    numbers1.sort()
    for number in numbers1:
        f.write(str(number) + "\n")
    
#Create second .txt file and write sorted integers into this
numbers2 = [20, 40, 30, 60, 50, 80, 70, 100, 90, 110]

with open("numbers2.txt", "w") as f:
    numbers2.sort()
    for number in numbers2:
        f.write(str(number) + "\n")

# Read the contents of the first text file, cast to int and add numbers to list numbers_1
numbers_1 = []
with open("numbers1.txt", "r") as f:
    for line in f:
        numbers_1.append(int(line.strip()))

# Read the contents of the second text file, cast to int and add numbers to list numbers_2
numbers_2 = []
with open("numbers2.txt", "r") as f:
    for line in f:
        numbers_2.append(int(line.strip()))

#Create third .txt file and write the combined lists into this
with open("all_numbers.txt", "w") as f:
    combined_numbers = numbers_1 + numbers_2
    combined_numbers.sort()
    f.write(str(combined_numbers))

print(combined_numbers)