
import pandas as pd

df = pd.read_excel('D:\Data\Mercari_item_numbers_only.xlsx')
items = df['number'].tolist()

print(items)
print(type(items))

list.reverse(items)

for item in items:
    print(type(item))
    print("look at this number : " + str(item))