import json
from itertools import islice
#
# Area of rectangles
#

class Solution:
    def someFunc(self, nums: list[list])-> int:
        if not nums:
            return 0
        
        max_i = nums[0][0] # найти максимальную координату
        for line in nums:
            for num in line:
                max_i = max(max_i, num)

        board = [[None for _ in range(max_i)] for _ in range(max_i)] # координатая плоскасть для дальнейшего расчета
        
        max_area = 0
        for coords in nums: # заполнить координатный лист площадью
            s_storage = [[(coords[2]-coords[0]) * (coords[3]-coords[1])]] # первый массив указывает принадлежность к фигуре, второй хранит значение площади фигуры
            max_area = max(max_area, s_storage[0][0]) # заодно созраняем максимальную площадь фигур без пересечения
            for x in range(coords[0], coords[2]):
                for y in range(coords[1], coords[3]):
                    board[y][x] = s_storage # каждой координатной ячейке принадлежащей к данно1 фигуре даём ссылку на хранилище

        for y in range(max_i): # проходим всю координатую плоскость 
            for x in range(max_i):
                if not board[y][x]: # эта ясейка не принадлежит никакой фигуре
                    continue

                check = [(y-1, x), (y+1, x), (y, x+1), (y, x-1)] # проверяем смежные ячейки слева, сверху...
                for (i, j) in check:
                    # проверяем 1. ячейка в координатной плоскасти
                    # 2. принадлежит какой-то фигуре 3. принадлежит другой фигуре
                    if (i>=0 and i<max_i and j>=0 and j<max_i)\
                            and board[i][j]\
                            and not (board[y][x][0] is board[i][j][0]):
                        board[y][x][0][0] += board[i][j][0][0] # складываем площади двух разных фигур
                        board[i][j][0] = board[y][x][0] # объединяем две фигуры, все ячейки в них теперь указывают на одну фигуру
                        max_area = max(max_area, board[y][x][0][0]) # проверяи не нашли ли новый максимум
        
        return max_area
    

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 1
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.someFunc(json.loads(args_raw[0]))    

            f_out.write(json.dumps(res) + '\n')
