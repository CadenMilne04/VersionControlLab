while True:
    try:
        name = input("Please enter a name:")
        name = str(name)
        break
    except:
        print("Make sure you entered a valid String.")
while True:
    try:
        other = input("Please enter some other input:")
        other = int(other)
        break
    except:
        print("Make sure you entered an Integer.")
for i in range(other):
    print(name)
