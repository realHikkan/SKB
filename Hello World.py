from flask import Flask, render_template
from certificate import Certificate
app = Flask(__name__)

@app.route("/")
@app.route('/list')
def index():
    user =  {'username': '©realHikkan'}
    cert_list = [
      Certificate("inhavk", "Dec 24 11:45:48 2020 GMT", "True"),
      Certificate("batyash", "Dec 25 13:33:25 2028 GMT", "False"),
      Certificate( "shun.kazani", "May 27 03:33:25 2019 GMT", "False"),
      Certificate("ilia", "May 27 03:33:25 2020 GMT", "True")]
    return render_template('list.html', title='Home', user=user, cert_list=cert_list)

if __name__ == "__main__":
    cert = Certificate("inhavk", "Dec 24 11:45:48 2020 GMT", "True")

    cn = cert.get_common_name()
    Validity_Not_After = cert.get_date()
    valid = cert.get_valid()

    print(cn)
    print(Validity_Not_After)
    print(valid)

    app.run(host='localhost')