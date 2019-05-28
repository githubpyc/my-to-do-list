from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.http import HttpResponse
from lists.models import Item

class homePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text':'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        first_item = Item.objects.first()
        self.assertEqual(first_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text':'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        save_items = Item.objects.all()
        self.assertEqual(save_items.count(), 2)

        first_save_item = save_items[0]
        second_save_item = save_items[1]
        self.assertEqual(first_save_item.text, 'The first (ever) list item')
        self.assertEqual(second_save_item.text, 'Item the second')
        
    def text_only_save_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_display_all_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/')
        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())