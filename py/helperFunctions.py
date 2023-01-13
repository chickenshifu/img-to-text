import time

def chronograph(function):
    def wrapper(*args, **kwargs):
        print(f"{function.__name__} started at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        result = function(*args, **kwargs)
        print(f"{function.__name__} ended at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        return result
    return wrapper


def print_color(color, text):
    color_code = ""
    if color == "red":
        color_code = "\033[91m"
    elif color == "green":
        color_code = "\033[92m"
    elif color == "blue":
        color_code = "\033[94m"
    else:
        color_code = "\033[0m"
    print(color_code + text + "\033[0m")

