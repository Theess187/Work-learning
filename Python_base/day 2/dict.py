import sys

errors ={
    500: "Internal Server Error",
    404: "Not Found",
    403: "Forbidden",
    401: "Unauthorized",
    200: "OK",
    400: "Bad Request"
}

code=int(sys.argv[1])
if code in errors:
    print(errors[code])  
else:
    print("Code not found")
    code = int (input("Enter another code: "))
    print(errors[code])


# не получилось сделать перепроверку на наличие кода в словаре при втором вводе
# и правильность ввода тоже не проверяется