# def error_report():
#     errors = {
#         "total": 0,
#         "by type": {}
#     }
#     with open("logs.txt") as f:
#         for line in f:
#             parts = line.strip().split()

#             if len(parts) >= 3 and parts[1] == "ERROR":
#                 error_text = " ".join(parts[2:])
#                 errors["by type"][error_text] = errors["by type"].get(error_text, 0) + 1
#                 errors["total"] += 1
#     return errors

# print(error_report())

def error_report():
    errors = {
        "total": 0,
        "by type": {}
    }

    with open("logs.txt") as f:
        for line in f:
            
            
    return errors