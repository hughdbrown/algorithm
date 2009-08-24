#!/usr/bin/env python
from __future__ import with_statement

import psyco
psyco.full()

import os, os.path
import glob
from hashlib import sha1
import datetime

def sha_file(filename):
    with open(filename, "rb") as f:
        return sha1(f.read()).hexdigest()

def directory_compare(src, dst):
    dir_count, file_count = 0, 0
    for root, dirs, files in os.walk(src):
        root_less = root[len(src)+1:]
        for dir in dirs:
            dir_count += 1
            x = os.path.join(root, dir, "*.*")
            for file in glob.glob(x):
                stem = os.path.join(root_less, dir, file)
                src_file = os.path.join(src, stem)
                dst_file = os.path.join(dst, stem)
                assert(os.path.exists(src_file))
                if not os.path.exists(dst_file):
                    print "Missing: ", dst_file
                elif not os.path.isdir(src_file):
                    file_count += 1
                    src_sha, dst_sha = sha_file(src_file), sha_file(dst_file)
                    if src_sha != dst_sha:
                        print "Difference: ", src_file, dst_file
                    #else:
                    #    print src_sha
    return dir_count, file_count

def check_dir(src, dst):
    s = datetime.datetime.now()
    dir_count, file_count = directory_compare(src, dst)
    e = datetime.datetime.now()
    print src
    print dst
    print "Elapsed: ", (e - s)
    print "%d directories checked" % dir_count
    print "%d files checked" % file_count
    print "*" * 20


if __name__ == '__main__':
    check_dir(r'h:\software\.', r'c:\g_drive\software\.')
