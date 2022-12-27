import re

#1
def to_camel_case(text):
   return ''.join([word.title() for word in re.split('_|-', text)])

#2
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
            return cls._instances[cls]
        else:
            raise NotImplementedError(f"Объект класса {cls.__name__} уже создан и находится здесь: {cls._instances[cls]}")

class A(metaclass=SingletonMeta):
    pass

#3
count_bits = lambda n: bin(n).count('1')

#4
def digital_root(n):
    return n if int(n) < 10 else digital_root(sum(map(int,str(n))))

#5
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"

assert to_camel_case("_i_love_python-and_programming") == "ILovePythonAndProgramming"
assert to_camel_case("i_love_python-and_programming") == "ILovePythonAndProgramming"
assert count_bits(100) == 3
assert digital_root(1111) == 4
assert even_or_odd(8) == "Even"
assert even_or_odd(9) == "Odd"
print("Successfully asserts")

a1 = A()
a2 = A()