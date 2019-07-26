from OPMWebComic import OPMWebComic, OPMWebComicBDActions
from CommonActions import (
    sed_mail,
    dtnow,
    get_real_number,
    notificar_w10toast,
    getConfigValue)

# from pprint import pprint

def main():
    opmwc = OPMWebComic()
    opmwc_bd_act = OPMWebComicBDActions()
    webc_lista_capitulos = opmwc.get_lista_capitulos()
    now = dtnow()
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
            arr_nuevos_capitulos.append(cap_numero)

    if len(arr_nuevos_capitulos) > 0:
        notificar_w10toast(arr_nuevos_capitulos)


if __name__ == "__main__":
    # main()
    sed_mail(
        "asunto sin importacia OPM WC 01",
        getConfigValue("MAIL", "EMAIL_EMISOR"),
        getConfigValue("MAIL", "EMAIL_EMISOR_PWD"),
        getConfigValue("MAIL", "EMAIL_RECEPTOR"),
        "Cuerpo de OPM WC !!")