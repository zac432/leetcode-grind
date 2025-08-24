def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into one sorted list.
    
    Args:
        list1: First sorted list
        list2: Second sorted list
    
    Returns:
        A new sorted list containing all elements from both input lists
    """
    merged = []
    i = j = 0
    
    # Compare elements from both lists and add the smaller one
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    # Add remaining elements from list1 (if any)
    while i < len(list1):
        merged.append(list1[i])
        i += 1
    
    # Add remaining elements from list2 (if any)
    while j < len(list2):
        merged.append(list2[j])
        j += 1
    
    return merged


# Example usage
if __name__ == "__main__":
    # Test cases
    list_a = [1, 3, 5, 7, 9]
    list_b = [2, 4, 6, 8, 10]
    
    result = merge_sorted_lists(list_a, list_b)
    print(f"Merged list: {result}")
    
    # Test with different lengths
    list_c = [1, 5, 9, 12]
    list_d = [2, 3, 4, 6, 7, 8, 10, 11]
    
    result2 = merge_sorted_lists(list_c, list_d)
    print(f"Merged list 2: {result2}")
    
    # Test with empty lists
    empty_list = []
    non_empty = [1, 2, 3]
    
    result3 = merge_sorted_lists(empty_list, non_empty)
    print(f"Merged with empty: {result3}")
    
    # Test with duplicate elements
    list_e = [1, 3, 5, 5, 7]
    list_f = [2, 3, 4, 5, 6]
    
    result4 = merge_sorted_lists(list_e, list_f)
    print(f"Merged with duplicates: {result4}")