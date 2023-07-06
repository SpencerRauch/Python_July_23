from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

list = ['bob','alex','steve']

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World! Seriously, hello!'  # Return the string 'Hello World!' as a response

@app.route('/greeting/<name>')
def greeting(name):
    return f'<h1>Welcome, {name}</h1>'

@app.route('/get_user/<int:index>')
def get_user(index):
    # index = int(index) another way of accomplishing this
    return list[index]

@app.route('/template')
def show_temp():
    return render_template("index.html")


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,port=5050,host="0.0.0.0")    # Run the app in debug mode