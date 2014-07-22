from unittest import TestCase
import unittest

import graffinity
import statistics
import createtestdata


class TestFoo(TestCase):

    def test_time_calculation(self):

        print("creating data test")
        n = 16
        h=createtestdata.datagenerator(n)
        fi = open("atest.py",'w')
        fi.write(str(h))
        fi.close()

        with open("atest.py",'r') as tf:
            data = eval(tf.read())

        print("creating data test: FINISHED")

        gender_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        age_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        languages_func = lambda x: 5*(len(x) - len(set(x)))
        friends_func = lambda x: 2.5*(len(x) - len(set(x)))
        knowngames_func = lambda x: 2.5*(len(x) - len(set(x)))/len(x)
        toplaywishlist_func = lambda x: 10*(len(x) - len(set(x)))/len(x)
        favouritegames_func = lambda x: 20*(len(x) - len(set(x)))/len(x)
        preferences_func = lambda x: 1*(len(x) - len(set(x)))
        vetoes_func = lambda x: 1*(len(x) - len(set(x)))
        gametype_func = lambda x: 15*(len(x) - len(set(x)))/len(x)
        skill01_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        skill02_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        skill03_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        skill04_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        skill05_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        skill06_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        skill07_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        skill08_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        skill09_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        skill10_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        guilds_func = lambda x: 5*(len(x) - len(set(x)))/len(x)

        funcs = {
            "gender": gender_func,
            "age": age_func,
            "languages": languages_func,
            "friends" : friends_func,
            "knowngames" : knowngames_func,
            "toplaywishlist": toplaywishlist_func,
            "favouritegames": favouritegames_func,
            "preferences": preferences_func,
            "vetoes": vetoes_func,
            "gametype": gametype_func,
            "skill01": skill01_func,
            "skill02": skill02_func,
            "skill03": skill03_func,
            "skill04": skill04_func,
            "skill05": skill05_func,
            "skill06": skill06_func,
            "skill07": skill07_func,
            "skill08": skill08_func,
            "skill09": skill09_func,
            "skill10": skill10_func,
            "guilds": guilds_func,


        }

        affinityfunc = """gender_func(x) + age_func(x) + languages_func(x) + \
        friends_func(x) + knowngames_func(x) + toplaywishlist_func(x) + \
        favouritegames_func(x) + preferences_func(x) + vetoes_func(x) + \
        gametype_func(x) + skill01_func(x) + skill02_func(x) + skill03_func(x) + \
        skill04_func(x) + skill05_func(x) + skill06_func(x) + skill07_func(x) + \
        skill08_func(x) + skill09_func(x) + skill10_func(x) + guilds_func(x)"""

        groupaffinityfunc = """gender_func(x) + age_func(x) + languages_func(x) + \
        friends_func(x) + knowngames_func(x) + toplaywishlist_func(x) + \
        favouritegames_func(x) + preferences_func(x) + vetoes_func(x) + \
        gametype_func(x) + skill01_func(x) + skill02_func(x) + skill03_func(x) + \
        skill04_func(x) + skill05_func(x) + skill06_func(x) + skill07_func(x) + \
        skill08_func(x) + skill09_func(x) + skill10_func(x) + guilds_func(x)"""

        g = graffinity.Graffinity(data, funcs, affinityfunc, groupaffinityfunc)

        results = g.calculate()

        print(results.get('n1','n18'),results.get('n18','n1'))

        # g = graffinity.Graffinity(data, funcs, affinityfunc, groupaffinityfunc)
        # group = ['n%i'%(i) for i in range(40,80)]
        # result = g.calculategroup(group)
        # print(group, result/(len(group)-1))

if __name__=="__main__":
#    import cProfile
#    cProfile.run('unittest.main()')
    unittest.main()
