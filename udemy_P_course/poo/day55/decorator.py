class User:
    def __init__(self, name):
        self.name = name
        self.is_logged = False


def logging_decorator(function):
    def wrapper(*args):
        sum = 0
        print(f"You called {function.__name__}{args}")
        function(*args)
        for i in args:
            sum += i
        return (f"It returned: {sum}")
    return wrapper



@logging_decorator
def a_function(*args):
    pass

print(a_function(1, 2, 3, 4))

# @logging_decorator
# def create_post(user):
#     print(f"The first post of {user.name}")

# user1 = User("Boss")
# user1.is_logged = True


# create_post(user1)
