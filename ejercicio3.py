a = ["1","2","3","4","5","6","7","8","9","10"]
b = ["1","1","3","5","8","13","21"]

def juntar():
    for i,x in zip(a,b):
        print("{"+",".join((a,b))+"}")

juntar()