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
        # Frank sees an explanation of the application
        # above an input form.
        form = self.driver.find_element_by_id('zipcodeForm')

        # Frank enters his zip code into the input form.
        form.send_keys('76209')

        # Frank hits submit.
        form.submit()

        # Frank is directed to a page that shows his senators
        # and his representatives.
        self.assertTrue('Kenny Marchant' in self.driver.page_source)
        self.assertTrue('Michael C. Burgess' in self.driver.page_source)

    def test_user_can_get_information_on_a_rep(self):
        # Frank can click on the name of any of the legislators
        # for more information on them.
        self.fail("Finish the test.")

        # Frank clicks on his senator's name.

        # Frank sees some biographical information as well as
        # some information about his rep's position.
