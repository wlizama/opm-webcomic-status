from OPMWebComic import OPMWebComic, OPMWebComicBDActions
from CommonActions import (
    sed_mail,
    dtnow,
    get_real_number,
    notificar_w10toast,
    getConfigValue)

# from pprint import pprint
NOW = dtnow()

def main():
    opmwc = OPMWebComic()
    opmwc_bd_act = OPMWebComicBDActions()
    webc_lista_capitulos = opmwc.get_lista_capitulos()
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
                NOW)

            # agregar a array para envio de notificación
            arr_nuevos_capitulos.append(cap_numero)

    if len(arr_nuevos_capitulos) > 0:
        arr_notf_caps = [str(scap) for scap in arr_nuevos_capitulos]
        str_caps = ",".join(arr_notf_caps)

        str_body_notf = "Salió un nuevo capítulo de OPM Webcomic 😱 cap: %s" % str_caps
        if len(arr_notf_caps) > 1:
            str_body_notf = "Han salido nuevos capítulos de OPM Webcomic 😱 caps: %s" % str_caps

        asunto = "Notificación OPM WC, nuevos capítulos"
        body_mail = """Ha salido un nuevo capitulo de OPM WC
        <br>
        Dirección de enlace: %s
        """ % opmwc.URL
        for nuevo_capitulo in arr_nuevos_capitulos:
            body_mail = "%s<br>- Capítulo nro. %s<br>" % (body_mail, nuevo_capitulo)

        is_sended = sed_mail(
            "%s  😱 %s" % (asunto, NOW),
            getConfigValue("MAIL", "EMAIL_EMISOR"),
            getConfigValue("MAIL", "EMAIL_EMISOR_PWD"),
            getConfigValue("MAIL", "EMAIL_RECEPTOR"),
            body_mail)

        if is_sended:
            notificar_w10toast(asunto, str_body_notf)
            


if __name__ == "__main__":
    main()