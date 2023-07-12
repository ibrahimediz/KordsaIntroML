liste = ["Demhat","EmreS","EmreG","Durmus","Cevaplar","Canberk"]
import os
filename = "01_DeepLearning"
for item in liste:
    try:
        os.mkdir(f"/workspace/KordsaIntroML/Exercises/{item}")
    except:
        pass 
    open(f"Exercises/{item}/{filename}.ipynb","ab+")



""" 
   Tip         kilo    fiyat
0  elma         10      12
1  armut        25      16
2  portakal     30      12
3  mandalina    12      35
"""

