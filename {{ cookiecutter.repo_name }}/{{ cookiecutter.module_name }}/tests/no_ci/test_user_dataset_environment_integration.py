## Test dataset information
import unittest

from {{ cookiecutter.module_name }}.data import Dataset


class TestDatasets(unittest.TestCase):
    """
    Basic smoke tests to ensure that all of the available datasets
    load and have some expected property.
    """
    def basic_unit_test(self):
        assert True
