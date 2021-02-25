from app import *
from app.models.user import User
from flask_login import login_user, login_manager
from flask_login import LoginManager
from app.forms import loginForm, registerForm

login_manager= LoginManager()
login_manager.init_app(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/main')
def main():
    return render_template("main.html")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=["GET","POST"])
def register():
    form = registerForm.RegisterForm (request.form)
    if request.method== "POST" and form.validate():
        try:
            user = User(
                username = form.username.data,
                email = form.email.data,
                fname = form.fname.data,
                lname = form.lname.data,
                password = form.password.data
            )
            db.session.add(user)
            db.session.commit() 
            flash("Yipee! you've registered successfully...!","success")
            return redirect("/login")
        except Exception as e:
            print("Failed to register.")
            print(e)
    return render_template("register.html", form = form)


@app.route('/login',methods=["GET","POST"])
def login():
    form = loginForm.LoginForm(request.form)
    if request.method== "POST" and form.validate():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username = form.username.data).first()
        if user and password == user.password: 
            login_user(user)
            return redirect('/')
        else:
            flash('Invalid Credentials','warning')
            return redirect('/login')
        
    return render_template("login.html", form = form)