"""
data_dict= {"data1":11, "data2":25, "data3" : 8, "data4": 9, "data5":16}
data_dict lug’atining barcha value’larine ko’paytmasini hisoblovchi
dastur tuzing.
"""
data_dict= {"data1":11, "data2":25, "data3" : 8, "data4": 9, "data5":16}
s=1
for i in data_dict.values():
    s=s*i
print(s)