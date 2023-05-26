from flask import Flask
from flask_pymongo import PyMongo
from flask import jsonify, request
from bson import json_util
import json
from flask_cors import cross_origin
from calculate import InsuranceRepo

app = Flask(__name__)


app.config[
    "MONGO_URI"
] = "mongodb+srv://gforce:zmxncbv@cluster0.mrswx8k.mongodb.net/gforce"

mongo = PyMongo(app, ssl=True)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/calculate-premium/", methods=["POST"])
@cross_origin()
def get_premium():
    request_data = request.json
    print(request_data)
    ages = request_data.get("age")
    sum_insured = request_data.get("sum_insured")
    city_tier = request_data.get("city_tier")
    tenure = request_data.get("tenure")
    if not ages or not sum_insured or not city_tier or not tenure:
        # Return Invalid Prams response
        pass
    success, response = InsuranceRepo.calculate_premium_amount(
        mongo_db=mongo, ages=ages, city_tier=1, sum_insured=sum_insured, tenure=tenure
    )
    if not success:
        pass
    return response


if __name__ == "__main__":
    app.run(debug=True)
