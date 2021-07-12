

class Calculator:
    def calculate(operand1 ,operand2 ,operation):
        operation=operation.lower() #making it case insensitive
        if operation =="add":
            return operand1 +operand2
        elif operation =="subtract":
            return operand1 -operand2
        elif operation =="divide":
            return operand1/operand2
        elif operation =="multiply":
            return operand1 *2
        else:
            return "operation not supported"


print(Calculator.calculate(1,2,"adD"))
