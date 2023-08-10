from data import db

def start(message):
    if not db.getUsersExist(message.from_user.id):
        text = '''
Xush kelibsiz! Iltimos, ismingizni bilsam bo'ladimi?
'''
        return text
    text = '''
Salom! Bugun sizga qanday yordam bera olaman?
'''
    return text

class register:

    def userNameError(message):
        text = f'''
Siz ismni noto'g'ri kiritganga o'xshaysiz. Iltimos, yana urinib ko'ring.
'''
        return text

    def sendContact(message):
        text = f'''
Iltimos, telefon raqamingizni yuborish uchun quyidagi tugmani bosing.
'''
        return text
    
    def registerSuccess(message):
        text = '''
Ajoyib! Sizning ro'yxatdan o'tishingiz muvaffaqiyatli yakunlandi.
'''
        return text

def help(message):
    text = '''
ADM invest Treyding maktabi
Forex / Kripto treyding
⠀
Professionallardan soha sirlarini mukammal o’rganing 🚀
30% nazariy 70% amaliyot
⠀
📞 +998 88 220 50 00
'''
    return text

def signUp(message):
    text = '''
Kursga arizangiz muvaffaqiyatli yuborildi 📘✨
'''
    return text

def signUpSend(message):
    userName = db.select('userId', message.from_user.id, 'users', 'userName')
    userPhone = db.select('userId', message.from_user.id, 'users', 'userPhone')
    text = f'''
Ism: {userName}
Nomer: {userPhone}
'''
    return text