# conftest.py
import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide  # Assuming these are defined in your_module

fake = Faker()

def generate_test_data(num_records):
    operations = [add, subtract, multiply, divide]
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1, fix_len=True))
        operation = fake.random_element(elements=operations)
        
        # Ensure b is not zero if operation is divide
        if operation == divide:
            b = Decimal(fake.random_number(digits=2, fix_len=True)) if b == 0 else b
        
        # Calculate the expected result based on the operation, include try-except for divide
        try:
            expected = operation(a, b)
        except ZeroDivisionError:
            continue  # Skip this iteration and generate a new set of data
        
        yield a, b, operation, expected


def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    if "a" in metafunc.fixturenames and \
       "b" in metafunc.fixturenames and \
       "operation" in metafunc.fixturenames and \
       "expected" in metafunc.fixturenames:
        num_records = metafunc.config.getoption("num_records")
        metafunc.parametrize("a,b,operation,expected", list(generate_test_data(num_records)))
