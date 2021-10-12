def maximal_square(matrix):
    memo = dict()
    best = 0
    for row in reversed(range(len(matrix))):
        for col in reversed(range(len(matrix[0]))):
            if matrix[row][col] == "0":
                continue
            else:
                memo[(row, col)] = 1
                # check if the diagonal elem is in dict
                if (row+1, col+1) in memo:
                    length = memo[(row+1, col+1)]
                    for l in range(1, length+1):
                        if matrix[row][col+l] == "1" and matrix[row+l][col] == "1":
                            memo[(row, col)] += 1
                        else:
                            break
                best = max(best, memo[(row, col)]**2)
    return best