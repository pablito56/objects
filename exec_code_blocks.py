#! /usr/bin/env python
#-*- coding: utf-8 -*-
u'''
Created on Nov 13, 2012
@author: pev
'''
from sys import argv
from os import path 
import code
import readline
import atexit
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import Terminal256Formatter


FORMATTER_STYLE = 'colorful'
RELOAD_BLOCKS_CMD = '%reload_blocks'
BLANKS = 1


class HistoryConsole(code.InteractiveConsole):
    def __init__(self, locals=None, filename="<console>",
                 histfile=path.expanduser("~/.demo_console_history")):
        code.InteractiveConsole.__init__(self, locals, filename)
        self.init_history(histfile)

    def init_history(self, histfile):
#        readline.parse_and_bind("tab: complete")
        if hasattr(readline, "read_history_file"):
            try:
                readline.read_history_file(histfile)
            except IOError:
                pass
            atexit.register(self.save_history, histfile)

    def save_history(self, histfile):
        readline.write_history_file(histfile)

class DemoConsole(HistoryConsole):
    def __init__(self, files=None, blanks=1, *args, **kargs):
        if not files:
            self.files = ["example{0}.py".format(num) for num in xrange(999)]
        else:
            self.files = files
        self.blanks = blanks
        self.reload_blocks()
        HistoryConsole.__init__(self, *args, **kargs)
#        super(DemoConsole, self).__init__(*args, **kargs)

    def reload_blocks(self, new_files=[]):
        if new_files:
            self.files = new_files
        self.code_block = []
        self.is_executable = False
        self.blocks = get_code_blocks(self.files, self.blanks)
        self.blocks_iter = iter(self.blocks)
        self.write("Loaded {0} code blocks\n".format(len(self.blocks)))

    def push(self, line):
#        from ipdb import set_trace; set_trace()
        if not line.strip() and len(self.buffer) == 0:
            # Accumulate next code blocks until they are executable (and execute them)
            while True:
                try:
                    b = self.blocks_iter.next()
                except StopIteration:
                    if self.code_block:
                        b = []
                        self.is_executable = True
                        is_compilable = True
                    else:
                        self.write("No more code blocks available. Execute '{0}' to restart\n".format(RELOAD_BLOCKS_CMD))
                        return False
                else:
                    try:
                        is_compilable = code.compile_command("".join(b), "<stdin>", "exec") is not None
                    except SyntaxError:
                        is_compilable = False
                if self.is_executable and is_compilable:
                    code_to_print = highlight("".join(self.code_block),
                                              PythonLexer(),
                                              Terminal256Formatter(style=FORMATTER_STYLE))
                    print code_to_print
#                    print "PUSHING '", "".join(self.code_block), "' ->",
#                    for code_line in self.code_block:
#                        res = HistoryConsole.push(self, code_line[:-1] if code_line[-1] == "\n" else code_line)
#                    HistoryConsole.push(self, "".join(self.code_block))
#                    self.buffer = [line[:-1] if line[-1] == "\n" else line for line in self.code_block]
                    map(self.push, [line[:-1] if line[-1] == "\n" else line for line in self.code_block if line != '\n'])
#                    self.runsource("".join(self.code_block), self.filename)
#                    print res
                    HistoryConsole.push(self, "\n")
#                    super(DemoConsole, self).push("".join(self.code_block))
                    self.code_block = b
                    self.is_executable = True
                    return False
                if self.code_block:
                    self.code_block.extend(['\n'] * self.blanks)
                self.code_block.extend(b)
                self.is_executable = code.compile_command("".join(self.code_block), "<stdin>", "exec") is not None
            return False
        elif line.strip().startswith(RELOAD_BLOCKS_CMD) and len(self.buffer) == 0:
            self.reload_blocks(line.strip().split(" ")[1:])
            return False
        return HistoryConsole.push(self, line)
#        return super(DemoConsole, self).push(line)


def clean_block_trail(block):
    '''Remove last empty last as well as last break line of given code block
    '''
#    print "CLEANING"
#    print ">>> ", block, " <<<"
    while True:
#        print ">>> ", block[-1], "|", block[-1].strip(), " <<<"
        if not block[-1].strip():
            block.pop(-1)
        else:
            break
    block[-1] = block[-1].replace("\n", "")
#    print ">>> ", block[-1], " <<<"
    return block


def get_code_blocks(files, blanks=1):
    '''Retrieve a list of code blocks; lists of strings containing lines of code
    :param files: list of files to read
    :return list of lists of single line strings
    '''
    blocks = []
    files_count = 0
    for fil in files:
        if not path.isfile(fil):
            break
        files_count += 1
        with open(fil) as f:
            curr_block = []
            found_blanks = 0
            for line in f:
                if not line.strip():
                    found_blanks += 1
                    if curr_block and found_blanks == blanks:
                        blocks.append(clean_block_trail(curr_block))
                        curr_block = []
                        found_blanks = 0
                    elif curr_block:
                        curr_block.append(line)
                else:
                    found_blanks = 0
                    curr_block.append(line)
            if curr_block:
                blocks.append(clean_block_trail(curr_block))
                curr_block = []
#    print "Loaded {0} code blocks of {1} files".format(len(blocks), files_count)
    return blocks


def main(inargv=argv):
#    console = code.InteractiveConsole()
    console = DemoConsole(files=inargv[1:], blanks=BLANKS)
    try:
        import readline
    except ImportError:
        pass
    console.interact()


if __name__ == '__main__':
    main(argv)
