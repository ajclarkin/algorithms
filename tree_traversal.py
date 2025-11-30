#! /usr/bin/python3

# Going to use breadth first search and depth first search to traverse and list the files in tree/

from os import listdir
from os.path import defpath, isfile, join
from collections import deque


def breadthfirst(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)

    while search_queue:
        dir = search_queue.popleft()
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)
            if isfile(fullpath):
                print(file)
            else:
                search_queue.append(fullpath)



def depthfirst(dir):
    for file in sorted(listdir(dir)):
        fullpath = join(dir, file)
        if isfile(fullpath):
            print(file)
        else:
            depthfirst(fullpath)


print("Breadth First Search")
breadthfirst("tree")


print("\nDepth First Search")
depthfirst("tree")
