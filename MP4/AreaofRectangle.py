# Name: Dana Huang
# School: FEU Alabang
# Machine Problem number - 1

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def ans(self):
        answer = self.length * self.width
        print(f"The Area of the Rectangle is: {answer}")


# checker functions (checks if input is float or negative)
def checker(int_l, temp_l, int_w, temp_w):
    if int_l < 0 or int_w < 0:
        while int_l < 0 or int_w < 0:
            print("The number is not a positives integer:\n")
            l_input = input("Enter Length value:")
            w_input = input("Enter the width of the rectangle:")
            temp_l = float(l_input)
            temp_w = float(w_input)
            int_l = int(float(l_input))
            int_w = int(float(w_input))
            if int_l != temp_l or int_w != temp_w:
                while int_l != temp_l or int_w != temp_w:
                    print("Input the correct data format is not a Positive integer:\n")
                    l_input = input("Enter Length value:")
                    w_input = input("Enter the width of the rectangle:")
                    temp_l = float(l_input)
                    temp_w = float(w_input)
                    int_l = int(float(l_input))
                    int_w = int(float(w_input))
                    if int_l == temp_l and int_w == temp_w:
                        return int_l, int_w
                        break
            elif int_l > 0 and int_w > 0:
                return int_l, int_w
                break
    elif int_l != temp_l or int_w != temp_w:
        while int_l != temp_l or int_w != temp_w:
            print("Input the correct data format is not a Positive integer:\n")
            l_input = input("Enter Length value:")
            w_input = input("Enter the width of the rectangle:")
            temp_l = float(l_input)
            temp_w = float(w_input)
            int_l = int(float(l_input))
            int_w = int(float(w_input))
            if int_l < 0 or int_w < 0:
                while int_l < 0 or int_w < 0:
                    print("The number is not a positives integer:\n")
                    l_input = input("Enter Length value:")
                    w_input = input("Enter the width of the rectangle:")
                    temp_l = float(l_input)
                    temp_w = float(w_input)
                    int_l = int(float(l_input))
                    int_w = int(float(w_input))
                    if int_l > 0 and int_w > 0:
                        return int_l, int_w
                        break
            elif int_l == temp_l and int_w == temp_w:
                return int_l, int_w
                break
    else:
        return int_l, int_w

l_input = input("Enter Length value:")
w_input = input("Enter the width of the rectangle:")
temp_l = float(l_input)
temp_w = float(w_input)
int_l = int(float(l_input))
int_w = int(float(w_input))


int_l, int_w = checker(int_l, temp_l, int_w, temp_w)
area = Rectangle(int_l, int_w)
area.ans()
