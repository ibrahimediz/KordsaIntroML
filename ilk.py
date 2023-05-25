liste = ["Demhat","EmreS","EmreG","Durmus","Cevaplar"]
import os
filename = "pandas1"
for item in liste:
    os.mkdir(f"/workspace/KordsaIntroML/Exercises/{item}")
    open(f"Exercises/{item}/{filename}.ipynb","wb+")



""" 
   Tip         kilo    fiyat
0  elma         10      12
1  armut        25      16
2  portakal     30      12
3  mandalina    12      35
"""