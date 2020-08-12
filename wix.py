import pandas as pd

df = pd.read_excel('D:\Data\Get_img_url.xlsx')
urls = df['Text2'].tolist()
print(df)
