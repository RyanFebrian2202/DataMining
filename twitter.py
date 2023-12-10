import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

df = pd.read_csv("Twitter_Data.csv")

print(df.head())
print('\n')

df.info()


df['clean_text'] = df['clean_text'].str.lower()

# check for NaN values and remove them (optional)
df["clean_text"].dropna(inplace=True)

# convert the column to string
df['clean_text'] = df['clean_text'].astype(str)

tokens = df['clean_text'].apply(word_tokenize)

print('\n')
print(tokens)
