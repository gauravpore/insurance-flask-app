
from flask import jsonify, request
from bson import json_util
import json





class InsuranceRepo:

    def calculate_premium_amount(mongo_db:any,ages,city_tier, sum_insured=None, tenure=None):
        query  = { "Age": { "$in" : ages }, "TierID":city_tier, "SumInsured":sum_insured,"Tenure":tenure}
        db_data = mongo_db.db.insurance.find(query)
       
        json_docs = []
        for doc in db_data:
            print(type(doc))
            json_doc = json.loads(json_util.dumps(doc))
            json_docs.append(json_doc)
        if len(json_docs) == 1:
            rate = json_docs[0].get("Rate")
            final_total = rate//2
        else:
            discount_total_amount = 0
            higest_age = max(ages)
            highest_age_member_rate = 0
            for entry in json_docs:
                if entry.get("Age") != higest_age:
                    base_rate = entry.get("Rate")
                    discount_amount = base_rate/2
                    discount_total_amount += discount_amount
                else:
                    highest_age_member_rate = entry.get("Rate")
            final_total = highest_age_member_rate + discount_total_amount
        response = {"final_total":final_total}
        return True,response