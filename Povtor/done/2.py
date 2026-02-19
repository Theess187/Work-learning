with open("logs.txt") as f:
    data = f.readlines()
    print(data)
    for line in data:
        print("Дата: " + line.split()[0] + ", Время: " + line.split()[1])
        
