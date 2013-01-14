#! /usr/bin/env python
#-*- coding: utf-8 -*-
u'''
Created on Nov 13, 2012
@author: pev
'''
from sys import argv


def exec_code_blocks(files):
    if not files:
        files = ["example{0}.py".format(num) for num in xrange(0, 9)]
    blocks = []
    curr_block = []
    for fil in files:
        with open(fil) as f:
            for line in f:
                if not line.strip():
                    if curr_block:
                        blocks.append(curr_block)
                        curr_block = []
                else:
                    curr_block.append(line)
            else:
                if curr_block:
                    blocks.append(curr_block)
                    curr_block = []
    else:
        if curr_block:
            blocks.append(curr_block)
            curr_block = []
    prog_locals = {}
    prog_globals = {}
    try:
        for b in blocks:
            code_to_print = "".join(['>>> ' + line for line in b])
            print code_to_print,
            right_code = "".join(b)
            exec right_code in prog_globals, prog_locals
            for k in prog_locals:
                if k not in prog_globals:
                    prog_globals[k] = prog_locals[k]
            input = raw_input('\n$ ')
            while True:
                if not input.strip():
                    break
                if input == "exit":
                    exit(0)
                try:
                    exec input in prog_globals, prog_locals
                except Exception, e:
                    print e.__class__.__name__ + ":", e
                for k in prog_locals:
                    if k not in prog_globals:
                        prog_globals[k] = prog_locals[k]
                input = raw_input('\n$ ')
    except (KeyboardInterrupt, EOFError):
        print "EXITING ON USER REQUEST"


if __name__ == '__main__':
    exec_code_blocks(argv[1:])
