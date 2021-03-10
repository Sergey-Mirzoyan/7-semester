from os.path import isfile, basename, splitext
from os import listdir
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
SMTP_HOST = ["smtp.mail.ru", 25]


# Отправка текстового письма

# Поиск файлов содержащих ключевое слово в текущей директории
def find(keyword):
    if keyword == '':
        return

    keyword_files = []

    for filename in listdir("."):
        if not isfile(filename) or splitext(filename)[1].lower() != '.txt':
            continue
        with open(filename) as file:
            file_data = file.read()
            if keyword in file_data:
                keyword_files.append(filename)

    return keyword_files


# Прикрепление файлов к письму
def attach_files_to_mime(mime, key_files):
    for filename in key_files:
        with open(filename, 'rb') as file:
            part = MIMEApplication(file.read(), Name=basename(filename))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(filename)
        mime.attach(part)


# Заполнение полей письма
def fill_mime(from_address, to_address, msg_subject, msg_text, filenames):
    mime = MIMEMultipart()
    mime['From'] = from_address
    mime['To'] = to_address
    mime['Subject'] = msg_subject
    mime.attach(MIMEText(msg_text, 'plain'))
    attach_files_to_mime(mime, filenames)
    return mime


# Отправка письма с вложениями
def send_mime_mail(mime, smtp_host, from_address, password):
    server = smtplib.SMTP(smtp_host[0], smtp_host[1])
    server.starttls()
    server.login(from_address, password)
    server.sendmail(mime['From'], mime['To'], mime.as_string())
    server.quit()

def main():
    global TO, FROM, PAS, SUBJ, MSG, KEY
    TO = input("Адрес получателя: ")
    FROM = input("Адрес отправителя: ")
    PAS = input("Пароль: ")
    SUBJ = input("Тема: ")
    MSG = input("Сообщение: ")
    KEY = input("Ключевое слово для поиска файла: ")
    key_filenames = find(KEY)
    mime = fill_mime(FROM, TO, SUBJ, MSG, key_filenames)
    send_mime_mail(mime, SMTP_HOST, FROM, PAS)

main()
