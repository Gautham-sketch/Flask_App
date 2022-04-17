from flask import Flask,jsonify,request

app = Flask(__name__)
contacts=[
    {
        "Contact_no" : "9987644456",
        "Name" : u"Raju",
        "id" : 1,
        "done" : False
    },
    {
        "Contact_no" : "9987644456",
        "Name" : u"Rahul",
        "id" : 2,
        "done" : True
    },
    {
        "Contact_no" : "9987644456",
        "Name" : u"Priya",
        "id" : 3,
        "done" : True
    },
    {
        "Contact_no" : "9987644456",
        "Name" : u"Usha",
        "id" : 4,
        "done" : False
    },
]

@app.route("/add-data", methods = ["POST"])

def addTask():
    if not request.json:
        return jsonify({
            "Satatus" : "error",
            "Message" : "Please provide the data !"
        },404)
    contact = {
        "Contact_no" : request.json.get("Contact",''),
        "Name" : request.json['Name'],
        "id" : contacts[-1]['id'] +1,
        "done" : False
    }
    contact.append(contacts)
    return jsonify({
        "Status" : "Success",
        "Message" : "Contact added successfully !"
    })