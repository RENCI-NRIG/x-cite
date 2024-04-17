# Testing

Testing proves that your code works as expected in response to the
inputs that it is expected to receive.

Of course you can "manually" run your code and check that it works as
expected.  Since frequent manual testing will soon become tedious, you
can also write code that tests your code, so that much of your testing
is automated.

When you test your code, you will be more confident about the
correctness of your code.  As your project evolves, the tests you have
written will help you to test the changes more confidently.  Your
tests will also serve as a sort of documentation about how to use the
code.

There are several ways to test your code:

- **Unit tests** test the smaller units of your code, namely:
  functions, classes, and methods.
  
- **Integration tests** are used to prove that your code works
  correctly when they interface with externals systems (for example:
  you read weather data from NOAA).
  
- **System tests** are used to test that your application as a whole
  works as expected.
  
This is a big topic.  In the interest of practicality, we will limit
the discussion to unit tests here.

## Writing unit tests

Python standard library ships a [`unittest`][unittest] module, which
provides some tools for testing your code.  Let us see how this works
in practice with a quick example.

[unittest]: https://docs.python.org/3/library/unittest.html

Suppose you have written a method for temperature conversion, in a
module named `temperature.py`:

```{.python filename=temperature.py}
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    :param celsius (float): Temperature in Celsius
    
    :returns: Temperature converted to Fahrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
```

You will write tests for your code in a corresponding module named
`test_temperature.py`:

```{.python filename=test_temperature.py}
import unittest

from temperature import celsius_to_fahrenheit

class TestCelsiusToFahrenheit(unittest.TestCase):
    def test_conversion(self):
        # Test conversion for 0°C
        self.assertEqual(celsius_to_fahrenheit(0), 32)

        # Test conversion for 100°C
        self.assertEqual(celsius_to_fahrenheit(100), 212)

        # Test conversion for negative temperature -10°C
        self.assertEqual(celsius_to_fahrenheit(-10), 14)

if __name__ == '__main__':
    unittest.main()
```

And then you will run your tests:

```{.bash}
$ python3 test_temperature.py 
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

As you see, `unittest` module provides:

-  A `TestCase` class, which has an `assertEqual()` method (and
[several other _assert_ methods][asserts]) to check that the code has
executed as expected.

[asserts]: https://docs.python.org/3/library/unittest.html#assert-methods

- A `unittest.main()` function method which provides a way to run the
  test.

The `TestCase` class also provides methods to handle _test fixtures_
to set things up before tests are run, and tear them down later,
namely `setUp()` and `tearDown()`.


### A failing test case

What would a failing test look like?  Let us add a new test case to
our `TestCelsiusToFahrenheit` class:

```{.python}
    def test_conversion_bad_input(self):
        # Test with bad input
        self.assertEqual(celsius_to_fahrenheit("not temperature"), 0)
```

This will of course fail, and leave us enough hints about why it
failed:

```{.bash}
$ python3 test_temperature.py 
.E
======================================================================
ERROR: test_conversion_bad (__main__.TestCelsiusToFahrenheit.test_conversion_bad)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/sajith/projects/x-cite/X-CITE/theme1/PE103/test_temperature.py", line 18, in test_conversion_bad
    self.assertEqual(celsius_to_fahrenheit("not temperature"), 14)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/sajith/projects/x-cite/X-CITE/theme1/PE103/temperature.py", line 9, in celsius_to_fahrenheit
    fahrenheit = (celsius * 9/5) + 32
                  ~~~~~~~~~~~^~
TypeError: unsupported operand type(s) for /: 'str' and 'int'

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (errors=1)
```

Now you can decide how to fix the code (or the test), or whether to
fix anything at all.  You may want to reject inputs other than numbers
in your `celsius_to_fahrenheit()` function. Or you may decide that
failing on unexpected inputs is fine, and change the test accordingly:

```{.python}
    def test_conversion_bad_input_expect_exception(self):
        # Test with bad input, and expect an exception
        with self.assertRaises(TypeError):
            celsius_to_fahrenheit("not temperature")
```            


## PyTest

[PyTest] is a framework for writing and running tests. You can use
PyTest along with `unittest` module.

[PyTest]: https://docs.pytest.org/en/8.0.x/index.html

You will need to install pytest with:

```{.bash}
$ pip install pytest
```

PyTest provides a commandline program named `pytest`, which will
_discover_ the tests you have written in your project and run them.
The output is a little fancier and probably more helpful than simply
running the test module directly:

```{.bash}
$ pytest 
============================= test session starts ==============================
platform linux -- Python 3.11.2, pytest-8.1.1, pluggy-1.4.0
rootdir: /home/sajith/projects/x-cite/X-CITE/theme1/PE103
plugins: anyio-4.3.0
collected 3 items                                                              

test_temperature.py .F.                                                  [100%]

=================================== FAILURES ===================================
_________________ TestCelsiusToFahrenheit.test_conversion_bad __________________

self = <test_temperature.TestCelsiusToFahrenheit testMethod=test_conversion_bad>

    def test_conversion_bad(self):
        # Test with bad input
>       self.assertEqual(celsius_to_fahrenheit("not temperature"), 0)

test_temperature.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

celsius = 'not temperature'

    def celsius_to_fahrenheit(celsius):
        """
        Convert temperature from Celsius to Fahrenheit.
    
        :param celsius (float): Temperature in Celsius
    
        :returns: Temperature converted to Fahrenheit
        """
>       fahrenheit = (celsius * 9/5) + 32
E       TypeError: unsupported operand type(s) for /: 'str' and 'int'

temperature.py:9: TypeError
=========================== short test summary info ============================
FAILED test_temperature.py::TestCelsiusToFahrenheit::test_conversion_bad - TypeError: unsupported operand type(s) for /: 'str' and 'int'
========================= 1 failed, 2 passed in 0.08s ==========================
```

## Tox

When you share your code with your colleagues, you will want to make
sure that your code works in environments other than your own too.
[Tox] will help you to test that your project builds and installs
correctly under several environments.  You might want to test your
code with several versions of Python, and various dependencies, for
example.

You will write a configuration file named `tox.ini`:

```{.ini filename=tox.ini}
[tox]
requires =
    tox>=4
env_list = py{38,39,310,311}

[testenv]
description = run unit tests
deps =
    pytest>=7
commands =
    pytest {posargs:tests}
```

You can install `tox` like so:

```{.bash}
$ pip install tox
```

And then run `tox` like so:

```{.bash}
$ tox
py38: skipped because could not find python interpreter with spec(s): py38
py38: SKIP ⚠ in 0.01 seconds
py39: skipped because could not find python interpreter with spec(s): py39
py39: SKIP ⚠ in 0 seconds
py310: skipped because could not find python interpreter with spec(s): py310
py310: SKIP ⚠ in 0 seconds
py311: commands[0]> pytest
============================= test session starts ==============================
platform linux -- Python 3.11.2, pytest-8.1.1, pluggy-1.4.0
cachedir: .tox/py311/.pytest_cache
rootdir: /home/sajith/projects/x-cite/X-CITE/theme1/PE103
collected 3 items                                                              

test_temperature.py .F.                                                  [100%]

=================================== FAILURES ===================================
_________________ TestCelsiusToFahrenheit.test_conversion_bad __________________

self = <test_temperature.TestCelsiusToFahrenheit testMethod=test_conversion_bad>

    def test_conversion_bad(self):
        # Test with bad input
>       self.assertEqual(celsius_to_fahrenheit("not temperature"), 0)

test_temperature.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

celsius = 'not temperature'

    def celsius_to_fahrenheit(celsius):
        """
        Convert temperature from Celsius to Fahrenheit.
    
        :param celsius (float): Temperature in Celsius
    
        :returns: Temperature converted to Fahrenheit
        """
>       fahrenheit = (celsius * 9 / 5) + 32
E       TypeError: unsupported operand type(s) for /: 'str' and 'int'

temperature.py:9: TypeError
=========================== short test summary info ============================
FAILED test_temperature.py::TestCelsiusToFahrenheit::test_conversion_bad - TypeError: unsupported operand type(s) for /: 'str' and 'int'
========================= 1 failed, 2 passed in 0.04s ==========================
py311: exit 1 (0.29 seconds) /home/sajith/projects/x-cite/X-CITE/theme1/PE103> pytest pid=935973
  py38: SKIP (0.01 seconds)
  py39: SKIP (0.00 seconds)
  py310: SKIP (0.00 seconds)
  py311: FAIL code 1 (0.32=setup[0.04]+cmd[0.29] seconds)
  evaluation failed :( (0.41 seconds)
```
