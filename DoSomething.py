#This is a very cool program

while True:
    try:
        name = str(input("Please enter a name:"))
        break
    except:
        print("Make sure you entered a valid String.")
while True:
    try:
        other = int(input("Please enter some other input:"))
        break
    except:
        print("Make sure you entered an Integer.")
for i in range(other):
    print(name)
