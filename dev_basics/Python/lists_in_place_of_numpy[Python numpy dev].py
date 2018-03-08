'''
    I need to write the function dot( L, K ) that should output the dot product of the lists L and K. If these two input lists are not of equal length, dot should output 0. If these two lists are both empty, dot also should output 0. You should assume that the input lists contain only numeric values.
'''
def dot(K, L):
   if len(K) != len(L):
      return 0
   return sum(i[0] * i[1] for i in zip(K, L))
    #If either of the lists is empty, zip(K, L) will return []. Then, by definition, sum([]) will give you zero.

def larger_dot(list_of_listsA, list_of_listsB):
    '''assuming both are square and the same size'''
    b_transposed = zip(list_of_listsB)
    result = []
    for ind_row in range(len(list_of_listsA)):
        result.append([])
        for ind_column in range(len(list_of_lists_B[0])):
            result[ind_row].append(dot(list_of_listsA[ind_row]), b_transposed[ind_column])
    return result
