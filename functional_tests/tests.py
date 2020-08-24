from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()
        
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
        
    def test_can_start_a_CV_for_one_user(self):
        #Alice has heard about a new online CV app. She goes to check out its home page.
        self.browser.get(self.live_server_url)
        
        #She follows the CV link in the top menu header
        self.browser.get('http://localhost:8000/cvedit')

        #She notices the page title and a URL mention CV editor
        self.assertIn('CV', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('CV', header_text)
        
        
        #She is invited to enter her name straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your name'
        )
        
        #She types "Alice" into a text box
        inputbox.send_keys('Alice')

        #When she presses enter, the page updates and she sees her name in the form.
        inputbox.send_keys(Keys.ENTER) 
        self.wait_for_row_in_list_table('1: Alice')
        
        #There is another text box inviting her to input her surname. She inputs Smith
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Smith')
        inputbox.send_keys(Keys.ENTER)
        
        #The page updates again showing both items.
        self.wait_for_row_in_list_table('1: Alice')
        self.wait_for_row_in_list_table('2: Smith')

        #Satisfied, she leaves the site to return at a later date.
        
    def test_multiple_users_can_start_CVs_at_different_URLs(self):
        # Alice starts a new to-do list
        self.browser.get('http://localhost:8000/cvedit')
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Alice')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Alice')

        # She notices that her list has a unique URL
        alice_cv_url = self.browser.current_url
        self.assertRegex(alice_cv_url, '/cvedit/.+')
        ## We use a new browser session to make sure that no information
        ## of Alice's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        #Francis visits the home page.  There is no sign of Alice's
        # list
        self.browser.get('http://localhost:8000/cvedit')
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Alice', page_text)
        self.assertNotIn('Smith', page_text)
        
        # Francis starts a new list by entering a new item. He
        # is less interesting than Alice...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Francis')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Francis')
        
        # Francis gets his own unique URL
        francis_cv_url = self.browser.current_url
        self.assertRegex(francis_cv_url, '/cvedit/.+')
        self.assertNotEqual(francis_cv_url, alice_cv_url)
        # Again, there is no trace of Alice's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Alice', page_text)
        self.assertIn('Francis', page_text)

        #Finish the test.
        self.fail('Finish the test!')




