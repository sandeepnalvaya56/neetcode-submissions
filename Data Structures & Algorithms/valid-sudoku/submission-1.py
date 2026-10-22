class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # placeholders for each hashset
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if element == ".":
                    continue
# rows[r] contains the elements in row r
                if element in rows[r]:  
                    return False
                else:
                    rows[r].add(element)
# columns[c] contains the elements in column c
                if element in columns[c]:  
                    return False
                else:
                    columns[c].add(element)
# " //3 " technique downsizes the array from 9*9 to 3*3, 
# then row*num_cols+col formula flattens 2d array of box coordinates into 1d array of box numbers"
                
                box_row = r // 3 # downsizing
                box_col = c // 3 # downsizing
                b = box_row * 3 + box_col # flattening
# boxes[b] contains the elements in box b
                if element in boxes[b]:  
                    return False
                else:
                    boxes[b].add(element)

        return True