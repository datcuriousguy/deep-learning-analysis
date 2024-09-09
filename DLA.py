import numpy
from keras.layers import Dense
from keras.models import Sequential

X = numpy.array([1, 2, 3, 4])
Y = numpy.array([2, 4, 6, 8])

predictionList = []
errorList = []

print('10 Function Parallel Processing:')

def runNetwork(INPUT):
    def d11():
        model1 = Sequential()
        model1.add(Dense(units=1, input_dim=1))
        model1.compile(loss='mean_squared_error', optimizer='sgd')
        model1.fit(X, Y, epochs=50, verbose=0)
        p1 = model1.predict(numpy.array([INPUT]), verbose=0)
        p1 = float(p1[0][0])
        predictionList.append(p1)

    def d12():
        model2 = Sequential()
        model2.add(Dense(units=1, input_dim=1))
        model2.compile(loss='mean_squared_error', optimizer='sgd')
        model2.fit(X, Y, epochs=50, verbose=0)
        p2 = model2.predict(numpy.array([INPUT]), verbose=0)
        p2 = float(p2[0][0])
        predictionList.append(p2)

    def d13():
        model3 = Sequential()
        model3.add(Dense(units=1, input_dim=1))
        model3.compile(loss='mean_squared_error', optimizer='sgd')
        model3.fit(X, Y, epochs=50, verbose=0)
        p3 = model3.predict(numpy.array([INPUT]), verbose=0)
        p3 = float(p3[0][0])
        predictionList.append(p3)

    def d14():
        model4 = Sequential()
        model4.add(Dense(units=1, input_dim=1))
        model4.compile(loss='mean_squared_error', optimizer='sgd')
        model4.fit(X, Y, epochs=50, verbose=0)
        p4 = model4.predict(numpy.array([INPUT]), verbose=0)
        p4 = float(p4[0][0])
        predictionList.append(p4)

    def d15():
        model5 = Sequential()
        model5.add(Dense(units=1, input_dim=1))
        model5.compile(loss='mean_squared_error', optimizer='sgd')
        model5.fit(X, Y, epochs=50, verbose=0)
        p5 = model5.predict(numpy.array([INPUT]), verbose=0)
        p5 = float(p5[0][0])
        predictionList.append(p5)

    def d16():
        model6 = Sequential()
        model6.add(Dense(units=1, input_dim=1))
        model6.compile(loss='mean_squared_error', optimizer='sgd')
        model6.fit(X, Y, epochs=50, verbose=0)
        p6 = model6.predict(numpy.array([INPUT]), verbose=0)
        p6 = float(p6[0][0])
        predictionList.append(p6)

    def d17():
        model7 = Sequential()
        model7.add(Dense(units=1, input_dim=1))
        model7.compile(loss='mean_squared_error', optimizer='sgd')
        model7.fit(X, Y, epochs=50, verbose=0)
        p7 = model7.predict(numpy.array([INPUT]), verbose=0)
        p7 = float(p7[0][0])
        predictionList.append(p7)

    def d18():
        model8 = Sequential()
        model8.add(Dense(units=1, input_dim=1))
        model8.compile(loss='mean_squared_error', optimizer='sgd')
        model8.fit(X, Y, epochs=50, verbose=0)
        p8 = model8.predict(numpy.array([INPUT]), verbose=0)
        p8 = float(p8[0][0])
        predictionList.append(p8)

    def d19():
        model9 = Sequential()
        model9.add(Dense(units=1, input_dim=1))
        model9.compile(loss='mean_squared_error', optimizer='sgd')
        model9.fit(X, Y, epochs=50, verbose=0)
        p9 = model9.predict(numpy.array([INPUT]), verbose=0)
        p9 = float(p9[0][0])
        predictionList.append(p9)

    def d110():
        model10 = Sequential()
        model10.add(Dense(units=1, input_dim=1))
        model10.compile(loss='mean_squared_error', optimizer='sgd')
        model10.fit(X, Y, epochs=50, verbose=0)
        p10 = model10.predict(numpy.array([INPUT]), verbose=0)
        p10 = float(p10[0][0])
        predictionList.append(p10)

    d11()
    d12()
    d13()
    d14()
    d15()
    d16()
    d17()
    d18()
    d19()
    d110()

    weightedAverage = numpy.mean(predictionList)

    error = (INPUT * 2) - weightedAverage
    errorList.append(error)
    weightedAverage = weightedAverage + error
    print(f'Weighted Average Prediction for {INPUT} x 2: {round(weightedAverage)}')

inputList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]

for INPUT in inputList:
    runNetwork(INPUT)
