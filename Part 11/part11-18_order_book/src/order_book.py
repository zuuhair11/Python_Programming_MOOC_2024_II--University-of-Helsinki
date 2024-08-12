# Write your solution here:
class Task:
    id = 1

    def __init__(self, description: str, programmer: str, workload: int) -> None:
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

        self.id = Task.id
        Task.id += 1

    def is_finished(self) -> bool:
        return self.finished

    def mark_finished(self) -> None:
        self.finished = True

    def __str__(self) -> str:
        status = 'FINISHED' if self.finished else 'NOT FINISHED'
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}'


class OrderBook:
    def __init__(self) -> None:
        self.tasks = []

    def add_order(self, description: str, programmer: str, workload: int) -> None:
        self.tasks.append(Task(description, programmer, workload))

    def all_orders(self) -> list:
        return self.tasks
    
    def programmers(self) -> list:
        return list(set(task.programmer for task in self.tasks))
    
    def finished_orders(self) -> list:
        return [task for task in self.tasks if task.is_finished()]
    
    def unfinished_orders(self) -> None:
        return [task for task in self.tasks if not task.is_finished()]

    def mark_finished(self, id: int) -> None:
        ids = [task.id for task in self.tasks]

        if id in ids:
            [task.mark_finished() for task in self.unfinished_orders() if task.id == id]
        else:
            raise ValueError('The given id is not valid!')


if __name__ == '__main__':
    # t1 = Task('program hello world', 'Eric', 3)
    # print(t1.id, t1.description, t1.programmer, t1.workload)
    # print(t1)
    # print(t1.is_finished())
    # t1.mark_finished()
    # print(t1)
    # print(t1.is_finished())
    # t2 = Task('program webstore', 'Adele', 10)
    # t3 = Task('program mobile app for workload accounting', 'Eric', 25)
    # print(t2)
    # print(t3)

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    orders.mark_finished(1)
    orders.mark_finished(2)

    for order in orders.all_orders():
        print(order)

    print()

    for programmer in orders.programmers():
        print(programmer)
