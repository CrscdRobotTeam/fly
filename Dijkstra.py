class Graph_matrix(object):
    def __init__(self):
        self.storage_matrix = []
        self.node_list = []

    def make_picture(self, matrix, _nodes):
        '''
        :param matrix: 输入邻接矩阵
        :return:
        '''
        self.node_list = _nodes
        for m in matrix:
            self.storage_matrix.append(m)

    def dict_min_by_value(self, this_dict):
        '''
        字典里值最小的键
        '''
        min = 10 ** 10
        key = ''
        for get_item in this_dict.items():
            if get_item[-1] < min:
                min = get_item[-1]
                key = get_item[0]
        return key

    def get_node_index(self, node):
        '''
        找min_key在列表节点中的下标
        '''
        for i in range(len(self.node_list)):
            if node == self.node_list[i]:
                return i

    def dijkstra(self, start_node):
        over_node = {start_node: 0}  # 已经查找完最短路径的节点以及距离
        found_node = dict()  # 待查找最短路径的节点以及与开始节点的距离
        i = self.get_node_index(start_node)
        for j in range(len(self.storage_matrix[i])):
            if j != i:
                found_node[self.node_list[j]] = self.storage_matrix[i][j]
        while found_node:
            min_key = self.dict_min_by_value(found_node)
            over_node[min_key] = found_node[min_key]
            found_node.pop(min_key)
            i = self.get_node_index(min_key)
            for get_node in found_node.items():
                j = self.get_node_index(get_node[0])
                if get_node[-1] > over_node[min_key] + self.storage_matrix[i][j]:
                    found_node[get_node[0]] = over_node[min_key] + self.storage_matrix[i][j]
        print(over_node)


m = 10 ** 10  # 代替表示无穷大
nodes = ['a', 'b', 'c', 'd', 'e', 'f']
distance = [[0, 7, 9, m, 14, m],  # a
            [7, 0, 10, 15, m, m],  # b
            [9, 10, 0, 11, 2, m],  # c
            [m, 15, 11, 0, m, 6],  # d
            [14, m, 2, m, 0, 9],  # e
            [m, m, m, 6, 9, 0]]  # f
test = Graph_matrix()
test.make_picture(distance, nodes)
test.dijkstra('a')
