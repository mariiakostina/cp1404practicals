#Task 1
out_file = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

#Task2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

#Task3
with open("numbers.txt", "r") as in_file:
    number_1 = int(in_file.readline())
    number_2 = int(in_file.readline())
print(number_1 + number_2)

#Task4
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)
