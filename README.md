# 🔹Insurance premium calculator (Backend)
### Author: Gaurav Pore


## 🔸Overview:
Flask app that serves an API endpoint ```https://insurance-flask-app.onrender.com/calculate-premimum``` configured with live mongo database in order to calculate premium amount on provided parameters like age, sum_insured, tenure, etc.

## 🔸**Tools & Technologies:**
- Python 3
- [Flask](https://www.djangoproject.com/start/)
- [MongoDB](https://www.mongodb.com/docs/)
- [PyMongo](https://pymongo.readthedocs.io/en/stable/)
- [Postman API Platform](https://learning.postman.com/docs/getting-started/introduction/)
- Requests
- Git 
- VS Code

### 🔸**API overview:**
```
/calculate-premimum -> Returns json response consisting of final total amount calculated on basis on input params. (age, tenure, sum_insured, city_tier).
```
> **🔸Installation Guide:**
- To install all requirements/packages:
```
pip install -r requirements.txt
```
- To run the application on local Port 5000:
```
flask run
```
or
```
python3 app.py
```
### 🔸Refer to the postman collection here --> [collection link](https://github.com/gauravpore/insurance-flask-app/blob/master/Insurance%20Flask%20API.postman_collection.json)
You can directly download and import the collection into postman and test the API.
