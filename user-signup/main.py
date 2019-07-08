from flask import Flask, request, redirect, render_template
import re


app + Flask(__name__)

app.config['DEBUG'] = True

@app.route('/',method=["GET"])
           

def apple():

    return render_template("index.html")
@app.route('/',method=["POST"])

def pear():
    input_username =request.form["username"]
    input_password =request.form["password"]        
    input_confirmationP = request.form["verify"]
    input_email = request.form["email"]
   
    erroruser=""        
    errorpassword=""
    verifyP=""        
    erroremail=""
    


    if  re.search(" ", input_username):
        erroruser= "No Spaces!"
    
    elif len(input_username) > 20 or len(input_username) <3:
    
        erroruser="3-20 characters !"
    

    



    
    if  re.search(" ", input_password):
        error_password= "No Spaces!"
   
    elif len(input_password) > 20 or len(input_password) <3:
        error_password= "3-20 character !"


    
   
    
    
    
    
    if input_confirmationP != input_password:
        verifyP="Does not match !"

   



    


    if not re.search("^[A-Z][a-z]@.", input_email):
        erroremail= "must contain @ or . "
    
   
    elif re.search(" "):
        erroremail= "no spaces !"
    elif len(input_email) > 20 or len(input_email) <3:
        erroremail= "3- 20"
  

    

    return render_template("index.html",user_error=erroruser,pass_error=errorpassword,verify_error_=verifyP,email_error=erroremail)

app.run()