import numpy as np
money=np.random.randint(-500,1000,size=(50,20))
print(money)

debit=np.where(money<0,money,0)
credit=np.where(money>0,money,0)
print(f"debit transaction{debit}")
print(f"credit transaction {credit}")

sum=money.sum(axis=0)
print(f"daily net changes{sum}")