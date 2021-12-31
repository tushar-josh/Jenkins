from seleniumbase import BaseCase

class HomeTest(BaseCase):
    def test_home_page(self):
        self.open("https://www.google.com/")
        self.assert_title("Google")
    def test_home_page(self):
        self.open("https://www.google.com/")
        self.assert_title("Googleee")