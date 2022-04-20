from crypt import crypt
from unicodedata import normalize
from src.model.login import LoginModel
from src.service.passwords import crypt_password
import re
from src.model.dto.userDto import UserDtoAdd, UserDtoUpdate

login_model = LoginModel()


class UserCore:
    def payload_clean_field(self, field):
        clean_field = field.lower().strip()
        clean_field = (
            normalize("NFKD", clean_field).encode("ASCII", "ignore").decode("utf-8")
        )
        return clean_field

    def payload_new_user(self, new_user):

        payload = UserDtoAdd(
            name=self.payload_clean_field(new_user.name),
            age=new_user.age,
            email=self.payload_clean_field(new_user.email),
            city=self.payload_clean_field(new_user.city),
            login=self.payload_clean_field(new_user.login),
            password=crypt_password(new_user.password),
            description=self.payload_clean_field(new_user.description),
            activated=new_user.activated,
        )
        return payload

    def payload_update_user(self, update_user):

        payload = UserDtoUpdate(
            name=self.payload_clean_field(update_user.name),
            age=update_user.age,
            email=self.payload_clean_field(update_user.email),
            city=self.payload_clean_field(update_user.city),
            description=self.payload_clean_field(update_user.description),
            activated=update_user.activated,
        )
        return payload


# if __name__ == "__main__":
#     user_core = UserCore()
