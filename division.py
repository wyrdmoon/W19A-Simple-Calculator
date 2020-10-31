def divNum(num1, num2):
  try: result = num1 / num2
  except ZeroDivisionError:
    print("you cannot divide by zero")
  print(str(num1) + " / " + str(num2) + " = " + str(result))
