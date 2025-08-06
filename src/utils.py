def read_points_from_file(path):
    point_list = []
    read = open(path, 'r')
    for line in read:
        point_list.append(list(map(float, line.split())))
    return point_list