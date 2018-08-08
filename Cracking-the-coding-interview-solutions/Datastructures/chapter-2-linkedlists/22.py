def find_n_to_last(node, n):
    """Returns nth to last element from the linked list."""
    def find_n_to_last_helper(node, n, count):
        if not node:
            return None

        result = find_n_to_last_helper(node.next, n, count)
        if count[0] == n:
            result = node.data

        count[0] += 1 
        return result 

    count = [0]
    return find_n_to_last_helper(node, n, count)