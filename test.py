#Начальная точка
def spawn_point(h, b):
    if random.choice([True, False]):
        if random.choice([True, False]):
            s = (0, random.randint(0, b - 1))
        else:
            s = (h - 1, random.randint(0, b - 1))
    else:
        if random.choice([True, False]):
            s = (random.randint(0, h - 1), 0)
        else:
            s = (random.randint(0, h - 1), b - 1)
    return s

#Конечная точка
def finish_point(s, h, b):
    return h - 1 - s[0], b - 1 - s[1]

def transition_choice(x, y, rm)
    choice_list = []
    if x > 0:
        if not rm[x - 1][y]:
            choice_list.append((x - 1, y))
    if x < len(rm) - 1:
        if not rm[x + 1][y]:
            choice_list.append((x + 1, y))
    if y > 0:
        if not rm[x][y - 1]:
            choice_list.append((x, y - 1))
    if y < len(rm[0]) - 1:
        if not rm[x][y + 1]:
            choice_list.append((x, y + 1))
    if choice_list:
        nx, ny = random.choice(choice_list)
        if x == nx:
            if ny > y:
                tx, ty = x * 2, ny * 2 - 1
            else:
                tx, ty = x * 2, ny * 2 + 1
        else:
            if nx > x:
                tx, ty = nx * 2 - 1, y * 2
            else:
                tx, ty = nx * 2 + 1, y * 2
        return nx, ny, tx, ty
    else:
        return -1, -1, -1, -1

#Лабиринт и матрица
def create_labyrinth(h=5, b=5):
    reach_matrix = []
    for i in range(h):  # создаём матрицу достижимости ячеек
        reach_matrix.append([])
        for j in range(b):
            reach_matrix[i].append(False)
    transition_matrix = []
    for i in range(h * 2 - 1):  # заполнение матрицы переходов
        transition_matrix.append([])
        for j in range(b * 2 - 1):
            if i % 2 == 0 and j % 2 == 0:
                transition_matrix[i].append(True)
            else:
                transition_matrix[i].append(False)
    start = start_point_generate(h, b)
    finish = finish_point_generate(start, h, b)
    list_transition = [start]
    x, y = start
    reach_matrix[x][y] = True
    x, y, tx, ty = transition_choice(x, y, reach_matrix)
    for i in range(1, b * h):
        while not (x >= 0 and y >= 0):
            x, y = list_transition[-1]
            list_transition.pop()
            x, y, tx, ty = transition_choice(x, y, reach_matrix)
        reach_matrix[x][y] = True
        list_transition.append((x, y))
        transition_matrix[tx][ty] = True
        x, y, tx, ty = transition_choice(x, y, reach_matrix)
    return transition_matrix, start, finish  # возвращаем матрицу проходов,начальную и конечную точку

