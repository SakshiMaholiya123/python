import numpy as np

data=np.random.randint(0,101,size=(200,6))
print(data)

total=data.sum(axis=1)
print(f"total score in all subjects{total}")
percent=(total/600)*100
print(f"percentage is{percent}")


grades = np.where(percent>=90,'A',np.where(percent>=75,'B',np.where(percent >= 60, 'C',np.where(percent>=40,'D','F')) ) )

for i in range(10):
    print(f"Student {i+1} : {grades[i]}")

top_cnt = int(0.10 * len(percent))

top_students = np.argsort(percent)[::-1][:top_cnt]

for rank, index in enumerate(top_students, start=1):
    print(f"Rank {rank}")
    print(f"Student ID : {index}")