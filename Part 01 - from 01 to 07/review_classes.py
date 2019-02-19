from abc import ABC, abstractmethod

# ---------- ---------- Basics ---------- ----------


class Person:

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello, I'm {}".format(self.name))


foo = Person()

# InstName.METHOD
foo.set_name("Arya Stark")
foo.greet()

# ClassName.METHOD(inst, param)
Person.set_name(foo, "Alex")
Person.get_name(foo)
Person.greet(foo)

# ---------- ---------- Private ---------- ----------


class AccessibleInsideTheClass:
    """
    Methods start with '__' will be inaccessible from the outside.

    Well, sort of, you would still be able
    to access it by `INSTANCE._CLASSNAME__PRIVATE_METHOD`.
    """

    def __top_secret(self):
        return "The secret is .. 42!"

    def get_secret(self):
        print(f"{self.__top_secret()} (this is from `get_secret`)")


acc = AccessibleInsideTheClass()
acc.get_secret()


# ---------- ---------- Superclass : One ---------- ----------

class Filter:
    def init(self):
        self.keywords = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.keywords]


class SpamFilter(Filter):
    def init(self):
        self.keywords = ['Spam']


oft = Filter()
sft = SpamFilter()

oft.init()
sft.init()

assert [1, 2, 3] == oft.filter([1, 2, 3])
assert [1, 2, 3] == sft.filter(["Spam", "Spam", 1, 2, 3])

assert issubclass(SpamFilter, Filter)

print(Filter.__bases__,
      SpamFilter.__bases__)

# ---------- ---------- Superclass : Multiple ---------- ----------


class Calc:
    def calculate(self, expr):
        self.value = eval(expr)


class Output:
    def output(self):
        print(f"The result is {self.value}")


class CalcAndPrint(Calc, Output):
    pass


help_me_calc = CalcAndPrint()

help_me_calc.calculate("1 + 1")
help_me_calc.output()

assert hasattr(help_me_calc, 'calculate')
assert hasattr(help_me_calc, 'output')
assert not callable(hasattr(help_me_calc, 'value'))

# ---------- ---------- Abstract Base Class---------- ----------


class HuamnAbilities(ABC):
    """
    ABC == Inheriting `ABC` + Decorating methods with `@abst..`

    It's kinda like 'interface' in other OOP languages, like Java.

    For the outside behavior,
    the instance cannot be init_ed if they weren't implemented.

        Example :: HumanCanWalk
            It only gets a `pass`, no code included.

        Example :: HumanCanWalkForReal
            It does implemented that, so it could be init_ed.

            BTW, if you're using `def ..(..): pass`
            it'll still be considered as 'implemented' (huh).
    """

    @abstractmethod
    def they_can_do(self):
        pass


class HumanCanWalk(HuamnAbilities):
    pass


class HumanCanWalkForReal(HuamnAbilities):
    def they_can_do(self):
        print("I can walk!!")


# h1 = HuamnAbilities()
# h2 = HumanCanWalk()
h3 = HumanCanWalkForReal()
