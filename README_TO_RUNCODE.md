# How to run code.
This code runs in python 3 by writing into terminal "Python3 src/simulator.py <memfile dest>" for example, "python3 src/simulator.py tests/integration/memfiles/add1.mem"
This should print out every register in the register file and what is currently on them.

# How to run tests
This folder also allows for pytest to be run, it is recommended to run all tests through the test_mips.py file by writing "pytest -rPf tests/integration/test_mips.py" which will run every integration test.