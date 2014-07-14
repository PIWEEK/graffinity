from unittest import TestCase

import graffinity

class TestFoo(TestCase):

    def test_basic_calculation(self):
        data = {
            "n1": {
                "gender": 0,
                "age": 36,
                "languages": [2,5,6],
            },
            "n2": {
                "gender": 1,
                "age": 33,
                "languages": [2,6],
            }
        }

        gender_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        age_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        languages_func = lambda x: 5*(len(x) - len(set(x)))
        affinity_func = lambda x: gender_func(x) + 3.5*age_func(x) + 0.1*languages_func(x)

        funcs = {
            "gender": gender_func,
            "age": age_func,
            "languages": languages_func,
            "affinity": affinity_func
        }
        g = graffinity.Graffinity(data, funcs)
        results = g.calculate()
        self.assertEquals(results["n1"]["n1"], 100)
        self.assertEquals(results["n1"]["n2"], 56)
        self.assertEquals(results["n2"]["n1"], 56)
        self.assertEquals(results["n2"]["n2"], 100)
