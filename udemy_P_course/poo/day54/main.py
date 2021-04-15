import time

current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        stop_time = time.time()
        print(f"{function.__name__} run speed: {stop_time - start_time}")
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()










# Python Decorator

# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#     return wrapper_function
#
# @delay_decorator
# def hello():
#     print("Hello")
#
# @delay_decorator
# def bye():
#     print("bye")
#
# def greet():
#     print("greet")
#

