# I can't really claim much credit for this implementation.
# I found this on the web and I converted it to use python generators.

def queensproblem(solution, rows, columns):
    if len(solution) == rows:
        yield solution
    else :
        for row in range(len(solution), rows):
            for col in add_one_queen(row, columns, solution):
                for x in queensproblem(solution + [col], rows, columns):
                    yield x
            else:
                break
 
def add_one_queen(new_row, columns, solution):
    for new_column in range(columns):
        if not conflict(new_row, new_column, solution):
            yield new_column

def conflict(new_row, new_column, solution):
    return any(solution[row]       == new_column or
               solution[row] + row == new_column + new_row or
               solution[row] - row == new_column - new_row
               for row in range(new_row))

for i,solution in enumerate(queensproblem([], 8, 8)):
    print i, solution
