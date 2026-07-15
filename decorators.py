import time
def logger(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        print("Analysis Started at :",start)
        result = func(*args, **kwargs)
        end=time.time()
        print(f"{func.__name__} Completed")
        print("Analysis Completed at :",end)
        timetaken=end-start
        print("Time taken:",timetaken,"secs")
        return result
    return wrapper