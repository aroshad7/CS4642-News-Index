import pandas as pd

news_set = pd.read_csv('news_1.csv');
dFrame = pd.DataFrame(news_set)

for i in range(len(dFrame.index)):
    if type(dFrame.News[i]) != str:
        print (dFrame.URL[i]),
        print (i+2)
        dFrame = dFrame.drop(i)

dFrame.to_csv('news_1_formatted.csv', index=False)