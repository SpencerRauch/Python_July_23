from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "No secrets on github"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html')  # Return the string 'Hello World!' as a response

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    # if request.method == "POST":
    #     pass #treat this like a post request
    # else:
    #     pass #treat this like a get
    session['name'] = request.form['name']
    session['region'] = request.form['region']
    session['calories_per_serving'] = request.form['calories_per_serving']
    return redirect('/display')
    # return render_template("display.html",name=name) #this is Bad!

@app.route('/display')
def display():
    if 'region' in session:
        region = session['region']
    else:
        region = "not supplied"
    return render_template("display.html",region=region)

#redirect on any action route
@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.