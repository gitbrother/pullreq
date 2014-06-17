
def FizzBuzz(number):
	if number % 15 == 0:
		return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)
