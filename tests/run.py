import os
import sys
import unittest

TEST_TARGETS = [
    'irolink_default_test',
    'irolink_list_test',
    'irolink_detail_test',
    'irolink_static_test',
    'irolink_api_image_test',
    'irolink_utils_color_convert_test',
]


def suite():
    suite = unittest.TestSuite()
    for testmodule in TEST_TARGETS:
        exec 'from ' + testmodule + ' import suite as _suite'
        suite.addTests(_suite())
    return suite
