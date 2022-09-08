from flask import Flask,request,jsonify,render_template
from flask_cors import cross_origin
app = Flask(__name__)
#from "./util" import load_model
import util

@app.route('/')
def hello_world():
    
    return render_template("index.html")

@app.route("/get_location")
def get_location():
    print("...get request.....")
    response = jsonify({'location':util.get_location()})
    response2 = jsonify({'location':"hello"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
    
@app.route("/get_price",methods=["POST"])  
@cross_origin() 
def price():
    print("...get request....",request.form)
    total_sqft = float(request.form["total_sqft"])
    location = str(request.form["location"])
    bath = int(request.form["bath"])
    balcony = int(request.form["balcony"])
    area_type = str(request.form["area_type"])
    size = int(request.form["size"]) 
    response = jsonify({'price':util.predict(size,total_sqft,bath,balcony,area_type,location)})
    
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    print("running app")
    app.run(debug=False,host="0.0.0.0")