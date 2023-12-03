import unittest

from unittest.loader import makeSuite
from unittest.loader import TestLoader

import self

# from test_cases.fill_in_a_form import TestFillInaForm
# from test_cases.framework import Test
from test_cases.login_to_the_system_TC01 import TestLoginPage
from test_cases.remaind_password_TC02 import TestLoginPage
from test_cases.change_language_TC03 import TestLoginPage
from test_cases.dashboard_addplayer_TC04 import TestDashboard
from test_cases.fill_add_player_form_req_TC05 import TestAddPlayer
from test_cases.fill_add_player_form_all_TC06 import TestAddPlayer


def full_suite(self):
    test_suite = unittest.TestSuite()
    unittest.TestLoader.loadTestsFromTestCase(self,testCaseClass=TestLoginPage)
    unittest.TestLoader.loadTestsFromTestCase(self,testCaseClass=TestDashboard)
    unittest.TestLoader.loadTestsFromTestCase(self,testCaseClass=TestAddPlayer)
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite(self))
