def debug(func):
    def wrapper(*args, **kwargs):
       args_value = ' ,'.join(str(arg) for arg in args)
       kwargs_value = ' ,'.join(f"{k}:{v}" for k,v in kwargs.items())
       print(f"calling: {func.__name__} with args {args_value} and with kwargs{kwargs_value}") 
       return func(*args,**kwargs)
    return wrapper

@debug
def hello():
    print("hello")
    
hello()

@debug
def greet(name,greeting="hello"):
    print(f"{greeting}, {name}")
    
greet("bhalla ji")
    