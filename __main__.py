from OPMWebComic import OPMWebComic
from pprint import pprint

def main():
    opmwc = OPMWebComic()
    pprint(opmwc.get_lista_capitulos())
    # pprint(opmwc.lista_capitulos_html)
    # pprint(opmwc.cantidad_capitulos)


if __name__ == "__main__":
    main()