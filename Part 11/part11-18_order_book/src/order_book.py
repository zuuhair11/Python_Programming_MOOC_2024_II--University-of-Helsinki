# Write your solution here:
class Task:
    id = 0

    @classmethod
    def new_id(cls) -> int:
        Task.id += 1
        return Task.id

    def __init__(self, description: str, programmer: str, workload: int) -> None:
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False
        self.id = Task.new_id()

    def is_finished(self) -> bool:
        return self.finished

    def mark_finished(self) -> None:
        self.finished = True

    def __str__(self) -> str:
        status = 'FINISHED' if self.finished else 'NOT FINISHED'
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}'


class OrderBook:
    def __init__(self) -> None:
        self.__tasks = []

    def add_order(self, description: str, programmer: str, workload: int) -> None:
        self.__tasks.append(Task(description, programmer, workload))

    def all_orders(self) -> list:
        return self.__tasks
    
    def programmers(self) -> list:
        return list(set(task.programmer for task in self.__tasks))

    def finished_orders(self) -> list:
        return [task for task in self.__tasks if task.is_finished()]
    
    def unfinished_orders(self) -> None:
        return [task for task in self.__tasks if not task.is_finished()]

    def mark_finished(self, id: int) -> None:
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError('Wrong id!')

    def status_of_programmer(self, programmer: str) -> tuple:
        if programmer not in self.programmers():
            raise ValueError('Programmer does not exists!')
        
        finished_tasks = [task for task in self.finished_orders() if task.programmer == programmer]
        not_finished_tasks = [task for task in self.unfinished_orders() if task.programmer == programmer]

        finished_hours = sum([task.workload for task in finished_tasks])
        not_finished_hours = sum([task.workload for task in not_finished_tasks])

        return (len(finished_tasks), len(not_finished_tasks), finished_hours, not_finished_hours)


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

    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)

    # orders.mark_finished(1)
    # orders.mark_finished(2)

    # for order in orders.all_orders():
    #     print(order)

    # print()

    # for programmer in orders.programmers():
    #     print(programmer)

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
