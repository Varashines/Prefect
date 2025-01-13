def calc(x,y):
	addition = add(x,y)
	substraction = sub(x,y)

	print(f"With {x},{y}: addition gives {addition} and substraction gives {substraction}")

def add(x,y):
	return (x+y)

def sub(x,y):
	return (x-y)

if __name__ == "__main__":
	calc(4,6)
