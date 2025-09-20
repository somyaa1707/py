students={
    "Somya":98,
    "Harshita":90,
    "Ishan":95,
    "Surya":96,
    "Abhay":89
}
name=input("Enter the student's name: ")
if name in students:
    print("Marks obtained are: ",students[name])
else:
    print("Not Found!")