from flask import Flask,request
from flask_restful import Api, Resource

#for flask_restful the syntax is different 

items = []

app = Flask(__name__)
api = Api(app) # It creates a new Flask application instance and sets it up. Let's break down what this line does
#is a special Python variable that holds the name of the current module.
#When you pass __name__ to Flask(), it tells the Flask framework where the application is defined (i.e., the module name).
"""
__name__ allows Flask to determine the location of your application, 
and this is useful when Flask tries to find templates and static files relative to your project.
If you run this file directly (e.g., python app.py), the value of __name__ will be "__main__",
and Flask will know that this script is the starting point of the application.
"""

#Resource Class for CRUD operations
class Item(Resource):
    #Read (Retrieve)
    def get(self,name):
        item = next((i for i in items if i['name'] == name),None)
        return {'item': item}, 200 if item else 404
    
    #Create
    def post(self,name):
        item = next((i for i in items if i['name'] == name),None)
        if item:
            return {'message': f"Item with name '{name}' already exists."}, 400
        
        data = request.get_json()
        item = {'name':name,'price':data['price']}
        items.append(item)
        return item,201
    
    #Update
    def put(self,name):
        #get the data
        data = request.get_json()
        item = next((i for i in items if i['name'] == name),None)
        if item:
             item['price'] = data['price']
             return item,200
        else:
            item = {'name':name, 'price':data['price']}
            items.append(item)
            return item,201
        
        # Delete
    def delete(self, name):
        global items
        items = [item for item in items if item['name'] != name]
        return {'message': f"Item '{name}' deleted."}, 200


# Add the resource and define the endpoint
api.add_resource(Item, '/item/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)















