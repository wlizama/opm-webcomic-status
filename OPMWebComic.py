import requests
from bs4 import BeautifulSoup
import re

class OPMWebComic:
    
    URL = "http://galaxyheavyblow.web.fc2.com"


    def __init__(self):
        self.__web_html_tree = None
        self.__lista_capitulos = []
        self.__is_obj_setted = False
    

    @property
    def web_html_tree(self):
        return self.__web_html_tree

    
    @property
    def lista_capitulos(self):
        return self.__lista_capitulos

    @property
    def is_obj_setted(self):
        return self.__is_obj_setted


    def __init_web_html_tree(self):
        response = requests.get(self.URL)
        soup = BeautifulSoup(response.content, "html.parser")
        self.__web_html_tree = soup


    def __init_lista_capitulos(self):
        lista_capitulos = self.web_html_tree.find_all(
            "a",
            attrs={"href": re.compile(r"/fc2-imageviewer/\?aid=\d&iid=\d")}
        )
        self.__lista_capitulos = lista_capitulos


    def set_obj(self):
        self.__init_web_html_tree()
        self.__init_lista_capitulos()
        self.__is_obj_setted = True


    def print_lista_captitulos_html(self):
        if not self.is_obj_setted:
            self.set_obj()

        whtmltree = self.web_html_tree
        link_list = whtmltree.find_all(
            "a",
            attrs={"href": re.compile(r"/fc2-imageviewer/\?aid=\d&iid=\d")}
        )
    
        for link in link_list:
            print(link)