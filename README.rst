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
