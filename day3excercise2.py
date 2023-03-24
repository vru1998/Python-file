class Vehicle:

    def __init__(self, color, type, year_of_market_release):
        self.color = color
        self.type = type
        self.year_of_market_release = year_of_market_release


def main(year_of_market_release=None):
    v1 = Vehicle("red", "Mercedes", 2010)
    v2 = Vehicle("black", "BMW", 2012)
    v3 = Vehicle("blue", "Audi", 2013)
    v4 = Vehicle("white", "TATA", 2014)
    list1 = [v1, v2, v3, v4]
    dict1 = {}

    for i in list1:
        print(i, year_of_market_release)
        if i.year_of_market_release in dict1.keys():
            dict1[i.year_of_market_release].append(i)
        else:
            dict1[i.year_of_market_release] = [i]

    for key, value in dict1.items():
        print(key)
        for item in value:
            print(item.type)


if __name__ == "__main__":
    main()