
def beep_boop():
    for i in range(0, 1001):
        if i == 0:
            continue

        if i % 100 == 0:
            print('beep boop')
            continue
        elif i % 20 == 0:
            print('boop')
            continue
        elif i % 5 == 0:
            print('beep')
            continue


if __name__ == '__main__':
    beep_boop()

# python beep_boop.py
