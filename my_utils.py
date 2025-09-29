def get_column(file_name, query_column, query_value, result_column = 1, info_ret = None):
    f = open(file_name, 'r')

    toReturn = []
    
    for l in f:
        A = l.rstrip().split(',')
        if(A[query_column] == query_value):
            toReturn.append(A[result_column])

    return_int = [int(float(x)) for x in toReturn]

    if(info_ret=='mean'):
        return (sum(return_int)/len(return_int))
    elif(info_ret=='median'):
        return_int.sort()
        if(len(return_int)%2==0):
            median = (return_int[len(return_int)//2] + return_int[len(return_int)//2 - 1]) / 2
        else:
            median = return_int[len(return_int)//2]
        return (median)
    elif(info_ret=='stdev'):
        mean = sum(return_int)/len(return_int)
        variance = sum((x - mean) ** 2 for x in return_int) / len(return_int)
        stdev = variance ** 0.5
        return (stdev)
    else:
        return (return_int)
