print("Nhập các dòng văn bản (Nhập 'done' để kết thúc):")
lines = []

while 1:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
    
print("\nCác dòng đã nhập sai khi chuyển thành chữ in hoa:")
for line in lines:
    print(line.upper())