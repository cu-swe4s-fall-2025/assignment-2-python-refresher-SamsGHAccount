def get_column(file_name, query_column, query_value, result_column = 1):
    f = open(file_name, 'r')

    toReturn = []

    for l in f:
        A = l.rstrip().split(',')
        if(A[query_column] == query_value):
            toReturn.append(A[result_column])

    return toReturn
