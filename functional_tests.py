from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()
        
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
        
    def test_can_start_a_CV_and_retrieve_it_later(self):
        #Alice has heard about a new online CV app. She goes to check out its home page.
        self.browser.get('http://localhost:8000')
        
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
        time.sleep(1) 
        self.check_for_row_in_list_table('Name: Alice')
        
        #There is another text box inviting her to input her surname. She inputs Smith
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Smith')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        #The page updates again showing both items.
        self.check_for_row_in_list_table('Name: Alice')
        self.check_for_row_in_list_table('Surname: Smith')
   
        #Alice wonders whether the site will remember her details. Then she sees that the site has generated a uniques URL for her -- there is some explanatory text to that effect.
        self.fail('Finish the test!')
        #She visits that URL -her details are still there.

        #Satisfied, she leaves the site to return at a later date.

if __name__ == '__main__':
    unittest.main(warnings='ignore')


