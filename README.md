**What is SimpleBMI Module**

A simple python module used to calcualte the BMI score and BMI Status based on the individual heights and weights.

**Installation**

```
python3 -m pip install simplebmi-test --index-url=https://test.pypi.org/simple
```


**Example**

```
from simplebmi_test import simplebmi

bmi_score, bmi_status = simplebmi.generate_bmi_data({"height": 1.6 , "weight": 53})

print(f"BMI Score : {bmi_score}, BMI Status : {bmi_status}")
```

