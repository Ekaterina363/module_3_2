def check_mail(mail):
    list_ = (".com", ".ru", ".net")
    check = "@"     #["@",".com", ".ru", ".net"]
    return check in mail and mail.endswith(list_)

def send_email (message, recipient, sender = "university.help@gmail.com"):
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif check_mail(recipient) and check_mail(sender):
        if sender != "university.help@gmail.com":
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru")
            print(message, "Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com")
    else:
        print("Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru")
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')






