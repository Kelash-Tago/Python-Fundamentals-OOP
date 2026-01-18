def calculator(a,b,operator):
    match operator:
        case "+":
            print(a+b)
        case "-":
            print(a-b)
        case "*":
            print(a*b)
        case "/":
            print(a/b)
        case _:
            print("operator not matched.")
    
calculator(15,3,"*")
