from unittest import TestCase
import unittest

import graffinity
import statistics



class TestFoo(TestCase):

    def test_time_calculation(self):
        with open("atest.py",'r') as tf:
            data = eval(tf.read())

        gender_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        age_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        languages_func = lambda x: 5*(len(x) - len(set(x)))

        funcs = {
            "gender": gender_func,
            "age": age_func,
            "languages": languages_func,
        }

        affinityfunc = "gender_func(x) + 3.5*age_func(x) + 0.1*languages_func(x)"

        g = graffinity.Graffinity(data, funcs, affinityfunc)
        g.calculate()

if __name__=="__main__":
    import cProfile
    cProfile.run('unittest.main()')
