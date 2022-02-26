#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import render_template, request
import joblib

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        purchases = request.form.get("purchases")
        suppcard = request.form.get("suppcard")
        print(purchases, suppcard)
        purchases = float(purchases)
        suppcard = float(suppcard)
        
        model1 = joblib.load("CCU_Reg")
        pred1 = model1.predict([[purchases, suppcard]])
        s1 = "The score of credit card upgrade based on Regression is: " + str(pred1)
        
        model2 = joblib.load("CCU_DT")
        pred2 = model2.predict([[purchases, suppcard]])
        s2 = "The score of credit card upgrade based on Decision Tree is: " + str(pred2)
        
        model3 = joblib.load("CCU_NN")
        pred3 = model3.predict([[purchases, suppcard]])
        s3 = "The score of credit card upgrade based on Neural Network is: " + str(pred3)
        
        model4 = joblib.load("CCU_RF")
        pred4 = model4.predict([[purchases, suppcard]])
        s4 = "The score of credit card upgrade based on Random Forest is: " + str(pred4)
        
        model5 = joblib.load("CCU_GB")
        pred5 = model5.predict([[purchases, suppcard]])
        s5 = "The score of credit card upgrade based on Gradient Boosting is: " + str(pred5)
        
        return(render_template("index.html", result1 = s1, result2 = s2, result3 = s3, result4 = s4, result5 = s5))
    else:
        return(render_template("index.html", result1 = "", result2 = "", result3 = "", result4 = "", result5 = ""))


# In[ ]:


if __name__ == "__main__":
    app.run(host="127.0.0.1", port = int("1111"))


# In[ ]:




