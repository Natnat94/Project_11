import requests
import html


class ApiRetriever:
    """this class purpose is to retrieve the information from
        the OpenFoodFacts API it require one category argument"""

    url = 'https://fr.openfoodfacts.org/cgi/search.pl?'

    def __init__(self):
        self.data = None
        self.research = {'search_terms': '',
                         'search_simple': '1',
                         'action': 'process',
                         'json': '1',
                         'tagtype_0': 'categories',
                         'tag_contains_0': 'contains',
                         'tag_0': '',
                         'page_size': '250'}

    def get_data(self, category):
        """this method send a request to get the data
            researched from the API in JSON"""
        self.research['tag_0'] = category
        content = requests.get(self.url, params=self.research)
        self.data = content.json()
        datacleaner = DataCleaner()
        data = datacleaner.realcleaner(self.data)
        return data


class DataCleaner:
    """this class purpose is to clean the raw data received from the API"""

    def __init__(self):
        self.data2 = {}
        self.data_save = []

    def realcleaner(self, data):
        """This method role is to clean the data received from
            any useless information"""
        for c in data["products"]:
            if self.isvalid(c):
                continue
            else:
                self.data_save.append(self.data2.copy())
        return self.data_save

    def isvalid(self, product):
        """this method role is to check if all the information needed
            exist and return True if an error occur"""
        keys = ['brands',
                'categories',
                'url',
                'product_name_fr',
                'stores',
                'ingredients_text',
                'nutrition_grade_fr',
                'id',
                'image_front_url',
                'image_front_small_url',
                'nutriments']
        error = False
        self.data2 = {}
        for key in keys:
            data = product.get(key)
            if data:
                if product[key] == "":
                    error = True
                else:
                    value = product[key]
                    if key == "image_front_small_url":
                        value = value.replace('200.jpg', '100.jpg')
                    elif key == "image_front_url":
                        value = value.replace('400.jpg', 'full.jpg')
                    elif key == "nutriments":
                        pass
                    else:
                        value = value.replace('\n', ' ')
                        value = value.replace("_", "")
                    self.data2[key] = html.unescape(value)
            else:
                error = True
        return error
