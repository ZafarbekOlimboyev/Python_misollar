xyz=int(input())
x=xyz//100
y=(xyz//10)%10
z=xyz%10
a=xyz//1000
data_100={0: "",1:"bir yuz",2:"ikki yuz",3:"uch yuz",4:"to`rt yuz",5:"besh yuz",6:"olti yuz",7:"yetti yuz",8:"sakkiz yuz",9:"to`qqiz yuz"}
data_10={0:"",1:"o`n",2:"yigirma",3:"o’ttiz",4:"qirq",5:"ellik",6:"oltmish",7:"yetmish",8:"sakson",9:"to’qson"}
data_1={0: "",1:"bir",2:"ikki",3:"uch",4:" to’rt",5:"besh",6:"olti",7:"yetti",8:"sakkiz",9:"to’qqiz"}
data_0={0:"bir ming"}
print(data_0[a],data_100[x],data_10[y],data_1[z])