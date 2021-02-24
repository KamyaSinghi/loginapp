from app.forms import *

class LoginForm(Form):
    username = StringField("Username", validators=[validators.Length(min=3, max=25),
     validators.DataRequired(message="Please Fill This Field")])
    password = PasswordField("Password", validators=[validators.Length(min=3, max=25),
     validators.DataRequired(message="Please Fill This Field")])