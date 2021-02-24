from app.forms import *

class RegisterForm(Form):
    email = StringField("Email", 
    validators=[validators.Email(message="Please enter a valid email address")])
    password = PasswordField("Password", validators=[validators.Length(min=3, max=25), 
    validators.DataRequired(message="Please Fill This Field")])
    fname = StringField("First Name", validators=[validators.Length(min=3, max=25), 
    validators.DataRequired(message="Please Fill This Field")])
    lname = StringField("Last Name", validators=[validators.Length(min=3, max=25), 
    validators.DataRequired(message="Please Fill This Field")])
    username = StringField("Username", validators=[validators.Length(min=3, max=25), 
    validators.DataRequired(message="Please Fill This Field")])