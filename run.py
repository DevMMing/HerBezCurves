import math
f=open('script2',"w")
for i in range(1000):
    f.write("circle\n")
    f.write("175 350 0 "+str(i/100.0)+"\n")
    f.write("circle\n")
    f.write("325 350 0 "+str(i/100.0)+"\n")
f.write("hermite\n")
f.write("100 400 100 100 -350 -175 50 275\n")
f.write("display\n")
f.write("save\n")
f.write("img.png\n")
f.close()
