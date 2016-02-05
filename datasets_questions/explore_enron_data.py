#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
POI=0
for key in enron_data:
  try:
    f=float(enron_data[key]["email_address"])
  except ValueError:
    continue
  else:
    if(~math.isnan(f)):
      POI=POI+1
print (POI)
total=0
for key in enron_data:
  total=total+1
print total
print total-POI
# print (enron_data["LAY KENNETH L"]["total_payments"])
# print enron_data["FASTOW ANDREW S"]["total_payments"]
# print enron_data["SKILLING JEFFREY K"]["total_payments"]
# for key in enron_data:
#   if key=="PRENTICE JAMES":
#     for subkey in enron_data[key]:
#       print (subkey)+" "
