#!/usr/bin/env python3
import csv
import math
from typing import List


class Server:
    """
    Server class to paginate a database of popular baby names. """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # avoid header

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> tuple:
        """
        Returns a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list of items
        """
        return ((page - 1) * page_size, page * page_size)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Takes the page number and page size to return the proper dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = self.index_range(page, page_size)

        try:
            return self.dataset()[start:end]  # return the indexed dataset
        except IndexError:
            return []
