"""
    Bundesnetzagentur: Ladesäulenregister

    API des Ladesäulenregisters der Bundesnetzagentur  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.ladestationen.model.station_overview_attributes import (
    StationOverviewAttributes,
)

from deutschland import ladestationen

globals()["StationOverviewAttributes"] = StationOverviewAttributes
from deutschland.ladestationen.model.station_overview_features import (
    StationOverviewFeatures,
)


class TestStationOverviewFeatures(unittest.TestCase):
    """StationOverviewFeatures unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStationOverviewFeatures(self):
        """Test StationOverviewFeatures"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StationOverviewFeatures()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
