liste = ["Demhat","EmreS","EmreG","Durmus","Cevaplar"]
import os
filename = "pandas1"
for item in liste:
    os.mkdir(f"/workspace/KordsaIntroML/Exercises/{item}")
    open(f"Exercises/{item}/{filename}.ipynb","wb+")
