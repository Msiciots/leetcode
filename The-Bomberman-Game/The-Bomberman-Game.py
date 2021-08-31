#!/bin/python3

import math
import os
import random
import re
import sys
def bomb(len_r,len_c,grid):
    grid_tmp = [''.join(['O'] * len_c)] * len_r
    for r in range(len_r):
        for c in range(len_c):
            if grid[r][c] == "O":
                if r-1 >= 0:
                    grid_tmp[r-1] = grid_tmp[r-1][:c]+'.'+grid_tmp[r-1][c+1:]
                if r+1 < len_r:
                    grid_tmp[r+1] = grid_tmp[r+1][:c]+'.'+grid_tmp[r+1][c+1:]
                if c-1 >= 0:
                    grid_tmp[r] = grid_tmp[r][:c-1]+'.'+grid_tmp[r][c:]
                if c+1 < len_c:
                    grid_tmp[r] = grid_tmp[r][:c+1]+'.'+grid_tmp[r][c+2:]
                grid_tmp[r] = grid_tmp[r][:c]+'.'+grid_tmp[r][c+1:]

    # for r in grid_tmp:
        # print(r)
    return grid_tmp

def bomberMan(n, grid):
    # Write your code here
    len_r = len(grid)
    len_c = len(grid[0])
    grid_tmp = [''.join(['O'] * len_c)] * len_r
    if n%2 == 0:
        return grid_tmp
    if n==1:
        return grid
    # 3 , 5 ,7, 9 
    n //= 2
    if n%2 == 1:
        grid = bomb(len_r,len_c,grid)
    else:
        grid = bomb(len_r,len_c,grid)
        grid = bomb(len_r,len_c,grid)

    return grid
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)
    # for r in result:
        # print(r)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

