from pkg import *
print("請輸入三角形的 3 個頂點坐標\r\n------------------------------")
coordinate_input=input("請輸入頂點A的坐標：")#A輸入
a=coordinate_input.split(",")
A=(a[0],a[1])

coordinate_input=input("請輸入頂點B的坐標：")#B輸入
b=coordinate_input.split(",")
B=(b[0],b[1])

coordinate_input=input("請輸入頂點C的坐標：")#C輸入
c=coordinate_input.split(",")
C=(c[0],c[1])

zhonxin_coordinate=triangle_zhonxin(A,B,C)#重心計算
print("------------------------------")
print(f"此三角形的重心為：({zhonxin_coordinate[0]},{zhonxin_coordinate[1]})")