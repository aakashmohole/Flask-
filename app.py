from flask import Flask,redirect,url_for

### WSGI Application
app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to my Flask Web by aakash"


@app.route('/members')
def members():
    return "Welcome to my world"

@app.route('/success/<int:score>')
def success(score):
    return '<html><body><h1>The Person is Pass </h1></body></html>'
 
 
@app.route('/fail/<int:score>')
def fail(score):
    return 'The person is failed by markes: '+str(score)



## Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks<50:
        result = 'fail'
    else: 
        result = 'success'
    #return result
    return redirect(url_for(result, score = marks))



if __name__ =='__main__':
    app.run(debug=True)