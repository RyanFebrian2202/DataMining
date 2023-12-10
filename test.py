
import nltk;
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

text = "The tranquility of the morning enveloped the small town, as soft sunlight gently kissed the cobblestone streets. Birds chirped melodiously, creating a symphony that echoed through the awakening alleys. Residents emerged from their homes, greeted by the fresh, crisp air, ready to embrace the day's possibilities."

ps = PorterStemmer()

print(word_tokenize(text))
print('\n')

words = word_tokenize(text)
for w in words:
    print(w, " : ", ps.stem(w))
