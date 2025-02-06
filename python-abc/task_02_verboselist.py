#!/usr/bin/env python3

class VerboseList(list):
    """
    A subclass of list that provides verbose output
    when modifying the list (append, extend, remove, pop).
    """
    def append(self, item):
        """Append an item to the list and print a message."""
        super().append(item)
        print(f"Added {item} to the list.")
    
    def extend(self, iterable):
        """Extend the list with elements from an iterable and print a message."""
        items_count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {items_count} items.")
    
    def remove(self, item):
        """Remove an item from the list and print a message."""
        print(f"Removed {item} from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        """Pop an item from the list at the given index and print a message."""
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)

# Example usage of VerboseList
verbose_list = VerboseList([1, 2, 3])

verbose_list.append(4)
verbose_list.extend([5, 6])
verbose_list.remove(3)
verbose_list.pop()
verbose_list.pop(0)
