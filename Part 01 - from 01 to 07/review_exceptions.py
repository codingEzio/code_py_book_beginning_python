from warnings import warn


# ----------- ----------- Self-defined ----------- -----------
class PanicError(Exception):
    pass


try:
    raise PanicError()
except PanicError:
    print(f"Ahhhh.. It’s {PanicError.__name__} !!")

# ----------- ----------- Do something with it ----------- -----------


class Calculator:
    be_gentle = False

    def calc(self, expr):
        try:
            return eval(expr)
        except Exception:
            if self.be_gentle:
                print("Something had gone wrong, man!")
            else:
                raise


my_calc = Calculator()

try:
    my_calc.calc("10 / 0")
except Exception:
    my_calc.be_gentle = True
    my_calc.calc("10 / 0")
else:
    print("I'll be exec_ed if there's no error being catched.")
finally:
    print("I'll always be here :P")

# ----------- ----------- Except Exceptions ----------- -----------

warn("I've got a bad feeling right now :(")
