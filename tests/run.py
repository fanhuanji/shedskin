#!/usr/bin/env python
import traceback, sys, os, time, subprocess, glob, getopt

def usage():
    print "'-l': give individual test numbers"
    print "'-r': reverse test order"
    print "'-f': break after first failure"
    sys.exit()

def parse_options():
    args, options = [], set()
    for arg in sys.argv[1:]:
        if arg.startswith('-'):
            options.update(arg[1:])
        else: 
            args.append(int(arg))
    return args, options

def test_numbers(args, options):
    if 'l' in options:
        test_nrs = args

    elif len(args) == 1:
        test_nrs = [args[0]]
    elif len(args) == 2:
        if args[0] > args[1]:
            args[0], args[1] = args[1], args[0]
            options.add('r')
        test_nrs = range(args[0],args[1])
    else:
        test_nrs = [int(os.path.splitext(f)[0]) for f in glob.glob('*.py') if f != 'run.py']

    if 'r' in options:
        test_nrs.reverse()

    return test_nrs

def main():
    args, options = parse_options()
    if 'h' in options:
        usage()

    test_nrs = test_numbers(args, options)
    msvc = 'v' in options

    failures = []
    for test_nr in test_nrs:
        if os.path.exists('%d.py' % test_nr): # XXX
            run_test(test_nr, failures, msvc)
            if failures and 'f' in options:
                break
            print

    if not failures:
        print '*** no failures, yay!'
    else:
        print '*** tests failed:', len(failures)
        print failures

def run_test(test_nr, failures, msvc):
    try:
        print '*** test:', test_nr
        if msvc: 
            assert os.system('shedskin -v %d' % test_nr) == 0
        else:
            assert os.system('shedskin -m Makefile.%d %d' % (test_nr, test_nr)) == 0
        if msvc:
            assert os.system('nmake /C /S clean') == 0
            assert os.system('nmake /C /S') == 0
            command = '.\\%d' % test_nr
        else:
            assert os.system('make clean; make -f Makefile.%d' % test_nr) == 0
            command = './%d' % test_nr
        check_output(command, test_nr)
        print '*** success:', test_nr
    except AssertionError:
        print '*** failure:', test_nr
        traceback.print_exc()
        failures.append(test_nr)

def get_output(command):
    com = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    output = ''.join(com.readlines())
    com.close()
    return output

def check_output(command, test_nr):
    native_output = get_output(command)
    cpython_output = get_output('python %d.py' % test_nr)
    if native_output != cpython_output:
        print 'output:'
        print native_output
        print 'expected:'
        print cpython_output
        raise AssertionError

if __name__ == '__main__':
    main()
