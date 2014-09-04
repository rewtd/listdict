listdict
========

The listdict is a Pythonic way of representing an OrderedDict.

What the dict is to the set, so the listdict is to the list; ordered, and
denoted with colon-separated key-value pairs like dict, and wrapped in square
brackets like list. e.g. ['eggs': 'spam', 'ham': 'spam']

I think it's time the OrderedList is promoted to a first-class citizen of
Python's data types, as the set has been. The OrderedList is extremely useful,
especially when working with JSON, and its syntax is rather clunky at the
moment. The listdict is an attempt to remedy that.

Usage
-----

Represent an OrderedDict as a listdict: ::

    >>> from collections import OrderedDict
    >>> from listdict import listdict
    >>> ordered_dict = OrderedDict([('eggs', 'spam'), ('ham', 'spam')])
    >>> ld = listdict(ordered_dict)
    >>> repr(ld)
    "['eggs': 'spam', 'ham': 'spam']"

Or, use json-style `dumps`: ::

    >>> from listdict import dumps
    >>> ordered_dict = OrderedDict([('eggs', 'spam'), ('ham', 'spam')])
    >>> dumps(ordered_dict)
    "['eggs': 'spam', 'ham': 'spam']"

Inversely, use `loads` to convert a listdict representation into an
OrderedDict: ::

    >>> from listdict import loads
    >>> loads("['eggs': 'spam', 'ham': 'spam']")
    OrderedDict([('eggs', 'spam'), ('ham', 'spam')])

