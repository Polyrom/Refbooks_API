import json

from django.urls import reverse
from rest_framework.test import APITestCase


class ReferenceBookTests(APITestCase):
    fixtures = ['refbooks.json',
                'refbook_versions.json',
                'refbook_elements.json']

    EXPECTED_ELEMENTS = {
        'elements': [
            {
                'code': 'T-3',
                'value': 'Test disease 3'
            },
            {
                'code': 'T-4',
                'value': 'Test disease 4'
            }
        ]
    }

    def test_get_refbooks(self):
        url = reverse('refbooks')
        response = self.client.get(url)
        refbook1 = response.data['refbooks'][0]
        refbook2 = response.data['refbooks'][1]
        self.assertEqual(refbook1['code'], 'MS-1')
        self.assertEqual(refbook2['name'], 'ICD-10 name')

    def test_get_refbooks_by_date(self):
        url = reverse('refbooks')
        response = self.client.get(url, {'date': '2022-12-02'})
        refbook1 = response.data['refbooks'][0]
        refbook2 = response.data['refbooks'][1]
        self.assertEqual(len(response.data['refbooks']), 2)
        self.assertEqual(refbook1['code'], 'MS-1')
        self.assertEqual(refbook2['code'], 'ICD-10')

    def test_get_elements(self):
        url = reverse('elements', kwargs={'pk': 1})
        response = self.client.get(url)
        expected_data = json.dumps(self.EXPECTED_ELEMENTS)
        self.assertEqual(json.dumps(response.data), expected_data)

    def test_get_elements_by_version(self):
        url = reverse('elements', kwargs={'pk': 1})
        response = self.client.get(url, {'version': '1.1'})
        expected_data = json.dumps(self.EXPECTED_ELEMENTS)
        self.assertEqual(json.dumps(response.data), expected_data)

    def test_check_element(self):
        url = reverse('check', kwargs={'pk': 1})
        params = {'code': 'T-3', 'value': 'Test disease 3'}
        response = self.client.get(url, params)
        self.assertTrue(response.data)

    def test_check_element_by_version_exist(self):
        url = reverse('check', kwargs={'pk': 1})
        params = {'code': 'T-1', 'value': 'Test disease 1', 'version': '1.0'}
        response = self.client.get(url, params)
        self.assertTrue(response.data)

    def test_check_element_by_version_absent(self):
        url = reverse('check', kwargs={'pk': 1})
        params = {'code': 'T-3', 'value': 'Test disease 3', 'version': '1.0'}
        response = self.client.get(url, params)
        self.assertFalse(response.data)
