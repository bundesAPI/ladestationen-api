"""
    Bundesnetzagentur: Ladesäulenregister

    API des Ladesäulenregisters der Bundesnetzagentur  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.ladestationen.api.default_api import DefaultApi  # noqa: E501

from deutschland import ladestationen


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_query_get(self):
        """Test case for query_get

        Query für alle Ladesäulen  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
