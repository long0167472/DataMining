import tkinter as tk
from tkinter import messagebox
import logging
from diabetes import Diabetes
# Tạo cửa sổ
window = tk.Tk()
window.geometry("500x200")
window.title("Dự đoán khả năng bị bệnh tiểu đường")
# Tạo và định vị các thành phần giao diện
labelpreg = tk.Label(window, text="Pregnancies:")
labelpreg.grid(column=1, row =1)
entry_preg = tk.Entry(window)
entry_preg.grid(column =2, row=1)

label_glucose = tk.Label(window, text="Glucose:")
label_glucose.grid(column=1, row =2)
entry_glucose = tk.Entry(window)
entry_glucose.grid(column=2, row =2)

label_blood = tk.Label(window, text="Blood Pressure:")
label_blood.grid(column=1, row =3)
entry_blood = tk.Entry(window)
entry_blood.grid(column=2, row =3)

label_skin = tk.Label(window, text="Skin Thickness:")
label_skin.grid(column=1, row =4)
entry_skin = tk.Entry(window)
entry_skin.grid(column=2, row =4)

label_insulin = tk.Label(window, text="Insulin:")
label_insulin.grid(column=4, row =1)
entry_insulin = tk.Entry(window)
entry_insulin.grid(column=5, row =1)

label_bmi = tk.Label(window, text="BMI:")
label_bmi.grid(column=4, row =2)
entry_bmi = tk.Entry(window)
entry_bmi.grid(column=5, row =2)

label_diabetes = tk.Label(window, text="Diabetes:")
label_diabetes.grid(column=4, row =3)
entry_diabetes = tk.Entry(window)
entry_diabetes.grid(column=5, row =3)

label_age = tk.Label(window, text="Age:")
label_age.grid(column=4, row =4)
entry_age = tk.Entry(window)
entry_age.grid(column=5, row =4)

lbresult = tk.Label(window, text="result: ")
lbresult.grid(column =1, row=7)
txtResult = tk.Entry(window,width=30)
txtResult.grid(column =2, row=7)


def check_range():
    try:
        check=True
        preg = float(entry_preg.get())
        preg_range = ""

        if preg <=5:
            preg_range = "1"
        elif 6 <= preg <= 11:
            preg_range = "2"
        elif 12<= preg <= 17:
            preg_range = "3"
        else:
            messagebox.showwarning("Lỗi", "Dữ liệu Pregnancies không phù hợp. Xin hãy nhập lại trong khoảng từ 0 đến 17")
            check = False

        glucose = float(entry_glucose.get())
        glucose_range = ""

        if glucose < 50:
            glucose_range = "1"
        elif 50 <= glucose <= 99:
            glucose_range = "2"
        elif 100 <= glucose <= 149:
            glucose_range = "3"
        elif 150 <= glucose <= 199:
            glucose_range = "4"
        else:
            messagebox.showwarning("Lỗi", "Dữ liệu glucose không phù hợp. Xin hãy nhập lại trong khoảng từ 0 đến 199")
            check = False

        blood = float(entry_blood.get())
        blood_range = ""

        if 0<= blood <=40:
            blood_range = "1"
        elif 41 <= blood <= 81:
            blood_range = "2"
        elif 82<= blood <= 122:
            blood_range = "3"
        else:
            messagebox.showwarning("Lỗi", "Dữ liệu BloodPressure không phù hợp. Xin hãy nhập lại trong khoảng từ 0 đến 122")
            check = False

        skin = float(entry_skin.get())
        skin_range = ""

        if 0<= skin <=33:
            skin_range = "1"
        elif 34 <= skin <= 66:
            skin_range = "2"
        elif 67<= skin <= 99:
            skin_range = "3"
        else:
            messagebox.showwarning("Lỗi", "Dữ liệu skinThickness không phù hợp. Xin hãy nhập lại trong khoảng từ 0 đến 122")
            check = False

        insulin = float(entry_insulin.get())
        insulin_range = ""

        if 0<= insulin <=211:
            insulin_range = "1"
        elif 212 <= insulin <= 423:
            insulin_range = "2"
        elif 424<= insulin <= 635:
            insulin_range = "3"
        elif 636<= insulin <= 846:
            insulin_range = "4"
        else:
            messagebox.showwarning("Lỗi", "Dữ liệu insulin không phù hợp. Xin hãy nhập lại trong khoảng từ 0 đến 122")
            check = False

        bmi = float(entry_bmi.get())
        bmi_range = ""

        if 0<= bmi <=22.3:
            bmi_range = "1"
        elif 22.4 <= bmi <= 44.7:
            bmi_range = "2"
        elif 44.8<= bmi <= 67.1:
            bmi_range = "3"
        else:
            messagebox.showwarning("Lỗi", "Dữ liệu bmi không phù hợp. Xin hãy nhập lại trong khoảng từ 0 đến 122")
            check = False

        diabetes = float(entry_diabetes.get())
        diabetes_range = ""

        if 0.078<= diabetes <=0.663:
            diabetes_range = "1"
        elif 0.664 <= diabetes <= 1.249:
            diabetes_range = "2"
        elif 1.25<= diabetes <= 1.835:
            diabetes_range = "3"
        elif 1.836<= diabetes <= 2.42:
            diabetes_range = "3"
        else:
            messagebox.showwarning("Lỗi", "Dữ liệu diabetes  không phù hợp. Xin hãy nhập lại trong khoảng từ 0 đến 122")
            check = False
        
        age = float(entry_age.get())
        age_range = ""

        
        if 0< age <=41:
            age_range = "1"
        elif 41 < age <= 61:
            age_range = "2"
        elif 61< age <= 81:
            age_range = "3"
        else:
            messagebox.showwarning("Lỗi", "Dữ liệu age không phù hợp. Xin hãy nhập lại trong khoảng từ 0 đến 81")
            check = False
        if check:
            model = Diabetes()
            predict = model.predict(preg_range, glucose_range, blood_range, skin_range, insulin_range, bmi_range, diabetes_range, age_range)
            # txtResult = predict  
            if (predict == 1):
                txtResult.delete(0, tk.END)
                txtResult.insert(0, "Bị tiểu đường")
            else:
                txtResult.delete(0, tk.END)
                txtResult.insert(0, "Không bị tiểu đường")
    except IOError as ex:
        logging.error(f"An IOError occurred: {ex}")


btn1 = tk.Button(window, text="Predict", command=check_range)
# btn1.place(x=200, y= 220)
btn1.grid(column=1, row =6)


# Hiển thị cửa sổ
window.mainloop()
