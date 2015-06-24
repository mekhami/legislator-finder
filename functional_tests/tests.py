from django.test import LiveServerTestCase
from selenium import webdriver


class FinderTest(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.live_server_url)

    def tearDown(self):
        self.driver.close()

    def test_user_enters_zip_code(self):
        # Frank visits the index of the application
        self.fail("Finish the test.")

        # Frank sees an explanation of the application
        # above an input form.

        # Frank enters his zip code into the input form.

        # Frank hits submit.

        # Frank is directed to a page that shows his senators
        # and his representatives.

    def test_user_can_get_information_on_a_rep(self):
        # Frank can click on the name of any of the legislators
        # for more information on them.
        self.fail("Finish the test.")

        # Frank clicks on his senator's name.

        # Frank sees some biographical information as well as
        # some information about his rep's position.
