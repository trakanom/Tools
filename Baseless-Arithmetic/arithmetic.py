from functools import cache


@cache
def init_dict(base):
    conDict = {f"{chr(55 + i)}": i for i in range(10, base + 1)}
    vertDict = {f"{i}": chr(55 + i) for i in range(10, base + 1)}
    conDict.update({f"{i}": i for i in range(10)})
    vertDict.update({f"{i}": i for i in range(10)})
    conDict.update({f"{chr(87 + j)}": j for j in range(10, base + 1)})
    return conDict, vertDict


def cleanList(valList):
    maxLength = max(map(lambda x: len(x), valList))
    cleanBin = [
        ["0"] * (maxLength - len(entry)) + [digit for digit in entry]
        for entry in valList
    ]
    return cleanBin


def naive_add(base, valList):
    conDict, vertDict = init_dict(base)
    valList = cleanList(valList)
    result = []
    carry = 0

    for i in range(len(valList[0])):
        carry = carry // base
        psum = sum(
            [carry]
            + [conDict[str(entry[len(valList[0]) - i - 1])] for entry in valList]
        )
        ires = psum % base
        result.append(vertDict[str(ires)])

        if psum >= base:
            carry += psum - ires

    while carry > 0:
        result.append((carry // base) % base)
        carry = carry // base

    result = "".join([str(i) for i in reversed(result)])
    while result[0] == "0":
        result = result[1:]

    return result


def multiply(base, valList):
    #TODO THIS IS STILL BROKEN. NEED TO REVISIT ALGORITHM.
    conDict, vertDict = init_dict(base)
    valList = cleanList(valList)
    product = [0] * (len(valList[0]) * 2)

    for i, num1 in enumerate(valList):
        for j, num2 in enumerate(valList):
            if i != j:
                temp_product = [0] * (len(num1) + len(num2))
                carry = 0

                for idx1, digit1 in enumerate(reversed(num1)):
                    for idx2, digit2 in enumerate(reversed(num2)):
                        product_ij = conDict[digit1] * conDict[digit2] + carry
                        carry = product_ij // base
                        temp_product[idx1 + idx2] += product_ij % base

                for idx in range(len(temp_product)):
                    if temp_product[idx] >= base:
                        carry = temp_product[idx] // base
                        temp_product[idx] %= base
                        temp_product[idx + 1] += carry
                print("Temp product:", temp_product)
                product = naive_add(base, [product, list(reversed(temp_product))])
                print("Product:", product)
    while len(product) > 1 and product[-1] == 0:
        product.pop()

    return "".join([vertDict[str(i)] for i in reversed(product)])


if __name__ == "__main__":
    assert naive_add(36, ["1A2", "2B3", "4C4"]) == "7X9", "Incorrect addition"
    print("ADDITION PASSED")
    # print(multiply(36, ["1A2", "2B3", "4C4"]))
    assert multiply(36, ["1A2", "2B3", "4C4"]) == "CSX37SO", "Incorrect multiplication"
    # example = multiply(36, ["1A2", "2B3",
