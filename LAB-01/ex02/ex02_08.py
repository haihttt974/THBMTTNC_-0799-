def chia_het_cho_5(bin):
    thapphan = int(bin, 2)
    if thapphan % 5 == 0:
        return True
    else:
        return False
    
chuoi_bin = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")
bin_list = chuoi_bin.split(',')
so_chia_het_cho_5 = [so for so in bin_list if chia_het_cho_5(so)]

if len(so_chia_het_cho_5) > 0:
    ket_qua = ', '.join(so_chia_het_cho_5)
    print("Các số nhị phân chia hết cho 5 là: ", ket_qua)
else:
    print("Không có số nhị phân nào chia hết cho 5")