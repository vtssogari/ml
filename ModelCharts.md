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

