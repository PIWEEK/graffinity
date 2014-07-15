from random import choice, sample

def datagenerator(n=1000):
    datadict = {}
    for i in range(n):
        datadict["n"+str(i)] = {"gender":[choice(genderchoices)],"age":[choice(agechoices)],"languages":sample(languageslist,3)}
    return datadict

genderchoices = [1,2]
agechoices = [i for i in range(18,70)]
languageslist = [i for i in range(1,20)]

h=datagenerator(50)
fi = open("atest.py",'w')
fi.write(str(h))
fi.close()

