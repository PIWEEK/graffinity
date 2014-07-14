
class Graffinity(object):
    def __init__(self, data, funcs):

        self.data = data

        self.f = {}
        self.functionresults = {}
        self.matrix = {}

        funcs.pop("affinity") #to workaround test's temporary inconsistency

        for func in funcs.keys():
          funcdata = [(d[0],d[1][func]) for d in data.items()]
          self.f[func] = {'data':funcdata}
          self.f[func]['funcdef'] = funcs[func]

        nodenames = data.keys()

        for datum in nodenames:
          self.matrix[datum] = {}
          for otherdatum in nodenames:
            self.matrix[datum][otherdatum] = 100

        print("initial matrix", self.matrix)

    def calculate(self):

        for isolatedfunc in self.f.items():
          self.calculateisolatedfunction(isolatedfunc)

        print("******************************************")
        print("final results per function",self.functionresults)

        #with individual function results do stuff and update self.matrix


        fr = self.functionresults

        for n in self.matrix:
          for m in self.matrix:
            try:
              self.matrix[n][m] = self.checkreverse(fr['gender'],n,m) + self.checkreverse(fr['age'],n,m) + self.checkreverse(fr['languages'],n,m)
            except:
              pass

        print("final matrix",self.matrix)
        for functionresult in self.functionresults.items():
          print(functionresult)

        return self.matrix

    def calculategroup(self, group):
      pass

    def calculateisolatedfunction(self, isolatedfunc):

        print("Processing function: ",isolatedfunc[0])
        result = {}
        funcdictresult = {}

        #will make tuples of consecutive items in a list (nodepairs)
        f = lambda data: [data[i:i+2] for i in range(len(data) - 1)]

        nodepairs = f(isolatedfunc[1]['data'])

        for nodepair in nodepairs:
          names, values = list(zip(*nodepair))

          flatvalues = [item for sublist in values for item in sublist]

          for n in names:
            result = isolatedfunc[1]['funcdef'](flatvalues)
            funcdictresult[names[0]] = {names[1]:result}


        print("******************************************")
        print(isolatedfunc[0],funcdictresult)
        self.functionresults[isolatedfunc[0]] = funcdictresult

        return

    def checkreverse(self, function, n, m):
      try:
        print("as is! ",function[n][m])
        return function[n][m]
      except:
        print("reverse! ",function[m][n])
        return function[m][n]


