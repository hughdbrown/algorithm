def queensproblem(solution, rows, columns):
    if len(solution) == rows:
       yield solution
    else :
        max_row_so_far = len(solution)
        for row in range(max_row_so_far, rows):
            for col in add_one_queen(row, columns, solution):
                for x in queensproblem(solution + [col], rows, columns):
                   yield x
            else:
                break
    return
 
def add_one_queen(new_row, columns, solution):
    for new_column in range(columns):
        if not conflict(new_row, new_column, solution):
            yield new_column
    return

def conflict(new_row, new_column, solution):
    return any(solution[row]       == new_column or
               solution[row] + row == new_column + new_row or
               solution[row] - row == new_column - new_row
               for row in range(new_row))

solutions = []
for i,solution in enumerate(queensproblem(solutions, 8, 8)):
    print i, solution
