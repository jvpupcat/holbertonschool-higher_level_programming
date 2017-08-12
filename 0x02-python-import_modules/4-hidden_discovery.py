#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    store_hid = dir(hidden_4)
    for x in store_hid:
        if x[:2] != '__':
            print(x)
