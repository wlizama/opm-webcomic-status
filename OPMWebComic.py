import requests
from bs4 import BeautifulSoup
import re
import urllib.parse as uparse
from BDManage import BDManage


class OPMWebComic:
    
    URL = "http://galaxyheavyblow.web.fc2.com"


    def __init__(self):
        self.__web_html_tree = None
        self.__lista_capitulos_html = []
        self.__is_obj_setted = False
        self.set_obj()
    

    @property
    def web_html_tree(self):
        return self.__web_html_tree

    
    @property
    def lista_capitulos_html(self):
        return self.__lista_capitulos_html


    @property
    def is_obj_setted(self):
        return self.__is_obj_setted

    
    @property
    def cantidad_capitulos(self):
        return len(self.lista_capitulos_html)


    def __init_web_html_tree(self):
        response = requests.get(self.URL)
        soup = BeautifulSoup(response.content, "html.parser")
        self.__web_html_tree = soup


    def __init_lista_capitulos_html(self):
        self.__lista_capitulos_html = self.web_html_tree.find_all(
            "a",
            attrs={"href": re.compile(r"/fc2-imageviewer/\?aid=\d&iid=\d")}
        )


    def set_obj(self):
        self.__init_web_html_tree()
        self.__init_lista_capitulos_html()
        self.__is_obj_setted = True


    def print_lista_capitulos_html(self):
        link_list = self.web_html_tree.find_all(
            "a",
            attrs={"href": re.compile(r"/fc2-imageviewer/\?aid=\d&iid=\d")}
        )
    
        for link in link_list:
            print(link)
    

    def get_lista_capitulos(self):
        lista_capitulos = []
        for listcap in self.lista_capitulos_html:
            href = listcap.get('href')
            url_parse = uparse.urlparse(href)
            query_string = url_parse.query
            params = uparse.parse_qs(query_string)
            lista_capitulos.append({
                'html': str(listcap),
                'content_tag_href': href,
                'content_string': listcap.string,
                'query_string': query_string,
                'params': params
            })
        return lista_capitulos


class OPMWebComicBDActions:
    
    def __init__(self):
        self.__objbdman = BDManage()


    @property
    def objbdman(self):
        return self.__objbdman


    def init_tables(self):
        self.objbdman.execute_sttmt("""CREATE TABLE IF NOT EXISTS CAPITULO (
            id_capitulo INTEGER PRIMARY KEY AUTOINCREMENT,
            numero NUMERIC NOT NULL,
            nombre VARCHAR(150) NOT NULL,
            descripcion VARCHAR(300)
            )""")


    def add_capitulo(self, numero, nombre, descripcion):
        self.objbdman.execute_insert("INSERT INTO CAPITULO VALUES (null, ?, ?, ?)",
            values=(
                numero,
                nombre,
                descripcion
            ))


    def select_capitulos(self):
        return self.objbdman.execute_select_all("SELECT * FROM CAPITULO")


    def select_capitulo_by(self, column_filter, value_to_find):
        return self.objbdman.execute_select_one("SELECT * FROM CAPITULO WHERE %s = '%s'" % (
            column_filter,
            value_to_find
        ))


    def delete_capitulos(self):
        return self.objbdman.execute_delete("DELETE FROM CAPITULO")

    
    def delete_capitulos_by(self, column_filter, value_to_find):
        return self.objbdman.execute_delete("DELETE FROM CAPITULO WHERE %s = '%s'" % (
            column_filter,
            value_to_find
        ))
    
