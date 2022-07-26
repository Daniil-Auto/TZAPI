from conftest import *
from api.diskapi import *

class TestYandex(object):
    def test_create_folder(self,path='SimbirSoftFolder'):
        loging()
        create_folder(path = path)
        get_info_folder(path= path)
        delete_folder(path= path)