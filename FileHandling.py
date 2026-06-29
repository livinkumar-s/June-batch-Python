# file=open("text.txt",'r')
# # print(file)
# # content=file.read(5)
# # content=file.readline()
# # content=file.readline()
# # content=file.readline()
# # content=file.readlines()[2]
# # print(content)
# file.close()

# file=open("text.txt","w")

# content='''Hello
# Hi
# Welcome'''

# # print(file.writable())
# file.write(content)

# file.close()

# file=open("text1.txt","a")

# content='''\nHello
# Hi
# Welcome'''

# # print(file.writable())
# file.write(content)

# file.close()

# file=open("text.txt",'r')
# file.seek(5)
# print(file.read(5))
# print(file.tell())
# file.close()

# file=open("text.txt","r")
# a=file.read(5)
# file.seek(0)
# b=file.read(10)
# print(a)
# print(b)
# file.close()

with open("text.txt","r") as f:
    a=f.read(5)
    f.seek(0)
    b=f.read(10)
    print(a)
    print(b)