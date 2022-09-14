from flask import Flask,redirect,url_for,render_template,request
from phone import parse_number

app = Flask(__name__)


@app.route("/",methods=["POST","GET"])
def get_num():
    if request.method == "POST":
        num = request.form["nm"]
        return redirect(url_for("display_number",number = num))
    else:
        return render_template("number.html")

@app.route("/<number>")
def display_number(number):
    a = number
    result = parse_number(number)
    print(result[0])
    print(result[1])
    return f"<h1>Country : {result[0]}</h1><h1>Service Provider : {result[1]}</h1>"


if __name__=="__main__":
    app.run(debug=True)