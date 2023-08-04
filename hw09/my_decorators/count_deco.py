
def repeats(calls):
    def decorator(func):
        result = []

        def wrapper(*args, **kwargs):
            for i in range(calls):
                result.append(func(*args, **kwargs))
            return result

        return wrapper

    return decorator
