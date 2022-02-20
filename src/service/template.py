from string import Template
from datetime import datetime


class ViewTemplate:
    def message(self, login_user, name_user, template_path):
        with open(template_path, 'r') as file:
            template = Template(file.read())
            date_now = datetime.now().strftime('%d/%m/%y')
            body_template = template.substitute(login=login_user, name=name_user, date=date_now)
            # print(body_template)
            return body_template

# if __name__ == '__main__':
    # template_path_test = 'src/template/template_confirm_mail.html'
    # ViewTemplate().message('Superman', 'Clark', template_path_test)
