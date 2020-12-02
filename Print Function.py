from __future__ import print_function
import sys, os, time
if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 150:
        for x in range(1,n+1):
            print(x, end='')
