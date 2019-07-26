import datetime
import email.message
import smtplib
import configparser
from win10toast import ToastNotifier

def dtnow():
    return datetime.datetime.now()


def getConfigValue(group, key):
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config[group][key]


def get_real_number(number_str):
    CHR_REPLC01 = "第"
    CHR_REPLC02 = "話"
    real_num = 0
    
    number_str = number_str.replace(CHR_REPLC01, "").replace(CHR_REPLC02, "")

    number_str_dec = float(number_str) % 1
    real_num = int(number_str) if number_str_dec == 0 else float(number_str)

    return real_num


def notificar_w10toast(title, body):

    toaster = ToastNotifier()
    toaster.show_toast(
        title,
        body,
        icon_path=getConfigValue("PATHS", "NOTIFICACCION_ICO"),
        threaded=True,
        duration=30)


def sed_mail(asunto, email_emisor, email_emisor_pwd, email_receptor, body):
    is_sended = True
    try:
        SUBJECT = asunto
        FROM_ADDR = email_emisor
        FROM_ADDR_PASS = email_emisor_pwd
        TO_ADDR = email_receptor

        msg = email.message.Message()
        msg["Subject"] = SUBJECT
        msg["From"] = FROM_ADDR
        msg["To"] = TO_ADDR
        msg.add_header('Content-Type','text/html')
        msg.set_payload(body)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # mail server ip
        server.login(FROM_ADDR, FROM_ADDR_PASS)
        server.sendmail(msg["from"],msg["To"].split(";"), msg.as_string().encode('utf-8').strip())
        server.set_debuglevel(1)
        server.quit()
    except Exception as ex:
        is_sended = False
        print(ex)
        raise ex

    return is_sended

