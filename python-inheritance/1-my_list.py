#!/usr/bin/python3
""" Nameless module containing MyList class """


class MyList(list):
    """MyList Class.
    """

    def print_sorted(self):
        """Sorts the contents of the list class and returns them"""

        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)

        return self
