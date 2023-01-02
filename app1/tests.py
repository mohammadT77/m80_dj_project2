from django.test import TestCase

# Create your tests here.
from app1.utils import get_ip_info


class UtilsTest(TestCase):

    def test1_get_ip_info(self):
        res = get_ip_info("5.89.88.82")
        print(res)