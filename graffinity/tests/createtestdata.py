from random import choice, sample, randint

n = 5000

def datagenerator(n=1000):
    datadict = {}
    for i in range(n):
        datadict["n"+str(i)] =   {
	"gender": [choice(genderchoices)],
	"age": [choice(agechoices)],
	"languages": sample(languageslist,3),
	"friends": sample(friendslist,randint(1,5)),
	"knowngames": sample(knowngameslist,randint(1,20)),
	"toplaywishlist": sample(toplaywishlistlist,randint(1,20)),
	"favouritegames": sample(favouritegameslist,randint(1,20)),
	"preferences": sample(preferenceslist,randint(1,3)),
	"vetoes": sample(vetoeslist,randint(1,3)),
	"gametype": sample(gametypelist,randint(1,5)),
	"skill01": [choice(skill01choices)],
	"skill02": [choice(skill02choices)],
	"skill03": [choice(skill03choices)],
	"skill04": [choice(skill04choices)],
	"skill05": [choice(skill05choices)],
	"skill06": [choice(skill06choices)],
	"skill07": [choice(skill07choices)],
	"skill08": [choice(skill08choices)],
	"skill09": [choice(skill09choices)],
	"skill10": [choice(skill10choices)],
	"guilds": sample(guildslist,randint(1,5)),
	}

    return datadict



genderchoices = [1,2]
agechoices = [i for i in range(18,70)]
languageslist = [i for i in range(1,20)]
friendslist = [i for i in range(1,n)]
knowngameslist =  [i for i in range(1,5000)]
toplaywishlistlist = knowngameslist
favouritegameslist = knowngameslist
preferenceslist = [i for i in range(1,5)]
vetoeslist = [i for i in range(1,5)]
gametypelist = [i for i in range(1,64)]
skill01choices = [i for i in range(1,100)]
skill02choices = skill01choices
skill03choices = skill01choices
skill04choices = skill01choices
skill05choices = skill01choices
skill06choices = skill01choices
skill07choices = skill01choices
skill08choices = skill01choices
skill09choices = skill01choices
skill10choices = skill01choices
guildslist = [i for i in range(1,200)]

if __name__=="__main__":

    h=datagenerator(n)
    fi = open("atest.py",'w')
    fi.write(str(h))
    fi.close()
