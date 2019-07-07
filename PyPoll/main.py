import os
import csv

os.chdir(os.path.dirname(__file__))
total = 0


Py_roll = os.path.join("Resources/election_data.csv")

with open(Py_roll) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        total +=1
    print ("Total Votes:" + str(total))

    candidate_name = row[2]
    print (candidate_name)
  


     
        





    