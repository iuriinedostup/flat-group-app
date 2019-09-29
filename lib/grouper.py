from collections import defaultdict
from functools import partial
from itertools import groupby
from typing import Iterable


class FlatGroupError(Exception):
    pass


class FlatGroup:
    """
    A class that allows nesting data using provided keys
    """

    def __init__(self, keys):
        """
        Check if keys don't have duplicates
        :param keys:
        """
        self.keys = keys
        if not len(keys) == len(set(keys)):
            raise FlatGroupError('Provided keys have duplicates')

    def keyfunc(self, key: str):
        """
        Helper function to fetch value from dictionary by key
        :param key:
        :return:
        """
        return partial(lambda k, row: row[k], key)

    def group(self, data, keys=None) -> Iterable:
        """
        Apply nesting logic on data
        :param data:
        :param keys:
        :return:
        """
        keys = keys or self.keys

        remain_keys = keys.copy()

        key = remain_keys.pop(0)
        keyfunc = self.keyfunc(key)

        result = defaultdict(list)

        try:
            data = sorted(data, key=keyfunc)
            for value, grouped_data in groupby(data, key=keyfunc):
                leaf = []

                for row in grouped_data:
                    row.pop(key)
                    leaf.append(row)

                if remain_keys:
                    leaf = self.group(leaf, remain_keys)

                result[value] = leaf
        except KeyError as e:
            raise FlatGroupError("%s is missing in data" % e) from None

        return result
