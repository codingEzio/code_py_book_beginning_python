# Importing features that'll be std but not yet
#   Old ones won't be del_ed, even for this one (added in 2.7 already).
from __future__ import division

from math import ceil, floor
import turtle as turtle_gui
from string import Template as string_templates
from string import capwords as string_capwords

# Polyfill is needed if using 2.*
assert 3 / 2 == 1.5
assert 3 // 2 == 1


def modulo():
    assert 10.5 % 2 == 0.5
    assert 2.75 % 0.5 == 0.25 == 2.75 - ((2.75//0.5) * 0.5)

    assert 10 % -3 == 10 - ((10 // -3) * -3)
    assert 10 % -4 == 10 - ((10 // -4) * -4)
    assert 30 % -7 == (30 - ((30//-7) * -7))
    assert -30 % 7 == (-30 - ((-30 // 7) * 7))


def negative_power():
    assert -3 ** 2 == -9
    assert (-3) ** 2 == 9


def float_bigger_or_smaller():

    assert ceil(32.1) == 33
    assert floor(32.9) == 32
    assert round(32.9) == 33  # round() == round(X, 0)


def turtle_fun(display=False):
    """ 
    Copied from https://michael0x2a.com/blog/turtle-examples

    It might take a while to complete,
    but the result (picture) is really really awesome!
    """

    if display == True:
        ninja = turtle_gui.Turtle()
        ninja.speed(35)

        for i in range(180):
            ninja.forward(100)
            ninja.right(30)
            ninja.forward(20)
            ninja.left(60)
            ninja.forward(50)
            ninja.right(30)

            ninja.penup()
            ninja.setposition(0, 0)
            ninja.pendown()

            ninja.right(2)

        turtle.done()


def list_methods():
    """
    The `pop` method is the only (else is `None`)
    list method both modifies the list AND returns a value.


    """

    numbers = [[1], [2, 2], [3, 3, 3]]

    numbers.insert(0, -1)
    assert numbers[0] == -1
    assert numbers.remove(-1) == None  # All `None` other than `pop`!!

    numbers.append(4)
    assert numbers.pop() == 4

    numbers.extend([5, 6])
    assert numbers.pop(3) == 5
    assert numbers.pop(-1) == 6

    numbers.insert(3, [4, 4, 4, 4])  # don't use neg-idx
    assert numbers[-1] == [4, 4, 4, 4]

    numbers.sort(key=len, reverse=True)
    numbers.sort(key=len)
    numbers.sort()

    print(numbers)

    assert sorted(numbers)[-1] == [4, 4, 4, 4]
    assert sorted("acdb") == ["a", "b", "c", "d"]  # always return list


def str_fmt_best_practices():
    """
    There're four ways to format strings.
    -- "%s" % "Hello"
    -- .format
    -- f"{}"
    -- Template(str).substitute(KEY, VAL)

    A brief analysis here: https://realpython.com/python-string-formatting/
    """

    # Use f-strings!
    printf_c_alike = "%s" % "This is awesome!"
    newer_style_fmt = "{}".format("This is awesome!")
    newer_style_fstr = f'{"This is awesome!"}'

    # Safer choice that avoiding malicious user-input
    tmpl_str = string_templates("$sentence")

    print(printf_c_alike,
          newer_style_fmt,
          newer_style_fstr, sep='\n')

    print(tmpl_str.substitute(sentence="This is awesome!"))


def str_methods():

    # Related
    assert "what the".split(" ") == ["what", "the"]
    assert "what the" == " ".join(["what", "the"])

    # You'Re | You're
    assert "You're HIRED!!".title() == "You'Re Hired!!"
    assert string_capwords("You're HIRED!!") == "You're Hired!!"


def dict_methods():

    assert dict.fromkeys(["a", "b"])  # None, None
    assert dict.fromkeys(["a", "b"], 100)  # 100, 100

    assert {"name": "alex"}.get("roaming", "N/A") == "N/A"

    assert {"One": 1, "Two": 2}.pop("One") == 1
    assert {"One": 1, "Two": 2}.pop("Three", "N/A") == "N/A"


def exec_and_eval():
    from math import sqrt

    tmp_scope = {}

    # Sharing the same scope
    exec("sqrt = 3.14", tmp_scope)
    print(eval("sqrt * 100", tmp_scope))

    # The original is still intact
    print(sqrt(100))

    # Checking the scope
    print(tmp_scope['sqrt'])
    print(tmp_scope.keys())


modulo()
negative_power()
float_bigger_or_smaller()

turtle_fun(display=False)

list_methods()
str_fmt_best_practices()
str_methods()
dict_methods()
exec_and_eval()
