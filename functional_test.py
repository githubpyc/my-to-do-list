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

        head_text = self.browser.find_element_by_tag_name('h1').head_text
        self.assertIn('To Do', head_text)

        inputbox = self.browser.find_element_by_tag_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys_ENTER)
        sleep(1)

        table = self.browser.get_element_by_tag_id('id_new_table')
        rows = table.find_element_by_tag_name('tr')

        self.assertTrue(
            any(row.text == 'Buy peacock feathers' for row in rows)
        )

        self.fail('Test is finished')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

