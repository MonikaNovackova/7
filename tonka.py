from flask import Flask, render_template, request, url_for
import requests


app=Flask("MyApp")

def send_simple_message(sendTo_mail,sendTo_name):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxf144e75fa05a4582bd674ba3d4b9552e.mailgun.org/messages",
        auth=("api","a9e3e2e98ea33f459e6a616f62ea179b-acb0b40c-6f225c23"),
        data={"from": "Very excited User Monika monika.novac@gmail.com",
        "to": [sendTo_mail,sendTo_name],
        "subject":"Hello "+sendTo_name,
 
        "html":'<b>hello there.</b>  ' + ' <h1>Monika Novackova</h1>'
        })



@app.route("/research")
def get_research_page():
    return render_template("research.html")

@app.route("/index")
def get_main_page():
    return render_template("index.html")

@app.route("/teaching")
def get_teaching_page():
    return render_template("teaching.html")

@app.route("/programming")
def get_programming_page():
    return render_template("programming.html")



@app.route("/signup2", methods=["POST"])
def sign_up():
    form_data=request.form
    print (form_data["email"])
    return "All ok. Your email is:"+ form_data["email"]



@app.route("/signup", methods=["POST"])
def returnhome():
    form_data=request.form
    v_email=form_data["email"]
    send_simple_message(sendTo_mail=form_data["email"],sendTo_name=form_data["name"])
    return render_template("programming.html",v_email=v_email)



app.run(debug=True)