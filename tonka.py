from flask import Flask, render_template, request, url_for
import requests


app=Flask("MyApp")


@app.route("/")
def get_main_page():
    return render_template("tonka.html")




if __name__MyApp == '__main__':
    app.run()