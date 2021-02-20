'''
Author: David Bernal
'''

def addition(x: int, y: int):
    return x + y

def print_hello(s: str):
    print(s)

def main():
    val = "Hello"
    print_hello(val)
    x,y = 5, 5
    total = addition(x,y)
    print(total)

if __name__ == "__main__":
    main()
