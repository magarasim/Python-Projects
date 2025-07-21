def display_menu():
	print("\n ---- Calculator ----")
	print("1. Add")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")
	print("5. Exit")

def calculator(operation, *args):
	if operation == "add":
		return sum(args)
	elif operation == "multiply":
		result = 1
		for num in args:
			result *= num
		return result
	elif operation == "subtract":
		return args[0] - args[1]
	elif operation == "divide":
		if args[1] == 0:
			return "error: Division by 0 is not possible"
		return args[0] / args[1]
	else:
		return "invalid operation"

def main():
	while True:
		display_menu()
		choice = input("choose (1-5): ")
		if choice == "5":
			print("Goodbye")
			break
		if choice in ["1", "3"]:
			nums = list(map(int, input("enter numbers separated by space: ").split()))
			op = "add" if choice == "1" else "multiply"
			result = calculator(op, *nums)
		elif choice in ["2", "4"]:
			a = int(input("First number: "))
			b = int(input("second number: "))
			op = "subtract" if choice == "2" else "divide"
			result = calculator(op, a, b)
		else:
			result = "invalid choice"
		print("result:", result)

main()