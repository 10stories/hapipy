import random
import unittest

import simplejson as json
from nose.plugins.attrib import attr

import helper
from hapi.settings import SettingsClient

class SettingsClientTest(unittest.TestCase):
    """ Unit tests for the HubSpot Settings API Python client.

    This file contains some unittest tests for the Settings API.

    Docs: http://docs.hubapi.com/wiki/Settings_API

    Questions, comments: http://docs.hubapi.com/wiki/Discussion_Group
    """

    def setUp(self):
        self.client = SettingsClient(**helper.get_options())

    def tearDown(self):
        pass

    @attr('api')
    def test_get_settings(self):
        # Get all settings, a lengthy list typically.
        settings = self.client.get_settings()
        self.assertTrue(len(settings))

        print "\n\nGot some settings: %s" % json.dumps(settings)

    @attr('api')
    def test_get_setting(self):
        # Get a specific named setting.
        name = 'test_name'
        settings = self.client.get_setting(name)
        self.assertTrue(len(settings))

        print "\n\nGot a specific setting: %s, giving %s" % (name, json.dumps(settings));

    @attr('api')
    def test_add_setting(self):
        # Add or update a specific setting.
        data = { 'name': 'test_name', 'value': 'test_value' }
        result = self.client.update_setting(data)
        # This is just a 201 response (or 500), no contents.

        print "\n\nUpdated setting: %s." % data['name']

    @attr('api')
    def test_delete_setting(self):
        # Deletes a specific setting, emptying out its value.
        name = 'test_name'
        settings = self.client.delete_setting(name)
        # This is just a 201 response (or 500), no contents.

        print "\n\nDeleted setting: %s." % name

if __name__ == "__main__":
    unittest.main()
