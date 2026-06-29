print(1)
print(2)
print(3)
# if True:
# print("Hello"
print(4)
print(5)
# Print(6)
# print(4/0)
# print(int("the Taj Mahal"))

# try:
#     Print("5"+7)
#     print(9/0)
# except TypeError:
#     print("Invalid Expression...!")
# except ZeroDivisionError:
#     print("Wrong Division...!")
# except Exception:
#     print("Wrong Code...!")

# print("Hello"+55)

# try:
#     print("Hello"+55)
# except TypeError:
#     print("wrong expression")

# try:
#     inp1=int(input("Enter a Number: "))
#     inp2=int(input("Enter a Number: "))
#     print(inp1/inp2)
# except ZeroDivisionError:
#     print("You cannot divide a num by '0'")
# except ValueError:
#     print("Please provide valid inputs...!")

# print("The code is over...!")

try:
    print(open("text1.txt").read(5))
except FileNotFoundError:
    print("File does not exist...!")
finally:
    print("The code is over")
