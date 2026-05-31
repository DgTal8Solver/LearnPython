def bread(func):
    def wrapper(*args, **kwargs):
        print("Bread")
        func(*args, **kwargs)
        print("Bread")
    return wrapper

def salad(func):
    def wrapper(*args, **kwargs):
        print("Salat")
        func(*args, **kwargs)
    return wrapper

def tomato(func):
    def wrapper(*args, **kwargs):
        print("Tomato")
        func(*args, **kwargs)
    return wrapper

def meat(func):
    def wrapper(*args, **kwargs):
        print("Meat")
        func(*args, **kwargs)
    return wrapper

@bread
@salad
@tomato
@meat
def make_sandwich():
    pass

def main():
    make_sandwich()

if __name__ == "__main__":
    main()
