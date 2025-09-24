def memoize(method):
    cache = {}
    def wrapper(self, *args):
        if args not in cache:
            cache[args] = method(self, *args)
        return cache[args]
    return wrapper

class Fibonacci:
    @memoize
    def calc(self, n):
        if n <= 1:
            return n
        return self.calc(n-1) + self.calc(n-2)

fib = Fibonacci()
print(fib.calc(30))
