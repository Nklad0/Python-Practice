import random


def message(p1, p2):
    for _ in range(p2):
        print(p1)

def main():
    input_text = input("Enter a text: ")
    text = input_text.title()
    print(f"text = {text}")
    n = random.randint(1, 10)
    print(f"n = {n}")
    print(f"message(text, n) will print the following:")
    message(text, n)

if __name__ == "__main__":
    main()
