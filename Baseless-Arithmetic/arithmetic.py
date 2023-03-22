class BaseArithmetic:
    def __init__(self, base=None, values=None):
        self.base = 10 if base is None else base
        self.values = [] if values is None else values
        self.init_dict()

    def naive_add(self, valList):
        valList = self.cleanList(valList)
        result = []
        carry = 0

        for i in range(len(valList[0])):
            carry = carry // self.base
            psum = sum([carry] + [self.conDict[(entry[len(valList[0]) - i - 1])] for entry in valList])
            ires = psum % self.base
            result.append(self.vertDict[str(ires)])

            if psum >= self.base:
                carry += psum - ires

        while carry > 0:
            result.append((carry // self.base) % self.base)
            carry = carry // self.base

        result = "".join([str(i) for i in reversed(result)])
        while result[0] == "0":
            result = result[1:]

        return f"Base {self.base}: " + result

    def multiply(self, valList):
        valList = self.cleanList(valList)
        product = [0] * (len(valList[0]) * len(valList))

        for i in range(len(valList[0])):
            for j in range(len(valList)):
                temp = self.conDict[valList[j][len(valList[j]) - i - 1]] * (self.base ** i)
                product = self.naive_add([product, temp])

        return product

    def cleanList(self, valList):
        maxLength = max(map(lambda x: len(x), valList))
        cleanBin = [("0" * (maxLength - len(entry)) + entry) for entry in valList]
        return cleanBin

    def init_dict(self):
        self.conDict = {f"{chr(55 + i)}": i for i in range(10, 36)}
        self.vertDict = {f"{i}": chr(55 + i) for i in range(10, 36)}
        self.conDict.update({f"{i}": i for i in range(10)})
        self.vertDict.update({f"{i}": i for i in range(10)})
        self.conDict.update({f"{chr(87 + j)}": j for j in range(10, 36)})


example = BaseArithmetic(base=36, values=["1A2", "2B3", "4C4"])
print(example.naive_add(example.values))
print(example.multiply(["12", "34"]))
