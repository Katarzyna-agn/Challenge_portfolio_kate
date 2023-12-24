import unittest
from unittest.loader import TestLoader

from test_cases.login_page_header_name_TC01 import TestLoginPage01
from test_cases.login_to_the_system_TC02 import TestLoginPage02
from test_cases.remind_password_TC03 import TestLoginPage03
from test_cases.change_language_TC04 import TestLoginPage04
from test_cases.dashboard_header_name_TC05 import TestDashboard01
from test_cases.dashboard_addplayer_TC06 import TestDashboard02
from test_cases.fill_add_player_form_all_TC07 import TestAddPlayer01



def full_suite():
    test_suite = unittest.TestLoader()
    login_page_header_name_test = test_suite.loadTestsFromTestCase(TestLoginPage01)
    login_to_the_system_test = test_suite.loadTestsFromTestCase(TestLoginPage02)
    remind_password_test = test_suite.loadTestsFromTestCase(TestLoginPage03)
    change_language_test = test_suite.loadTestsFromTestCase(TestLoginPage04)
    dashboard_header_name_test = test_suite.loadTestsFromTestCase(TestDashboard01)
    dashboard_add_player_test = test_suite.loadTestsFromTestCase(TestDashboard02)
    fill_add_player_all_test = test_suite.loadTestsFromTestCase(TestAddPlayer01)

    return unittest.TestSuite([login_page_header_name_test, login_to_the_system_test, remind_password_test, change_language_test,dashboard_header_name_test, dashboard_add_player_test, fill_add_player_all_test])


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
