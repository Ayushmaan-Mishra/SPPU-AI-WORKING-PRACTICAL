def n_queens(n):
    board = [["."] * n for _ in range(n)]
    col = set()
    neg_diag = set()
    pos_diag = set()
    res = []

    def backtrack(r):
        if r == n: 
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        for c in range(n):
            if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
            col.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = 'Q'

            backtrack(r + 1)

            col.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = '.'

    backtrack(0)
    return res

n = int(input("Enter the number of queens: "))
solutions = n_queens(n)

if solutions:
    print(f"\nTotal solutions: {len(solutions)}\n")
    for solution in solutions:
        for row in solution:
            print(row)
        print()  # Blank line between solutions
else:
    print("No solution exists.")
