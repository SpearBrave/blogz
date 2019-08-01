from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"]= "mysql+pymysql://blogz:bbb@localhost:3306/blogz"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
app.secret_key = "bbb"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(120), unique= True)
    password= db.Column(db.String(120))
    blogs = db.relationship("Blog", backref = "owner")
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Blog(db.Model):

    id =   db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    body = db.Column(db.String(300))
    owner_id= db.Column(db.Integer,db.ForeignKey("user.id"))
 
    def __init__(self, name,body,owner):
        
        self.name = name
        self.body = body
        self.owner= owner



@app.route("/")
def index():
    all_users =  User.query.filter_by(username=user)
    render_template("home_page.html",all_users)







@app.before_request
def require_login():
    allowed_routes = ["login", "register","blog","index"]
    if request.endpoint not in allowed_routes and  "user" not in session:
        return redirect('/login') 


@app.route("/login", methods = ["POST", "GET"])
def login():

    user_error= ""
    password_error=""
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        exist_user = User.query.filter_by(username=user)
        
        
        if not exist_user :
            user_error= "user does not exist"
            return render_template("login.html", user_error =user_error)

        if  exist_user.password == password
            password_error = "password is wrong"

            return render_template("login.html", password_error=password_error)

        if exist_user and User.password:
            session["user"] = user
            return redirect('/new_post')
        
    return render_template("login.html")




  


@app.route("/register" , methods = ["POST", "GET"])
def register(): 
    
    if request.method == "POST":
        user= request.form["username"]
        password = request.form["password"]
        verify = request.form["verify"]
        user_error =""
        pass_error =""
        verify_error=""
        existing_user = User.query.filter_by(username=user).first()
        if existing_user:
            user_error = "username already exist"
        if len(password)<3:
            pass_error = "password should be (3>)long"
        if len(user)<3: 
            user_error = "username should be (3>)"
        if verify != password:
            verify_error= "verify and password dont match" 

        if user_error or pass_error or verify_error  :
            return render_template("register.html",user_error=user_error,pass_error=pass_error,verify_error=verify_error)
        else:   
            new_user = User(user,password)
            db.session.add(new_user)
            db.session.commit()
            session["user"] = user # remember user
            return redirect("/new_post")
       


    return render_template("register.html")





@app.route("/blog" )
def mainblog ():
    blog_id = request.args.get("id")  #gets id number
    if blog_id :
        single = Blog.query.get(blog_id)
        return render_template("individual_blog.html",blog=single) #uses single blogs info
    blogs = Blog.query.all()
    
    return render_template("all_post.html",)

    return render_template("todos.html",blogs=blogs)






@app.route("/new_post",methods=["POST","GET"])
def new_post():
    owner = User.query.filter_by(username=session['username'])
    if request.method == "POST": 
        Title = request.form["Title"] #takes the input from form.html   #*** line 52 ***
        Body = request.form["body"]   # same                            #*** line 52 *
        errorTitle= ""
        errorBody= ""
        exist_user = User.query.filter_by(username=user)
        if Title == "" :
            errorTitle = "error no chracters"
    
        if Body == "":
            errorBody= "error no characters"
        if errorTitle or errorBody :
            return render_template("new_blog_input.html", error=errorTitle,error=errorBody,owner)
            
        new_blog = Blog(name,Body,owner) 
        
        db.session.add(new_blog)    #  git bash
        db.session.commit()            
        blog_id= new_blog.id #takes the blogs id 
    
        return render_template("new_blog_input.html") # adds the link to the blog_id with concatenation
    return redirect("individual_blog.html")


@app.route ( "/logout")
def logout():
    del session["user"] 
    return redirect("/blog")

if __name__ == "__main__":

app.run()

