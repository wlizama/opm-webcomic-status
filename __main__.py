from OPMWebComic import OPMWebComic, OPMWebComicBDActions
from pprint import pprint

def main():
    opmwc = OPMWebComic()
    opmwca = OPMWebComicBDActions()
    pprint(opmwc.get_lista_capitulos())
    opmwca.init_tables()
    # pprint(opmwc.lista_capitulos_html)
    # pprint(opmwc.cantidad_capitulos)


if __name__ == "__main__":
    main()