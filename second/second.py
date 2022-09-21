def input_write(text = ""):
    while True:
        try:
            score = int(input(text))
            return score
        except ValueError as error:
            print("Напшите число")

a = input_write("Ведите число:")
b = input_write("Ведите число:")

print(f"{a} + {b} = {a + b}")