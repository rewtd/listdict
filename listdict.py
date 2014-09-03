from collections import OrderedDict
import pyparsing as pp


# Minimal BNF. See below for a more comprehensive BNF
bnf = """
listdict
    [ keyvaluepairs ]
    'listdict()'

keyvaluepairs
    keyvaluepair
    keyvaluepairs , keyvaluepair

keyvaluepair
    key : value

"""

key = pp.quotedString()
colon = pp.Literal(':').suppress()
value = pp.quotedString()
keyvaluepair = pp.Group(key + colon + value)
keyvaluepairs = pp.delimitedList(keyvaluepair, ',')
lsquare = pp.Literal('[').suppress()
rsquare = pp.Literal(']').suppress()
empty = pp.Literal('listdict()').suppress()

parser = (lsquare + keyvaluepairs + rsquare | empty)


class listdict(OrderedDict):
    """
    listdict is a Pythonic way of representing an OrderedDict.

    What dict is to set, so listdict is to list; ordered, and denoted with
    colon-separated key-value pairs like dict, and wrapped in square brackets like
    list.

    >>> ordered_dict = loads("['eggs': 'spam', 'ham': 'spam']")
    >>> ld = listdict(ordered_dict)
    >>> repr(ld)
    "['eggs': 'spam', 'ham': 'spam']"

    """
    def __repr__(self):
        return dumps(self)


def loads(listdictrepr):
    """
    Converts "['eggs': 'spam']" to OrderedDict([('eggs': 'spam')])

    >>> loads("['eggs': 'spam', 'ham': 'spam']")
    OrderedDict([('eggs', 'spam'), ('ham', 'spam')])

    >>> loads('listdict()')
    OrderedDict()

    """
    data = parser.parseString(listdictrepr)
    if data:
        evil = ((eval(k), eval(v)) for k, v in data)
        return OrderedDict(evil)
    else:
        return OrderedDict()


def dumps(ordered_dict):
    """
    Converts OrderedDict([('eggs', 'spam')]) to "['eggs': 'spam']"

    >>> ordered_dict = OrderedDict([('eggs', 'spam'), ('ham', 'spam')])
    >>> dumps(ordered_dict)
    "['eggs': 'spam', 'ham': 'spam']"

    >>> dumps(OrderedDict([]))
    'listdict()'

    """
    if not ordered_dict:
        return 'listdict()'
    pairs = [': '.join((repr(k), repr(v))) for k, v in ordered_dict.items()]
    return '[' + ', '.join(pairs) + ']'


# bnf = """
# listdict
#     [ keyvaluepairs ]
#     'listdict()'
#
# keyvaluepairs
#     key : value
#     keyvaluepairs , key : value
#
# key
#     bool
#     bytestring
#     float
#     integer
#     keytuple
#     none
#     unicode
#
# value
#     bool
#     bytestring
#     dict
#     float
#     integer
#     list
#     listdict
#     none
#     set
#     string
#     valuetuple
#     unicode
#
# keytuple
#     ( tuplekeys )
#     ()
#
# tuplekeys
#     key ,
#     key , keys
#
# keys
#     key
#     key , keys
#
# dict
#     { keyvaluepairs }
#     {}
#
# list
#     [ values ]
#     []
#
# values
#     value
#     value , values
#
# set
#     { values }
#     'set()'
#
# valuetuple
#     ( tuplevalues )
#     ()
#
# tuplevalues
#     value ,
#     value , values
#
# """
