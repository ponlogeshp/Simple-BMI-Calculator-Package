# Author : Pon Logesh P
# Country : India, Chennai.


"""
Input:
    
bmi_input : Accepts a Dictionary of Height and Weight of a Individual

Output:

returns : a pair of values which are bmi_score and the bmi_status

"""


def generate_bmi_data(bmi_input):
    try:

        bmi_score = bmi_input["weight"] / (bmi_input["height"]**2)

        if bmi_score <= 20:
            bmi_status = "lean"
        elif bmi_score >=21 and bmi_score <=30:
            bmi_status = "normal"
        else:
            bmi_status = "obese"

    except Excpetion as exc:
        raise Exception(exc)
    return bmi_score, bmi_status
