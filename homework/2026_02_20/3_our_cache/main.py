def cache(func):
    data = {}

    def wrapper(*args, **kwargs):
        params = dict(zip(func.__code__.co_varnames[:len(args)], args))
        params.update(kwargs)
        params = dict(sorted(params.items(), key=lambda x: x[0]))

        key = f"{func.__name__}:{params}"
        if key not in data:
            data[key] = func(*args, **kwargs)
            print(f"Add new key:\n\t{key}")
        return data[key]

    return wrapper

@cache
def my_sum(a, b):
    return a + b

def main():
    my_sum(1,3)
    my_sum(2,3)

    my_sum(b=3, a=1)
    my_sum(2, b=3)

if __name__ == "__main__":
    main()