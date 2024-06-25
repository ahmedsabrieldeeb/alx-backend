#!/usr/bin/env python3
""" Simple helper function """


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list of items

    Args:
        page (int): page number
        page_size (int): number of items per page

    Returns:
        tuple: a tuple of size two containing start index and end index
    """
    return ((page - 1) * page_size, page * page_size)
