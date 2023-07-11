from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key= "key"

@app.route('/')
def index():
    return render_template("index.html")



#action: where form will go when submitted
@app.route('/process', methods=['POST'])
#in the route that accepts it, we need to specify that it is listening for post request
def process():
    print(request.form)

    session['name'] = request.form['name'] 
    session['dojo_location'] = request.form['dojo_location'] 
    session['favorite_language'] = request.form['favorite_language'] 
    session['comments'] = request.form['comments'] 

    return redirect ('/result')


@app.route('/result')
def display():
    return render_template ("display.html")



if __name__=="__main__":
    app.run(debug=True)

