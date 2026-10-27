def custom_sort(int_list):
    """Sorts a list of integers using Bubble Sort algorithm.
    The original list is kept intact. 
    Returns new sorted list."""
    
    n = len(int_list)
    sorted_list = int_list.copy()
    
    comparisons = 0 
    
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if sorted_list[j] > sorted_list[j + 1]:  
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                
    return sorted_list, comparisons