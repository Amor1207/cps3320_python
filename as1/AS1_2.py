while 1:
    try:
        systolic = float(input(("please input your Systolic value: ")))
        if systolic > 0:
            break
        else:
            print("input a postive number!")
    except:
        print("input a postive number!")
if systolic < 120:
    print("The Systolic value "+str(systolic)+" implies a Normal blood pressure case")
elif systolic >= 120 and systolic <= 139:
    print("The Systolic value "+str(systolic)+" implies a Prehypertension blood pressure case")
elif systolic >= 140 and systolic <= 159:
    print("The Systolic value "+str(systolic)+" implies a High blood -Stage 1 blood pressure case")
elif systolic >= 160 and systolic <= 179:
    print("The Systolic value "+str(systolic)+" implies a High blood -Stage 2 blood pressure case")
else:
    print(("The Systolic value "+str(systolic)+" implies a Hypersensitive crisis blood pressure case"))

