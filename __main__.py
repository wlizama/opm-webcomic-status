from OPMWebComic import OPMWebComic, OPMWebComicBDActions
from pprint import pprint

def main():
    opmwc = OPMWebComic()
    opmwc_bd_act = OPMWebComicBDActions()
    webc_lista_capitulos = opmwc.get_lista_capitulos()

    """ Buscar si capitulo no existe en BD
    """
    for webc_capitulo in webc_lista_capitulos:
        html, content_tag_href, content_string, query_string, params = webc_capitulo.values()
        iid_cap = params['iid'][0]
        exist_cap = opmwc_bd_act.select_capitulo_by('numero', iid_cap)
        if not exist_cap:
            print("El capitulo %s no existe en BD, es nuevo 😱 !!!" % content_string)
            opmwc_bd_act.add_capitulo(
                iid_cap,
                content_string,
                "Capítulo ubicado en %s" % content_tag_href)


if __name__ == "__main__":
    main()