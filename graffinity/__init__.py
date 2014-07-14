import itertools
import re
from collections import defaultdict


class Graffinity(object):
    def __init__(self, data, funcs, affinityfunc):

        self.data = data

        p = re.compile("([a-z]+ )_[a-z]+\(x\)", re.VERBOSE)
        self.affinityfunc = p.sub("self.checkreverse(fr['\\1'],n,m)",affinityfunc)

        self.f = {}
        self.functionresults = {}
        self.matrix = {}


        for func in funcs.keys():
          funcdata = [(n,nfuncs[func]) for n,nfuncs in data.items()]
          self.f[func] = {'data':funcdata}
          self.f[func]['funcdef'] = funcs[func]

        nodenames = data.keys()

        #We initialize the result matrix
        for nodename in nodenames:
          self.matrix[nodename] = {}
          for othernodename in nodenames:
            self.matrix[nodename][othernodename] = 0.0

        print("initial matrix", self.matrix)

    def calculate(self):

        for isolatedfunc in self.f.items():
          self.calculateisolatedfunction(isolatedfunc)

        fr = self.functionresults



        for n in self.matrix:
          for m in self.matrix:
            self.matrix[n][m] = eval(self.affinityfunc)
            self.matrix[m][n] = self.matrix[n][m]



        print("final matrix",self.matrix)

        return self.matrix

    def calculategroup(self, group):
      pass

    def calculateisolatedfunction(self, isolatedfunc):

        funcdictresult = {}
        nodepairs = list(itertools.combinations(isolatedfunc[1]['data'],2))
        funcdictresult = defaultdict(lambda: defaultdict(float))

        for nodepair in nodepairs:
          names, values = list(zip(*nodepair))
          flatvalues = [item for sublist in values for item in sublist]
          result = isolatedfunc[1]['funcdef'](flatvalues)
          funcdictresult[names[0]][names[1]] = result

        self.functionresults[isolatedfunc[0]] = funcdictresult

        return

    def checkreverse(self, function, n, m):
      if function[n][m] == 0:
        return function[m][n]
      return function[n][m]


