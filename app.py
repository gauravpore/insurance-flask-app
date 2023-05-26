### Author - Gaurav Pore ###

from flask import Flask, jsonify, request

from flask_pymongo import PyMongo
from flask_cors import cross_origin

from calculate import InsuranceRepo

app = Flask(__name__)


app.config[
    "MONGO_URI"
] = "mongodb+srv://gforce:zmxncbv@cluster0.mrswx8k.mongodb.net/gforce?tlsAllowInvalidCertificates=true"

mongo = PyMongo(app)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/calculate-premium/", methods=["POST"])
@cross_origin()
def get_premium():
    """
    Endpoint to calculate premimum amount for given parameters
    """
    request_data = request.json
    print(request_data)
    ages = request_data.get("age")
    sum_insured = request_data.get("sum_insured")
    city_tier = request_data.get("city_tier")
    tenure = request_data.get("tenure")
    if not ages or not sum_insured or not city_tier or not tenure:
        error_response = {"code": 400, "message": "Invalid Parameters"}
        return jsonify(error_response), 400
    success, response = InsuranceRepo.calculate_premium_amount(
        mongo_db=mongo, ages=ages, city_tier=1, sum_insured=sum_insured, tenure=tenure
    )
    if not success:
        error_response = {"code": 400, "message": response}
        return jsonify(error_response), 400
    success_response = {
        "code": 200,
        "response": response,
        "message": "Premimum amount calculated successfully",
    }
    return jsonify(success_response), 200


if __name__ == "__main__":
    # setting this for production
    app.run(debug=False)
