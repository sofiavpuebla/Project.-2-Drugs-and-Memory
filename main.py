import src.getInfo as ex
from src.parser import *


def main():
    args=parser()
    country=args.country
    index=args.index
    attribute=args.attribute
    ex.filterCountry(country)
    print(ex.getAttributeIndex(country,attribute))
    print(ex.getIndex(country,index))


if __name__ == "__main__":
    main()

