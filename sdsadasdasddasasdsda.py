# C:\\Users\\TUSER\\Desktop\\Time2Kode\\Subjects.txt
file = open("Subjects.txt", "a+")
i=0
while i != 3:
    i = int(input("Select between 1, 2, or 3:"))
    if i == 1:
        subject = input("Enter a subject ")
        file.write(f"{subject}\n")
        file.seek(0)
    elif i == 2:
        print(file.read())
    elif i!=1 or i!=2:
        print("please enter a valid number")    
    

subject = input("Enter a subject ")
file.write(subject)
file.seek(0)
print(file.read())
file.close()