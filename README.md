# Tox-Unit-Testing

### Running Tox
#### pytest file 1: my_module.py
```
def square(x):

  return x ** 2
```
#### pytest file 2: test_my_module.py
```
from my_module import square

def test_square_gives_correct_value():

    # When
    subject = square(4)

    # Then
    assert subject == 16
```
#### Tox File: tox.ini
```
[tox]
envlist = py27, py310
skipsdist=True

[testenv]
# install pytest in the virtualenv where commands will be executed
deps = pytest
commands = 
	# NOTE: you can run any command line tool here - not just tests
	pytest
```

### Tox Output
![image](https://github.com/srsapireddy/Machine-Learning-Model-Testing-and-Monitoring/assets/32967087/2bf8bb17-9a69-491d-8785-c35737f99277)


pytest reference: https://docs.pytest.org/en/7.4.x/ </br>
Tox Reference: https://tox.wiki/en/4.11.3/ </br>
Trox Reference 2: https://chromium.googlesource.com/external/github.com/numpy/numpy/+/refs/heads/maintenance/1.11.x/tox.ini
