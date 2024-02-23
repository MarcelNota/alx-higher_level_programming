#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    # for printing
    for name in sorted(dir(hidden_4)):
        # for numbers with __ only_
        if name[:2] != '__':
            print("{}".format(name))
