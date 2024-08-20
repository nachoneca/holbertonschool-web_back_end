##!/usr/bin/env python3


import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> tuple:
    """Func that takes the page and page size, to return the
intex of the starting element and the ending element"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Func that get page and page size, uses the func
        index_range to get all the data inside that range"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if len(data) < end_index:
            return []
        total_data = data[start_index:end_index]
        return total_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Func that gives info:
        -page_size
        -page
        -data
        -next_page
        -prev_page
        -total_pages"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        db_len = len(self.dataset())
        total_pages = math.ceil(db_len / page_size)
        return {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if not page >= total_pages else None,
            'prev_page': page - 1 if not page <= 1 else None,
            'total_pages': total_pages
        }