def get_height_weight():
    height_cm = float(input("Enter your height in centimeters: "))
    weight_kg = float(input("Enter your weight in kilograms: "))
    height_m = height_cm / 100
    return height_m, weight_kg


def calculate_bmi(height_m, weight_kg):
    bmi = round((weight_kg / height_m**2), 2)
    print("Your Body Mass Index (BMI) is:", bmi)
    return bmi


def obesity_info(bmi):
    if bmi > 0:
        if bmi < 16:
            print("You are mal-nutritioned.")
        elif bmi < 18.5:
            print("You are under-weight.")
        elif bmi < 25:
            print("You are normal weight.")
        elif bmi < 30:
            print("You are over-weight.")
        else:
            print("You are obese.")
    else:
        print("Enter valid information.")


def Find_normal_weight_range(height_m):
    min_w = round(18.5 * height_m**2, 2)
    max_w = round(24.99 * height_m**2, 2)
    print("Normal weight range for your height is", min_w, "kg and", max_w, "kg.")
    return min_w, max_w


def suggest(bmi, weight_kg, min_w, max_w):
    if bmi < 18.5:
        need = round(min_w - weight_kg, 2)
        print("You should gain", need, "kg to reach the normal weight.")
    elif bmi >= 25:
        shed = round(weight_kg - max_w, 2)
        print("You should shed", shed, "kg to reach the normal weight.")
    else:
        print("Your weight is already normal.")


def run_bmi_calculator():
    height_m, weight_kg = get_height_weight()
    bmi = calculate_bmi(height_m, weight_kg)
    obesity_info(bmi)
    min_w, max_w = Find_normal_weight_range(height_m)
    suggest(bmi, weight_kg, min_w, max_w)


run_bmi_calculator()