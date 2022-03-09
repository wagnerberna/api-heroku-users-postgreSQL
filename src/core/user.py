from unicodedata import normalize
from src.model.login import LoginModel
import re

login_model = LoginModel()


class UserCore:
    def check_login(self, login):
        if login_model.find_login(login):
            return True
        return False

    def check_mail(self, email):
        regex = '^[a-z0-9.]+@[a-z0-9]+\.[a-z]+(\.[a-z]+)?$'
        if re.search(regex, email):
            return True
        return False

    def payload_clean_field(self, field):
        clean_field = field.lower().strip()
        clean_field = normalize('NFKD', clean_field).encode('ASCII', 'ignore').decode('utf-8')
        return clean_field

    def payload_new_and_update_user(self, name, age, email, city, login, password, description, activated=False):
        clean_name = self.payload_clean_field(name)
        clean_email = self.payload_clean_field(email)
        clean_city = self.payload_clean_field(city)
        clean_login = self.payload_clean_field(login)
        clean_description = self.payload_clean_field(description)

        payload = {
            'name': clean_name,
            'age': age,
            'email': clean_email,
            'city': clean_city,
            'login': clean_login,
            'password': password,
            'description': clean_description,
            'activated': activated,
        }
        return payload

    def payload_get_user(self, user_id, name, email, login, password, activated, age, description, city):

        payload = {
            'user_id': user_id,
            'name': name,
            'age': age,
            'email': email,
            'city': city,
            'login': login,
            'password': '******',
            'description': description,
            'activated': activated,
        }
        print('---core payload:::', payload)
        return payload


if __name__ == '__main__':
    user_core = UserCore()
    print(user_core.check_mail('teste@gmail.com'))
    print(user_core.check_mail('teste@gmail.com.br'))
    print(user_core.check_mail('testegmail.com'))
    print(user_core.check_mail('teste@gmail'))
    print(user_core.check_mail('tes$?@gmail.com'))
