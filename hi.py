from ast import Pass


name = input("Enter your name: ")

# Check for Speacial chars
ch = "[@_!#$%^&*()<>?/\|}{~:']"

for i in ch:
    if(name.count(i) == 0):
        pass
    else:
        print("Error : Enter your name not special characters\n")
        exit(1)
for l in name:
    if (l.isnumeric() == True):
        print("Error : Enter letters not numbers\n")
        exit(2)

    else:
        pass

print(f"Hello, {name}!!\n")