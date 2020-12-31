from flask import *
import re


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/",methods=['GET', 'POST'])
def pro():
    if request.method == 'POST':
        text=request.form["userinput"]
        if request.form.get("wcount"):
            forward_message=len(text.split())
        elif request.form.get("uniquewords"):
            s2=",".join(set(re.split('[,\s]\s*',text.lower())))
            forward_message=s2
        elif request.form.get("titletext"):
            forward_message=text.title()
    return render_template("index.html", forward_message=forward_message)


if __name__=="__main__":
    app.run(debug=True)
