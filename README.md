# pytest-pokie

Pytest plugin to run tests on pokie applications

The pytest-pokie plugin extracts the pokie-based Flask application from the global namespace, and exposes a set
of predefined fixtures for pokie structures.

## avaliable fixtures

Note: fixtures depend on the predefined values for the different DI constants as specified on the pokie.constants
file.

|Fixture| Description|
|---|--------------------------|
|pokie_app| Pokie Application object|
|pokie_flask| Pokie Flask object|
|pokie_di| Pokie Di object|
|pokie_config|Pokie Config object|
|pokie_db|Pokie Database client|
|pokie_client| Flask test client| 

## writing tests for pokie applications

Pytest must be invoked using the internal pokie pytest runner. The pytest runner will automatically add the pytest-pokie
plugin to pytest. All additional pytest command-line arguments can be specified:

```shell
$ python main.py pytest --help

[Pokie] Running pytest with: ['--help']
usage: main.py [options] [file_or_dir] [file_or_dir] [...]

positional arguments:
  file_or_dir

general:
  -k EXPRESSION         only run tests which match the given substring expression. An expression is a python evaluatable expression where all names are substring-matched against test names and their parent classes. Example: -k
                        'test_method or test_other' matches all test functions and classes whose name contains 'test_method' or 'test_other', while -k 'not test_method' matches those that don't contain 'test_method' in their names. -k
                        'not test_method and not test_other' will eliminate the matches. Additionally keywords are matched to classes and functions containing extra names in their 'extra_keyword_matches' set, as well as functions which
                        have names assigned directly to them. The matching is case-insensitive.
  -m MARKEXPR           only run tests matching given mark expression.
                        For example: -m 'mark1 and not mark2'.
  --markers             show markers (builtin, plugin and per-project ones).
  -x, --exitfirst       exit instantly on first error or failed test.
  --fixtures, --funcargs
(...)
$
```

The scaffold structure is similar to the common pytest usage:
```shell
some_module/
  (...)
main.py
tests/
  __init__.py
  some_module/
    __init__.py
    test_something.py  
```

And to run the tests:
```shell
$ python3 main.py pytest
```

## using tox

