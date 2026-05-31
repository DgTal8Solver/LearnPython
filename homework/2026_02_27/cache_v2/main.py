import json
import os

__file__

def cache(filename: str):
    def decorator(func):
        data = {}
        path = os.path.join(
            os.path.dirname((__file__)),
            filename
        )
        try:
            with open(path, 'r') as file:
                data = json.load(file)
                print("Loaded")
        except:
            pass

        def wrapper(*args, **kwargs):
            params = dict(zip(func.__code__.co_varnames[:len(args)], args))
            params.update(kwargs)
            params = dict(sorted(params.items(), key=lambda x: x[0]))

            key = f"{func.__name__}:{params}"
            if key not in data:
                data[key] = func(*args, **kwargs)
                with open(path, 'w') as file:
                    json.dump(data, file)
                print(f"Add new key:\n\t{key}")
            return data[key]

        return wrapper
    
    return decorator

@cache("cache.json")
def my_sum(a, b):
    return a + b

def main():
    my_sum(1,3)
    my_sum(2,3)

    my_sum(b=3, a=1)
    my_sum(2, b=3)

if __name__ == "__main__":
    main()