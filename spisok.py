class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data
    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data
    def set_next(self, next):
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node == None:
            self.head = new_node
            return
        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def show(self):
        cur_node = self.head
        output = ""
        while cur_node != None:
            output += str(cur_node.get_data()) + "--> "
            cur_node = cur_node.get_next()
        print(output)

    def push_front(self, data):
        new_node = Node(data)
        cur_node = self.head
        new_node.set_next(cur_node)
        self.head = new_node

    def value_at(self, index):
        cur_node = self.head
        count = 0
        while cur_node != None:
            if count == index:
                return cur_node.get_data()
            count +=1
            cur_node = cur_node.get_next()
        print("-")

    def insert(self, index, data):
        new_node = Node(data)
        cur_node = self.head
        count = 0
        while cur_node.get_next() != None:
            if index == 0:
                self.push_front(data)
                return
            elif count + 1 == index:
                the_node_after_cur = cur_node.get_next()
                cur_node.set_next(new_node)
                new_node.set_next(the_node_after_cur)
                return
            count += 1
            cur_node = cur_node.get_next()
        print("-")

    def remove_front(self):
        cur_node = self.head
        self.head = cur_node.get_next()


    def remove(self, index):
        cur_node = self.head
        count = 0
        while cur_node.get_next() != None:
            if index == 0:
                self.remove_front()
                return
            elif count + 1 == index:
                the_node_to_remove = cur_node.get_next()
                the_node_after_removed = the_node_to_remove.get_next()
                cur_node.set_next(the_node_after_removed)
                return
            count += 1
            cur_node = cur_node.get_next()
        print("-")


print('Введите количество элементов - n для заполнения списка')
n = int(input())
print('Введите',n, 'чисел')
linked_list = LinkedList()
for i in range(1, n + 1):
    linked_list.append(int(input()))

print('\n')
user = str(input('Вставить элемент в конец - 1\n Вставить элемент в нужное место 2\n удалить элемент 3\n'))

match user:
    case'1':
        print('Введите элемент')
        ele = int(input())
        linked_list.append(ele)
        print('\n')
        print(linked_list.show())

    case'2':
        print('Введите индекс элемента, на место которого вы хотите вставить число.')
        print('Индекс:')
        ind = int(input())
        print('\n')
        print('Введите число, которое вы хотите вставить')
        ele1 = int(input())
        print(linked_list.insert(ind, ele1))
        print(linked_list.show())

    case'3':
        print('Введите индекс элемента, который вы хотите удалить')
        print('Индекс:')
        ind = int(input())
        print('\n')
        linked_list.remove(ind)
        print(linked_list.show())


