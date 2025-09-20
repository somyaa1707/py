
user_text = input("Enter some text to write: ")
with open("output.txt", "w") as file:
    file.write(user_text + "\n")
print("Data written to 'output.txt'.")
append_text = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(append_text + "\n")
print("Additional data appended to 'output.txt'.")
print("\nFinal content of 'output.txt':\n")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
