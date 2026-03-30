def main():
    print("Let's calculate!")
    
    x = int(input("x > "))
    y = int(input("y > "))
    
    print("%d + %d = %d" % (x, y, add(x, y)))
    print("%d - %d = %d" % (x, y, subtract(x, y)))
    print("%d * %d = %d" % (x, y, multiply(x, y)))
    print("%d / %d = %0.3f" % (x, y, divide(x, y)))
    
    
def add(a, b) -> int:
    return a + b

def subtract(a, b) -> int:
    return a - b

def multiply(a, b) -> int:
    return a * b
    
def divide(a, b) -> float | None:
    try:
        return a/b
    except ZeroDivisionError:
        print("Error: cannot divide by zero.")     
        return None

if __name__ == "__main__":
    main()
