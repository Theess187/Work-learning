errors = 0
info = 0
success = 0
with open("DPINST.LOG", "r",encoding="utf-16") as log:
    # print("This is a log file", log.read())
    for l in log:
        # print(repr(l))
        if "ERROR" in l:
            errors += 1 
        elif "INFO:" in l:
            info += 1 
        elif "SUCCESS" in l:
            success += 1
            print(l.strip())
print("Total errors found:", errors)
print("Total info messages found:", info)
print("Total success messages found:", success)