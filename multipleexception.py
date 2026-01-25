try:
    num1,num2=eval(int(input("enter two numbers separated by comma:")))
    result=num1/num2
    print("the answer is", result)

except ZeroDivisionError as e:
    print(e)
except ValueError as f:
    print(f)
except SyntaxError as s:
    print(s)
finally:
    print("mathy person ")