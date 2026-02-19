

statuses = {
    1: "UP",
    2: "DOWN",
    3: "UNKNOWN"
} 

while True:
    try:
        status = int(input("Enter service status (UP(1)/DOWN(2)/UNKNOWN(3))/Exit(4): "))
        if status == 4:
            print("Exiting the program.")
            break
    except ValueError:
        print("Invalid input. Text. Please enter a number.")
        continue
    else:        


        if status    in statuses:
            print ("Service status is", statuses[status])
        else:
            print("Invalid input. Number out of range. Please enter 1, 2, or 3.")
            
