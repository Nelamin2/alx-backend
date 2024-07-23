#! /usr/bin/ env python3
"""
Hypermedia pagination.
"""
import csv
import math
from typing import List, Dict, Any, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Retrieves a page of data.
        """
        isinstance(type(page), int) and isinstance(type(page_size), int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return {
                "index": 0,
                "data": [],
                "page_size ": page_size,
                "page": page,
                "next_page": None,
                "prev_page": None,
                "total_pages": 0}
        return {
            "index": start,
            "data": data[start:end],
            "page_size": page_size,
            "page": page,
            "next_page": page + 1 if end < len(data) else None,
            "prev_page": page - 1 if start > 0 else None,
            "total_pages": math.ceil(len(data) / page_size)
        }
