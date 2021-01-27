
import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt


#EMPTY LISTS FOR TARGET VALUES
dates = []   
prices = []

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader) # skip the first row, since its column names
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))

    return

def predict_prices(dates, prices, x):       # FUNCTION RUNNING FOR 3 SEPERATE MODELS
    dates = np.reshape(dates,(len(dates), 1))

    svr_lin = SVR(kernel='linear', C=1e-3)
    svr_poly = SVR(kernel='poly', C=1e-3, degree = 2)
    svr_rbf = SVR(kernel='rbf', C=1e-3, gamma=0.1)

    #FITTING AND TRAINING THE MODELS WITH TARGET VALUES
    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)

    
    #CREATING THE PLOT FOR EACH MODELS WITH CORESPONDING COLORS
    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF Model')
    plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear Model')
    plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial Model')

    
    #LABELING THE PLOT
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regressior aka SVR')
    plt.legend()
    plt.show()

    #PREDICTING THE NEW VALUES
    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

get_data('AAPL.csv')    # YOUR STOCK HISTORY PRICE FILE LOCATION

predicted_price = predict_prices(dates, prices, 30)

print(predicted_price)

