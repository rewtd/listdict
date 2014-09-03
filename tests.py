import doctest
import sys
import listdict


def test_doctests(verbose=False):
    failures, tests = doctest.testmod(listdict, verbose=verbose)
    assert not failures, '{} of {} doctests failed'.format(failures, tests)


if __name__ == '__main__':
    verbose = '-v' in sys.argv
    test_doctests(verbose=verbose)
