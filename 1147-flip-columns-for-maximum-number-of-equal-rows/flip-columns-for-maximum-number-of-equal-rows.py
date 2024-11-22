class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = defaultdict(int)

        for row in matrix:
            row_key = tuple(row)

            if row[0]:
                # Check Flipped Tuples
                new_list = []
                for n in row:
                    if n == 1:
                        new_list.append(0)
                    else:
                        new_list.append(1)
                row_key = tuple(new_list)


            count[row_key] += 1

        return max(count.values())
