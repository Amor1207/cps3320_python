val = [0 for i in range(12)]
index = 0
while index < 12:
    temp = 'Enter val'+str(index)+": "
    try:
        val[index] = float(input(temp))
        index += 1
    except:
        print("please input an int or float!")
#6.0 * (1 - (1/3) - (1.0/5) + (6.0/2.0) + (16/8) - (2.0/11))
result = val[0] * (val[1] - (val[2] / val[3]) - (val[4] / val[5]) + (val[6] / val[7]) + (val[8] / val[9]) - (val[10] / val[11]))
print("The result of solving the expression: ", end="")
print(str(val[0]) + "*(" + str(val[1]) + "-(" + str(val[2]) + "/" + str(val[3]) + ")-(" + str(val[4]) + "/" + str(val[5]), end="")
print(")+(" + str(val[6]) + "/" + str(val[7]) + ")+(" + str(val[8]) + "/" + str(val[9]) + ")-(" + str(val[10]) + "/" + str(
    val[11]) + "))"+" is ",result, end="")