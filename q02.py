allList=[]
dic={"eName":"","eSalary":0}
totle=0
count=0
print("----------------------------\r\n        員工薪資輸入\r\n    若姓名處未輸入則代表結束\r\n----------------------------")
while(True):
    input_name=input("請輸入姓名:")
    if input_name == "":
        break
    else:
        dic["eName"]=input_name
        dic["eSalary"]=int(input("請輸入薪資:"))
        allList.append(dic.get("eName"))
        allList.append(dic.get("eSalary"))
        print()
print("----------------------------")
for i in range(0,int(len(allList)/2)):
    print(f"員工{allList[count]:8}的薪資為{allList[count+1]:10,}")
    totle+=allList[count+1]
    count+=2
    
print("----------------------------")
print(f"合計薪資：{(totle):>10,}")
if totle!=0:
    print(f"平均薪資：{totle/int(len(allList)/2):>13.2f}")
else:
    print(f"平均薪資：{0:>13.2f}")
print("============================")