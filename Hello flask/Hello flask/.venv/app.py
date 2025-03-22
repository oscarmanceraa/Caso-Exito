import re
import lineaRegLin
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/hello2')
def hello():
    return "¡Hola, mundo!"

@app.route("/hello/<name>") #url + parametro en la url 
def hello_there(name):
    now = datetime.now() #acceder a la hora actual
    formatted_now = now.strftime("%A, %d %B, %Y at %X") # esta reescribiendo reseteando - string from time
    
    match_object = re.match("[a-zA-Z]+", name)# expresiones regulares
    
    if match_object :
        clean_name = match_object.group(0)
    else:
        clean_name = "friend"
        
    content = f"hello there {clean_name},  | the date is: {formatted_now}"
    return content

@app.route("/")
def helloHTML():
    return render_template("index.html")

@app.route("/calc", methods=["GET", "POST"])
def calcular():
    
    result = None
    
    if request.method == "POST":
        hours = float(request.form['hours'])
        result = lineaRegLin.calculate_grade(hours)

    return render_template("calcGrades.html", result=result)
