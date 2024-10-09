## Build URL Dynamically
## Variable Rules
## Jinja 2 Template Engine

'''
{{}} expressions to print output in html
{% %} conditions, for loop
{# #} comments
'''


from flask import Flask, render_template,request,redirect,url_for

'''
It creates an instance of the Flask class, which will be our WSGI(Web Server Gateway Interface) application.
'''
# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the Flask app!</h1></html>"

@app.route("/index",methods = ['GET'])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form",methods = ['GET','POST'])
def handle_form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template("form.html")

# Variable Rule
@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score < 50:
        res = "You failed!"
    else:
        res = "You passed!"

    return render_template('result.html', result = score)

@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score >= 50:
        res = "You failed!"
    else:
        res = "You passed!"

    exp = {'score':score, 'result':res}

    return render_template('result1.html', result = exp)

# if condition
@app.route("/successif/<int:score>")
def successif(score):
    return render_template('result.html', result = score)


@app.route("/fail/<int:score>")
def fail(score):
    return render_template('result.html', result = score)

@app.route("/submit", methods = ['GET','POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['Science'])
        maths = float(request.form['Maths'])
        c = float(request.form['C'])
        total_score = float((science + maths + c)/3)
    else:
        return render_template('getresult.html')
    return redirect(url_for('success', score = total_score))


if __name__ == "__main__":
    app.run(debug=True)