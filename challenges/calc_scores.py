# The attached file contains information about anonymous students and their calculus scores for Calculus I and Calculus II.
# Use the scikit-learn library to perform a linear regression using ordinary least squares method. According to the
# regression, what is the predicted Calculus II score for a student who scored a 97% in Calculus I?

from sklearn import linear_model

reg = linear_model.LinearRegression()

import csv

with open('regressive_math_scores.csv') as f:
    all_scores = []
    for line in f:
        scores = line.split('/')
        if len(scores) < 3:
            continue
        # s = [scores[1], scores[2]]
        all_scores.append(scores)

    reg.fit(all_scores, [0, 1, 2])

