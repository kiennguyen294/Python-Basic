def func_info(arg1, arg2):
    print('Decorator arg1 =' + str(arg1))
    print('Decorator arg2 =' +str(arg2))

    def the_real_decorator(function):

        def wrapper(*args, **kwargs):
            print('Function {} args: {} kwargs: {}'.format(function.__name__, str(args), str(kwargs)))
            result = function(*args, **kwargs)
            return result
        return wrapper
    return the_real_decorator


@func_info(3, 'Python')
def treble(a) :
    return a*3

print(treble(5))