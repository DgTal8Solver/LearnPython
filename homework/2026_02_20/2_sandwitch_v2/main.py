def bread(func):
    def wrapper(*args, **kwargs) -> str:
        result = func(*args, **kwargs)
        if result:
            return f"Bread\n{result}\nBread"
        return "Bread\nBread"
    return wrapper

def salad(func):
    def wrapper(*args, **kwargs) -> str:
        result = func(*args, **kwargs)
        if result:
            return f"Salat\n{result}"
        return "Salat"
    return wrapper

def tomato(func):
    def wrapper(*args, **kwargs) -> str:
        result = func(*args, **kwargs)
        if result:
            return f"Tomato\n{result}"
        return "Tomato"
    return wrapper

def meat(func):
    def wrapper(*args, **kwargs) -> str:
        result = func(*args, **kwargs)
        if result:
            return f"Meat\n{result}"
        return "Meat"
    return wrapper

@bread
@salad
@tomato
@meat
def make_sandwich() -> str:
    return ""

def main():
    sandwich = make_sandwich()
    print(sandwich)

if __name__ == "__main__":
    main()
