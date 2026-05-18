import pandas as pd

dict={'a':[1,2,3,4,5],'b':[6,7,8,9,10],'c':[11,12,13,14,15]}
d=pd.DataFrame(dict)
print(d)

#create csv file

d.to_csv("data.csv")

d.to_csv("data_1.csv",index=False,header=['p','q','r'])

csv_1=pd.read_csv("C:\\Users\\DELL\\Downloads\\sample_data_25x5.csv")
print(csv_1)

csv_2=pd.read_csv("C:\\Users\\DELL\\Downloads\\sample_data_25x5.csv",nrows=1)
print(csv_2)
print(type(csv_2))

csv_2=pd.read_csv("C:\\Users\\DELL\\Downloads\\sample_data_25x5.csv",usecols=['City'])
print(csv_2)

csv_2=pd.read_csv("C:\\Users\\DELL\\Downloads\\sample_data_25x5.csv",skiprows=[1,2,3,4])
print(csv_2)

csv_2=pd.read_csv("C:\\Users\\DELL\\Downloads\\sample_data_25x5.csv",header=2)
print(csv_2) 

csv_2=pd.read_csv("C:\\Users\\DELL\\Downloads\\sample_data_25x5.csv",names=["col_1",'col_2','col_3'])
print(csv_2)

csv_2=pd.read_csv("C:\\Users\\DELL\\Downloads\\sample_data_25x5.csv",dtype={'Marks':'float'})
print(csv_2)
