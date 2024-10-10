from flask import Flask
from flask_restful import Api, Resource

Api = Api(app)
app = Flask(__name__) # It creates a new Flask application instance and sets it up. Let's break down what this line does
#is a special Python variable that holds the name of the current module.
#When you pass __name__ to Flask(), it tells the Flask framework where the application is defined (i.e., the module name).

fakeDatabase = {
    1:{'name':'Clear Car'},
    2:{'name':'Write Blog'},
    3:{'name':'start stream'},
}



@app.route('/')
def Hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)

"""
__name__ allows Flask to determine the location of your application, 
and this is useful when Flask tries to find templates and static files relative to your project.
If you run this file directly (e.g., python app.py), the value of __name__ will be "__main__",
and Flask will know that this script is the starting point of the application.
"""
















