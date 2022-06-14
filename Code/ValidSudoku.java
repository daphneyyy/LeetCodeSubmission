//Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

// Each row must contain the digits 1-9 without repetition.
// Each column must contain the digits 1-9 without repetition.
// Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
// Note:
// A Sudoku board (partially filled) could be valid but is not necessarily solvable.
// Only the filled cells need to be validated according to the mentioned rules.

class Solution {
    private static final int SIZE = 9;
    private static final int FACTOR = 3;

    public boolean isValidSudoku(char[][] board) {
        return (checkCol(board) && checkRow(board)) && check3by3(board);
    }

    public boolean checkRow(char[][] board) {
        for (int row = 0; row < SIZE; row++) {
            boolean[] checker = new boolean[SIZE];
            for (int col = 0; col < SIZE; col++) {
                if (board[row][col] != ".".charAt(0)) {
                    if (checker[Integer.parseInt(String.valueOf(board[row][col])) - 1]) {
                        return false;
                    } else {
                        checker[Integer.parseInt(String.valueOf(board[row][col])) - 1] = true;
                    }
                }
            }
        }
        return true;
    }

    public boolean checkCol(char[][] board) {
        for (int col = 0; col < SIZE; col++) {
            boolean[] checker = new boolean[SIZE];
            for (int row = 0; row < SIZE; row++) {
                if (board[row][col] != ".".charAt(0)) {
                    if (checker[Integer.parseInt(String.valueOf(board[row][col])) - 1]) {
                        return false;
                    } else {
                        checker[Integer.parseInt(String.valueOf(board[row][col])) - 1] = true;
                    }
                }
            }
        }
        return true;
    }

    public boolean check3by3(char[][] board) {
        for (int row = FACTOR; row < SIZE + FACTOR; row += FACTOR) {
            for (int col = FACTOR; col < SIZE + FACTOR; col += FACTOR) {
                boolean[] checker = new boolean[SIZE];
                for (int r = row - FACTOR; r < row; r++) {
                    for (int c = col - FACTOR; c < col; c++) {
                        if (board[r][c] != ".".charAt(0)) {
                            if (checker[Integer.parseInt(String.valueOf(board[r][c])) - 1]) {
                                return false;
                            } else {
                                checker[Integer.parseInt(String.valueOf(board[r][c])) - 1] = true;
                            }
                        }
                    }
                }
            }
        }
        return true;
    }
}
