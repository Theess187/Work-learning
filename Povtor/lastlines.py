from collections import deque

def last_lines(file, n):
    try:
        with open(file) as f:
            lastlines = deque(f,n)
        for line in lastlines:
            print(line.strip())
        
    except FileNotFoundError:
        print (f"Not Found", file)
    except UnicodeDecodeError as err:
        print("ERROR", err)
n=None
name = input("Введите имя файла: ")
# if name.find(".txt") == -1:
#     file = name + ".txt"
# else:
#     file = name
if name.endswith(".txt"):
    file = name    
else:
    file = name + ".txt"
    
print(file)
while n == None:
    try:
        n = int (input("Введите количество последних строк: "))
    except :
        print("Введите число!")
last_lines(file, n)