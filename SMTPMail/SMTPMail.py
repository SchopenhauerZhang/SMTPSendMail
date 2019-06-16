#!/usr/bin/env python
import smtplib

# 外部函数库 谁用谁添加


class SMTPMail:
    __user = 'Schopenhauerzhang@icloud.com'
    __pwd = ''
    __sendMail = 'Schopenhauerzhang@icloud.com'
    __receiver_mail = 'Schopenhauerzhang@icloud.com'

    def __init__(self):
        self.__smtp_obj = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
        self.__login(self.__user, self.__pwd)

    def __login(self, user, pwd):
        if user and pwd:
            self.__smtp_obj.login(user, pwd)
        else:
            self.__smtp_obj.login(self.__user, self.__pwd)

    def login(self, user, pwd):
        self.__login(user, pwd)

    def get_sender(self, send_mail):
        if send_mail:
            self.__sendMail = send_mail

    def get_receiver(self, receiver_mail):
        if receiver_mail:
            if isinstance(receiver_mail, list):
                self.__receiver_mail = ','.join(str(s) for s in receiver_mail)
            elif isinstance(receiver_mail, tuple):
                self.__receiver_mail = ','.join(str(s) for s in receiver_mail)
            elif isinstance(receiver_mail, dict):
                self.__receiver_mail = ','.join(str(s) for s in receiver_mail.values())
            else:
                self.__receiver_mail = receiver_mail

    def send_mail(self, message):
        self.__smtp_obj.sendmail(self.__sendMail, self.__receiver_mail, message.as_string())



