#!/usr/bin/python3
if __name__ == "__main__":
    hidden = sorted(dir('hidden_4'))
    for i in range(0, len(hidden)):
        if hidden[i][:2] != "__":
            print("{}".format(hidden[i]))
