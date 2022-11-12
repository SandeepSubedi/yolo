import pandas as pd
import re
from textblob import TextBlob
import json
from pandas import json_normalize
import itertools
import itertools
def oneDArray(x):
    return list(itertools.chain(*x))

responses = [{'product_name': 'Goldstar black sports shoes', 'description': 'very very good product', 'price': 1699, 'images': 'http://shoeasy.me/media/photos/products/Goldstar_Black___Grey_Sports_Shoes_For_Men___G10_G305.jpg', 'category': {'category_name': 'Sports'}, 'reviews': ['Very nice product but delivery time was very slow , 3.50', 'bad product late delivery , 0.50']}, {'product_name': 'Goldstar Black Sports Shoe G11', 'description': 'Goldstar Black Sports Shoe G11', 'price': 1299, 'images': 'http://shoeasy.me/media/photos/products/Goldstar_Black_Sports_Shoes_For_Men_-_G10_G902.jpg', 'category': {'category_name': 'Sports'}, 'reviews': ['Good Product , 4.50', 'It doesnot fit on my foot and color goes after washing , 1.50']}, {'product_name': 'GoldStar Black Sports Shoe G766', 'description': 'GoldStar Black Sports Shoe G766', 'price': 1599, 'images': 'http://shoeasy.me/media/photos/products/Goldstar_Shoes_For_Men_G10_701_Black_Goldstar_Sports_Shoe.jpg', 'category': {'category_name': 'Sports'}, 'reviews': ['Good product durable but seller response was slow , 3.50', 'Nice product , 5.00']}]
df=pd.DataFrame(responses)
# big_list=[]
# for i in range(len(responses)):
#     a=responses[i]['reviews']
#     newList = []
#     for element in a:
#         print("this is elemenmt",element)
#         newList.extend(element.split(','))
#        # newList=oneDArray(newList)
#         print(newList)
#     big_list.append(newList)
# print(big_list)

# for i in range(len(big_list)):
#     df = pd.DataFrame (big_list[i], columns = ['rating and reviews'])
#     print(df)