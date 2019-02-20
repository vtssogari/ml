# Choosing the right model, layer activation and loss function

### From book "Deep Learning with Python"

| Problem Type                            | Last Layer Activation | Loss function             |
| ---------------------                   |-----------------------|---------------            |
| Binary classification                   | sigmoid               | binary_crossentropy       |
| Multiclass, single-label classification | softmax               | categorical_crossentropy  |
| Multiclass, multilabel classification   | sigmoid               | binary_crossentropy       |
| Regression to arbitray values           | None                  | mse                       |
| Regression to values between 0 and 1    | sigmoid               | mse or binary_crossentropy|
