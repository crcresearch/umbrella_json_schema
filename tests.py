# Copyright (C) 2016, University of Notre Dame
# All rights reserved
import json
import unittest
from jsonschema.validators import validate
import jsonschema.exceptions
import os


class Test(unittest.TestCase):
    def setUp(self):
        with open("json_schema.json") as fp:
            self.schema = json.load(fp)

    def _load(self, filename):
        with open(os.path.join("data", filename)) as fp:
            return json.load(fp)

    def test_invalid_1_empty(self):
        spec = self._load("invalid_1_empty.json")
        # ValidationError: 'hardware' is a required property
        self.assertRaises(jsonschema.exceptions.ValidationError, validate, spec, self.schema)

    def test_invalid_2(self):
        spec = self._load("invalid_2.json")
        # ValidationError: '' is not of type 'object'
        # validate(spec, self.schema)
        self.assertRaises(jsonschema.exceptions.ValidationError, validate, spec, self.schema)

    def test_invalid_3(self):
        spec = self._load("invalid_3.json")
        # ValidationError: 'os' is a required property on instance 'hardware': {}
        # validate(spec, self.schema)
        self.assertRaises(jsonschema.exceptions.ValidationError, validate, spec, self.schema)

    def test_valid_1(self):
        spec = self._load("valid_1.json")
        # Shouldn't raise an exception
        print(spec)
        validate(spec, self.schema)
        # self.assertRaises(jsonschema.exceptions.ValidationError, validate, spec, self.schema)

    def test_valid_2(self):
        spec = self._load("valid_2.json")
        # Shouldn't raise an exception
        print(spec)
        validate(spec, self.schema)
        # self.assertRaises(jsonschema.exceptions.ValidationError, validate, spec, self.schema)

if __name__ == '__main__':
    unittest.main()
