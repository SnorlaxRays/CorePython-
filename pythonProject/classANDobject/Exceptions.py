'''
try:
    name = int(input("Enter any number:"))
    print(name)

except Exception as e:
    print("Exception:" , e)

else:
    print("Your name is " + name)

finally:
    print("This is a python language")



try:
    number = int(input("Enter your number:"))
    if number > 10:
        raise Exception("Invalid number")

except Exception as e:
    print(e)


while True:
    try:
        x = int(input("Please enter any number:"))
        break

    except Exception as e:
        print(e)
    except ValueError:
        print("That was no valid number. Try again...")

'''
'''
def this_fails():
    x = 1/0

try:
    this_fails()

except Exception as e:
    print(e)

try:
    x = 0 * 0

except(ZeroDivisionError,ValueError):
    print('ZeroDivisionError or ValueError is raised')
except:
    print('Something else went wrong')
else:
    print("Nothing went wrong")
finally:
    print("Always execute this") #this fianlly clause to define clean-up actions that must be executed under all circumstances e.g closing a file

#we use raise Keyword to instantiate the Exception 
You use raise ur custom exception using raise keyword
'''
'''
class InputError(Exception):
    pass

raise InputError('Custom exception')
'''












