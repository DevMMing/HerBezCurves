import math
f=open('script2',"w")
f.write("hermite\n")
f.write("200 400 200 100 -250 -175 500 -200\n")
for i in range(100):
    #f.write("hermite\n")
    #f.write("400 400 100 100 "+str(i+250)+" "+ str(i-175)+" "+str(500+i)+" "+str(i-200)+"\n")
    f.write("hermite\n")
    f.write("400 400 100 100 "+str(i+250)+" "+ str(i-175)+" "+str(500-i)+" "+str(i+200)+"\n")
    f.write("hermite\n")
    f.write("400 400 100 100 "+str(i-250)+" "+ str(i+175)+" "+str(500+i)+" "+str(i-200)+"\n")
    f.write("hermite\n")
    f.write("400 400 100 100 "+str(250-i)+" "+ str(i+175)+" "+str(500+i)+" "+str(i+200)+"\n")
    f.write("hermite\n")
    f.write("400 400 100 100 "+str(i-250)+" "+ str(i+175)+" "+str(500-i)+" "+str(i+200)+"\n")
f.write("display\n")
f.write("save\n")
f.write("img.png\n")
f.close()
