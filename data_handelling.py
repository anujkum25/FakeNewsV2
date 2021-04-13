import pandas as pd 

real_data=pd.read_csv("Data\FakeNews_ref_data_Real.csv")
fake_data=pd.read_csv("Data\FakeNews_reference_data_Fake.csv")

print(real_data.head())
print(fake_data.head())

