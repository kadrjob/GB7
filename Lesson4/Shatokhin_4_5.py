from utils import currency_rates as cr


def main(argv):
    if len(argv) > 1:
        return cr(argv[1])
    else:
        return cr(argv[0])


if __name__ == "__main__":
    import sys

    print(main(sys.argv))
    exit(0)
