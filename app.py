name = input("Enter your name: ")

mark1 = int(input("Enter Tamil mark: "))
mark2 = int(input("Enter English mark: "))
mark3 = int(input("Enter Maths mark: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 35:
    print("Grade: D")
else:
    print("Result: Fail")