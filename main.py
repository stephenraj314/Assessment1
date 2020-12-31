from flask import *
import re
#using regex for multidelimiter split()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/",methods=['GET', 'POST'])
def func():
    if request.method == 'POST':
        text=request.form["userinput"]
        if request.form.get("wcount"):
            message=len(text.split())
        elif request.form.get("uniquewords"):
            #using split to seprate words in string and using set() to find unique words
            s2=",".join(set(re.split('[,\s]\s*',text.lower())))
            message=s2
        elif request.form.get("titletext"):
            #using title() to convert first letters to capital letters
            message=text.title()
    return render_template("index.html", message=message)


if __name__=="__main__":
    app.run(debug=True)
