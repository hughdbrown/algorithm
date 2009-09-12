#!/usr/bin/env python
from __future__ import with_statement

import hashlib
import collections 

def dofile(filename):
    def repeatedkeys(x):
        d = collections.defaultdict(int)
        for xx in x:
            key = xx[1]
            d[key] += 1
        return [key for key in d if d[key] > 1]
    def repeatedlines(x, repeated):
        d = collections.defaultdict(list)
        for t in x:
            key = t[1]
            if key in repeated:
                d[key].append(t[0])
        return d
    def match(linesets):
        # Match algorithm is not quite right
        # It can match segments of different lengths, 
        # meaning there is a match at the start
        # but not over the whole length
        def runlength(linesets, item, i):
            run = []
            while i < len(linesets) and item in linesets[i]:
                run.append(item)
                i += 1
                item += 1
            return run
        def removerun(linesets, i, run):
            for r in run:
                linesets[i].remove(r)
                i += 1
        matches = []
        for i, lineset in enumerate(linesets):
            runs = []
            for item in lineset:
                run = runlength(linesets, item, i)
                if len(run) >= 3:
                    runs.append(run)
                removerun(linesets, i, run)
            if len(runs) > 1:
                matches.append(runs)
        return matches
    def process_matches(filename, matches, rawlines):
        print filename
        for m in matches:
            # print the line numbers
            for mm in m:
                print mm
            # print the text of the match
            for lineno in m[0]:
                print rawlines[lineno]
            print
    with open(filename) as f:
        #rawlines = [line.rstrip() for line in f if len(line.rstrip())]
        rawlines = [line.rstrip() for line in f]
        lines_with_hashes = [(i, hashlib.md5(line).hexdigest(), line) for i, line in enumerate(rawlines)]
        lines_with_repeated_keys = repeatedkeys(lines_with_hashes)
        repeated_lines = repeatedlines(lines_with_hashes, lines_with_repeated_keys)
        matches = match(sorted(repeated_lines.values()))
        process_matches(filename, matches, rawlines)
        
if __name__ == '__main__':
    import sys
    import glob
    for arg in sys.argv[1:]:
        for filename in glob.glob(arg):
            dofile(filename)
