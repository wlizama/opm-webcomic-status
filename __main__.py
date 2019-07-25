from OPMWebComic import OPMWebComic, OPMWebComicBDActions
import datetime
from pprint import pprint


def get_real_number(number_str):
    CHR_REPLC01 = "第"
    CHR_REPLC02 = "話"
    real_num = 0
    
    number_str = number_str.replace(CHR_REPLC01, "").replace(CHR_REPLC02, "")

    number_str_dec = float(number_str) % 1
    real_num = int(number_str) if number_str_dec == 0 else float(number_str)

    return real_num


def main():
    opmwc = OPMWebComic()
    opmwc_bd_act = OPMWebComicBDActions()
    webc_lista_capitulos = opmwc.get_lista_capitulos()
    now = datetime.datetime.now()
    arr_nuevos_capitulos = []

    """ Buscar si capítulo no existe en BD
    """
    for webc_capitulo in webc_lista_capitulos:
        html, content_tag_href, content_string, query_string, params = webc_capitulo.values()
        cap_numero = get_real_number(content_string)
        exist_cap = opmwc_bd_act.select_capitulo_by('numero', cap_numero)
        if not exist_cap:
            # print("El capítulo %s no existe en BD, es nuevo 😱 !!!" % cap_numero)

            # agregar a BD
            opmwc_bd_act.add_capitulo(
                cap_numero,
                content_string,
                "Capítulo ubicado en %s" % content_tag_href,
                now)

            # agregar a array para envio de notificación
            arr_nuevos_capitulos.append({
                "cap_numero" : cap_numero,
                "nombre": content_string,
                "full_url" : "%s%s" % (opmwc.URL, content_tag_href)
            })

    print(arr_nuevos_capitulos)

if __name__ == "__main__":
    main()