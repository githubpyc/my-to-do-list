from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        

        self.assertIn('To-Do List', self.browser.title)

        head_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do Lists', head_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_tablelist('1: Buy peacock feathers')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy one get one free')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_tablelist('2: Buy one get one not free')

        self.fail('Test is finished')

    def check_for_row_in_tablelist(self, item_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(item_text, [row.text for row in rows])


if __name__ == '__main__':
    unittest.main(warnings='ignore')

