from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route('/list')
def index():
    user =  {'username': '©realHikkan'}
    cert_list = [
      {"CN": "inhavk", "Validity_Not_After": "Dec 24 11:45:48 2020 GMT", "Valid": True},
      {"CN": "batyash", "Validity_Not_After": "Dec 25 13:33:25 2028 GMT", "Valid": False},
      {"CN": "shun.kazani", "Validity_Not_After": "May 27 03:33:25 2019 GMT", "Valid": False}]
    return render_template('list.html', title='Home', user=user, cert_list=cert_list)

if __name__ == "__main__":
    app.run(host='localhost')