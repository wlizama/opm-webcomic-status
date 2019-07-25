from OPMWebComic import OPMWebComic, OPMWebComicBDActions
import datetime
from win10toast import ToastNotifier

from pprint import pprint


def get_real_number(number_str):
    CHR_REPLC01 = "第"
    CHR_REPLC02 = "話"
    real_num = 0
    
    number_str = number_str.replace(CHR_REPLC01, "").replace(CHR_REPLC02, "")

    number_str_dec = float(number_str) % 1
    real_num = int(number_str) if number_str_dec == 0 else float(number_str)

    return real_num


def notificar_w10toast(arr_capitulos):

    arr_notf_caps = [str(scap) for scap in arr_capitulos]
    str_caps = ",".join(arr_notf_caps)

    str_body_notf = "Salió un nuevo capítulo de OPM Webcomic 😱 cap: %s" % str_caps
    if len(arr_notf_caps) > 1:
        str_body_notf = "Han salido nuevos capítulos de OPM Webcomic 😱 caps: %s" % str_caps

    toaster = ToastNotifier()
    toaster.show_toast(
        "Notificación OPM WC capítulos!",
        str_body_notf,
        icon_path=None,
        threaded=True,
        duration=30)


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
            arr_nuevos_capitulos.append(cap_numero)

    if len(arr_nuevos_capitulos) > 0:
        notificar_w10toast(arr_nuevos_capitulos)


if __name__ == "__main__":
    main()