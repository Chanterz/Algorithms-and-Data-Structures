import os
import collections

components = collections.OrderedDict(
    {1: ("атом", []), 2: ("молекула", []), 3: ("клетка", []), 4: ("дерево", []), 5: ("металл", [])})


def write_to_file(components):
    with open(os.path.join(os.getcwd(), "components.txt"), encoding="utf-8", mode="w") as file:
        for key, value in components.items():
            file.write("{}:{};".format(key, value[0]))
        file.write("\n")

        for key, value in components.items():
            containing = [0 for _ in range(len(components))]
            if len(value[1]) == 0:
                file.write(" ".join(map(str, containing)))
                file.write("\n")
            else:
                for i in value[1]:
                    containing[i - 1] = 1
                file.write(" ".join(map(str, containing)))
                file.write("\n")


def read_from_file(path):
    comp = {}
    with open(path, encoding="utf-8", mode="r") as file:
        dct = file.readline()

        for item in dct.split(";"):
            item = item.split(":")
            if item[0] == "\n":
                break
            comp[int(item[0])] = (item[1], [])

        for i in range(len(dct)):
            lst = file.readline()
            lst = lst.split(" ")
            for idx, val in enumerate(lst):
                if val == "1":
                    comp[i + 1][1].append(idx + 1)
    return comp


def print_composition(item, first, components):
    if len(item[1]) == 0:
        print("\t" + item[0])
    else:
        print("\t" + item[0]) if not first else print("{} состоит из:".format(item[0]))
        for i in item[1]:
            print_composition(components[i], False, components)


def implement_components(components):
    for i in components:
        components[i][1].clear()
    for key, value in components.items():
        print("{} состоит из (введите через пробел номера из предложенных):".format(value[0]))
        for i in components:
            if i != key:
                print("{}. {}".format(i, components[i][0]))
        contains = input(">>>")
        if len(contains) != 0:
            contains = list(map(int, contains.split(" ")))
        components[key][1].extend(contains)


comp = read_from_file("C:\\Users\\BetaB\\PycharmProjects\\Algorithms-and-Data-Structures\\2labcomponents.txt")
# implement_components(comp)

comp = collections.OrderedDict(
    {1: ("атом", []), 2: ("молекула", []), 3: ("клетка", []), 4: ("дерево", []), 5: ("металл", [])})
implement_components(comp)
for key, value in comp.items():
    print_composition(value, True, comp)
write_to_file(comp)
