import itertools
import re
import os
from collections import defaultdict
from multiprocessing import Pool, cpu_count

import dill

class GraffinityFunctionCalculator(object):
    def __init__(self, isolatedfunc):
        self._isolatedfunc = isolatedfunc

    def calculate(self):
        if hasattr(os, 'getppid'):  # only available on Unix
            print('parent process:', os.getppid())
        print('process id:', os.getpid(), self._isolatedfunc[0])

        funcdictresult = {}
        nodepairs = list(itertools.combinations(self._isolatedfunc[1]['data'],2))
        funcdictresult = defaultdict(lambda: defaultdict(float))

        for nodepair in nodepairs:
            names, values = list(zip(*nodepair))
            flatvalues = [item for sublist in values for item in sublist]
            result = self._isolatedfunc[1]['funcdef'](flatvalues)
            funcdictresult[names[0]][names[1]] = result

        print('FINISHED:', os.getpid(), self._isolatedfunc[0])
        return dill.dumps({self._isolatedfunc[0]: funcdictresult})


def run_dill_encoded(what):
    fun, args = dill.loads(what)
    return fun(*args)


def graffinity_worker(*args):
    gfc = GraffinityFunctionCalculator(args)
    return gfc.calculate()


class Graffinity(object):
    def __init__(self, data, funcs, affinityfunc, processors = 1):
        self.data = data
        self.processors = processors
        p = re.compile("([a-zA-Z0-9]+ )_[a-z]+\(x\)", re.VERBOSE)
        self.affinityfunc = p.sub("checkreverse(fr['\\1'],n,m)", affinityfunc)

        self.f = {}
        self.matrix = {}

        for func in funcs.keys():
            funcdata = [(n, nfuncs[func]) for n, nfuncs in data.items()]
            self.f[func] = {'data':funcdata}
            self.f[func]['funcdef'] = funcs[func]

        nodenames = data.keys()

        #We initialize the result matrix
        for nodename in nodenames:
            self.matrix[nodename] = {}
            for othernodename in nodenames:
                self.matrix[nodename][othernodename] = 0.0

    def calculate(self):
        pool=Pool(cpu_count())
        jobs = []
        for isolatedfunc in self.f.items():
            job = pool.apply_async(run_dill_encoded, (dill.dumps((graffinity_worker, isolatedfunc)),))
            jobs.append(job)

        self.functionresults = {}
        for job in jobs:
            self.functionresults.update(dill.loads(job.get()))

        # Black magic!
        # This variable must be named fr because it's used in the eval(self.affinityfunc)
        fr = self.functionresults

        for n in self.matrix:
            for m in self.matrix:
                self.matrix[n][m] = eval(self.affinityfunc)
                self.matrix[m][n] = self.matrix[n][m]

        return self.matrix

    def calculategroup(self, group):
        pass

def checkreverse(function, n, m):
    if function[n][m] == 0.0:
        return function[m][n]

    return function[n][m]
