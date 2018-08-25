# Uses python3
import sys

def get_change(m):
    '''
    Take the coin with largest value
    '''
    ten = m // 10
    five = (m - ten * 10) // 5
    one = m - ten * 10 - five * 5
    return  one + five + ten

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
