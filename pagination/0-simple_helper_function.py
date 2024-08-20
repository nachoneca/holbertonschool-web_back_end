#!/usr/bin/env python3
"""Func that takes the page and page size, to return the
intex of the starting element and the ending element"""


def index_range(page: int, page_size: int) -> tuple:
    """Func that takes the page and page size, to return the
intex of the starting element and the ending element"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
