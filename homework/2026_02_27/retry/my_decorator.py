from typing import Any

def retry(count):
    def decorator(func):
        def wrapper(*args, **kwargs) -> Any | None:
            for _ in range(count):
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    continue
                except OSError:
                    print(f"{func.__name__} raise OsError exception.")
                    return None
            print(f"{func.__name__} raise Retry exception.")
            return None
        return wrapper
    return decorator