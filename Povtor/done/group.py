with open("logs.txt") as f:
    data = f.readlines()
    errors = {}
    for line in data:
        if "ERROR" in line:
            if "ERROR" not in errors:
                errors["ERROR"] = 1
            else:
                errors["ERROR"] += 1
    
        if "INFO" in line:
            if "INFO" not in errors:
                errors["INFO"] = 1
            else:
                errors["INFO"] += 1

    

    print(errors)