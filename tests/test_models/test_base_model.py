#!/usr/bin/python3
"""unit test 
"""
import unittest
from models.base_models import BaseModel


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = BaseModel(None)
        b2 = BaseModel(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, BaseModel(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = BaseModel()
        b2 = BaseModel(12)
        b3 = BaseModel()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = BaseModel(12)
        b.id = 15
        self.assertEqual(15, b.id)

if __name__ == "__main__":
    unittest.main()
