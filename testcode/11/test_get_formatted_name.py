from unittest import TestCase
from name_function import get_formatted_name

class TestGet_formatted_name(TestCase):
    def test_get_formatted_name(self):
        #self.fail()
        """能够正确地处理像Janis Joplin这样的姓名吗？ """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
