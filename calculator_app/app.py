import calc as ca


def main():
    print("<--CALCULATOR-->")
    print("=" * 30)

    while True:
        print("\nSelect operation:\n")
        print("-" * 30)
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exponentiate\n6. Exit")
        print("-" * 30, "\n")

        operator = int(input("Enter your choice: "))
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        match operator:
            case 1:
                
                print("Result:", ca.add(a, b))

            case 2:
                
                print("Result:", ca.subtract(a, b))

            case 3:
                
                print("Result:", ca.multiply(a, b))

            case 4:
                

                result = ca.divide(a, b)

                if result is False:
                    print("Cannot divide by zero!")
                else:
                    print("Result:", result)

            case 5:
                
                print("Result:", ca.exponentiate(a, b))

            case 6:
                print("Thanks for using Calculator!")
                break

            case _:
                print("Invalid choice!")


if __name__ == "__main__":
    main()