def status(number):
    result = number%2
    if result == 0:
        return "even number"
    else:
        return "odd number"


answer= status(4)
print(answer)
