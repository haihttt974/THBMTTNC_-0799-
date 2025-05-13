def dao_nguoc(str):
    return str[::-1]

input_string = input("Mời nhập chuỗi cần đảo ngược: ")
print("Chuỗi đảo ngược là:", dao_nguoc(input_string))