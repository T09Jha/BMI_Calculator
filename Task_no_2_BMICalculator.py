import tkinter
root=tkinter.Tk()
root.title("BODY-MASS-INDEX CALCULATOR")
#WEIGHT label
weight_label = tkinter.Label(root, text='Enter your weight (kg):')
weight_label.pack()
weight_entry = tkinter.Entry(root)
weight_entry.pack()
#Height label
height_label = tkinter.Label(root, text='Enter your height (cm):')
height_label.pack()
height_entry = tkinter.Entry(root)
height_entry.pack()
def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100  # converting height from cm to meters
    bmi = weight / (height * height)
    result_label.config(text=f"Your BMI: {bmi:.2f}")
    if bmi < 18.5:
        result_label.config(text=f"Your BMI: {bmi:.2f} You are UNDERWEIGHT!")
    elif bmi >= 18.5 and bmi <= 24.9:
        result_label.config(text=f"Your BMI: {bmi:.2f} You are NORMALLY WEIGHED!")
    elif bmi >= 25 and bmi <= 29.9:
        result_label.config(text=f"Your BMI: {bmi:.2f} You are OVERWEIGHT!")
    else:
        result_label.config(text=f"Your BMI: {bmi:.2f} You are OBESE!!!!! You need to take CARE!!")
calculate_button = tkinter.Button(root, text='Calculate BMI', command=calculate_bmi)
calculate_button.pack()
#Result label
result_label = tkinter.Label(root, text='')
result_label.pack()
result_label = tkinter.Label(root, text='')
result_label.pack()
# Start the Tkinter main loop
root.mainloop()