### Author - Gaurav Pore ###

from flask import jsonify, request
from bson import json_util

import json


class InsuranceRepo:
    @staticmethod
    def calculate_premium_amount(
        mongo_db: any, ages: list, city_tier: int, sum_insured: int, tenure: int
    ):
        """
        This method queries collection document from hosted Mongo database
        and calculates the premium amount based on given input params.
        Params:
            - mongo_db -> Instance of Mongo Db client
            - ages -> List of integers containing ages of family memebers
            - city_tier -> Tier ID for city (1 or 2)
            - tenure -> tenure for insurance
        Returns:
            - success, response
        """

        if (
            type(ages) != list
            or type(city_tier) != int
            or type(sum_insured) != int
            or type(tenure) != int
        ):
            return False, "Invalid data type for parameters"

        try:
            query = {
                "Age": {"$in": ages},
                "TierID": city_tier,
                "SumInsured": sum_insured,
                "Tenure": tenure,
            }

            # fetching desired rows data
            db_data = mongo_db.db.insurance.find(query)

            json_docs = []
            for doc in db_data:
                json_doc = json.loads(json_util.dumps(doc))
                json_docs.append(json_doc)

            if len(json_docs) == 1:
                # for single individual | discount 50%
                rate = json_docs[0].get("Rate")
                final_total = rate / 2
            else:
                # finding member with highest age to exclude from discount logic
                discount_total_amount = 0
                higest_age = max(ages)
                highest_age_member_rate = 0
                for entry in json_docs:
                    if entry.get("Age") != higest_age:
                        base_rate = entry.get("Rate")
                        discount_amount = base_rate / 2
                        discount_total_amount += discount_amount
                    else:
                        highest_age_member_rate = entry.get("Rate")
                final_total = highest_age_member_rate + discount_total_amount
            response = {"final_total": final_total}
            success = True
        except Exception as error:
            print(error)
            response = "Something went wrong while calculating premium amount"
            success = False
        return success, response
