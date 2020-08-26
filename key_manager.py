import configparser
from cryptography.fernet import Fernet

class Cypher(object):
    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__config.read('keys.ini')

    def encrypt(self, val):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
            
        f = Fernet(key)
        encoded = f.encrypt(str(val).encode())
        self.__config['auth']={
            'token': encoded.decode('utf-8')
        }
        
        with open('keys.ini', 'w') as configfile:
            self.__config.write(configfile)
        
       
    def get_auth(self):
        try:
            token = self.__config.get('auth', 'token').encode()
            key = open("secret.key", "rb").read()
            f = Fernet(key)
            return f.decrypt(token).decode('utf-8')
            
        except:
            return None
