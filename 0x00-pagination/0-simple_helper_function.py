#!/usr/bin/env python3
"""
a script that takes two integer arguments page and page_size
and returns a tuple containing two integers
start index and end index corresponding to the range of indexes
to return in a list for those particular pagination parameters
"""


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing a start index and an end index"""
    return ((page - 1) * page_size, page * page_size)
