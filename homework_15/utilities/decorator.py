from parser import verbose


def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        if verbose:
            print("Starting to process your request")
        func(*args, **kwargs)
        if verbose:
            print("Processing is over")

    return wrapper
