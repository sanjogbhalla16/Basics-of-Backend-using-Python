from flask import Flask, jsonify, request

app = Flask(__name__)

#use of Postman to test these CRUD operations

items =[]

#CRUD operations

#1. Read(Retrieve all items)
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({'items': items})

#2. Read(Retrieve single item)
#This approach is efficient because it stops as soon as it finds the first matching item, 
#rather than continuing to search through the entire list
@app.route('/items/<string:name>', methods=['GET'])
def get_single_item(name):
    item = next((i for i in items if i["name"] == name), None)
    if item:
         return jsonify({'item': item})
    return jsonify ({ 'message': 'Item not found'}),404


#3. Create(Add a new item)
@app.route('/items', methods=['POST'])
def create_item():
    #get the data from the json
    data = request.get_json()
    item = {'name':data['name'],'price':data['price']}
    items.append(item)
    return jsonify({'item':item}),201


# Update(Update the existing item)
@app.route('/items/<string:name>', methods=['PUT'])
def update_item(name):
    #get the data from the api to put in the item
    data = request.get_json()
    #get the item from the items list
    item = next((i for i in items if i["name"] == name), None)
    if item:
        item['price'] = data['price']
        return jsonify({'item':item})
    return jsonify( { 'message': 'Item not found'}),404

# Delete(Delete an item)
@app.route('/items/<string:name>', methods=['DELETE'])
def delete_item(name):
    #Since we're going to modify the list, we need to reference the global items variable in this function. 
    #Otherwise, Python would treat it as a local variable.
    global items
    #makes a new list leaving that one item
    items = [i for i in items if i["name"] != name]
    return jsonify({'message': f'Item {name} deleted'})



# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    