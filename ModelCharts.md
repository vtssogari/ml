# Choosing the right model, layer activation and loss function

### From book "Deep Learning with Python"

| Problem Type                            | Last Layer Activation | Loss function             | metrics                  | Optimizer |
| ---------------------                   |-----------------------|---------------            |-------                   | ----------|
| Binary classification                   | sigmoid               | binary_crossentropy       | binary_accuracy, acc     | adam |
| Multiclass, single-label classification | softmax               | categorical_crossentropy  | categorical_accuracy, acc| adam |
| Multiclass, multilabel classification   | sigmoid               | binary_crossentropy       | categorical_accuracy, acc| adam |
| Regression to arbitray values           | None                  | mse                       | mse, mae, mape           | adam |
| Regression to values between 0 and 1    | sigmoid               | mse or binary_crossentropy| mse, mae, mape           | adam |


Activation Types: reul, sigmoid, tanh
Optimizer: adam, sgd, rmsprop, etc


Use SGD+Nesterov for shallow networks, and either Adam or RMSprop for deepnets.

| Optimizer | Description | more | Advantages | example | note |
|-----------|-------------|------|------------|---------|------|
| adam | Adaptive moment estimation | Adam = RMSprop + Momentum | Relatively low memory requirements (though higher than gradient descent and gradient descent with momentum) Usually works well even with little tuning of hyperparameters. |Adam(lr=0.001) | for deepnets |
| rmsprop | | | |  |for deepnets|
| sgd  | Stochastic gradient descent | SGD + Nesterov enabled | works well for shallow networks |SGD(lr=0.01, nesterov=True) |  for shallow networks |
|adagrad | || well-suited for dealing with sparse data. don’t need to tune the learning rate manually. | | 
|adaDelta| ||  tends to remove the decaying learning Rate problem of it ||
