from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()
        
        
    def test_can_start_a_CV_for_one_user(self):
        #Alice has heard about a new online CV app. She goes to check out its home page.
        self.browser.get(self.live_server_url)
        
        #She follows the CV link in the top menu header
        self.browser.get('http://localhost:8000/cvedit/list')

        #She notices the page title and a URL mention CV editor
        self.assertIn('CV', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('CV', header_text)
        
        
        #She decides to create a new CV by following the link.
        self.browser.get('http://localhost:8000/cvedit/new')
        
        #She is invited to enter a title for her CV
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a title'
        )
        
        #She types Alice's CV into a text box
        inputbox.send_keys('Alice CV')
        
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
        
        #She goes back to the CV list and sees her CV.
        self.browser.get('http://localhost:8000/cvedit/list')
        new_header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Alice CV', new_header_text)
        
        #Satisfied, she leaves the site to return at a later date.
        
        self.fail('Finish the test!')




