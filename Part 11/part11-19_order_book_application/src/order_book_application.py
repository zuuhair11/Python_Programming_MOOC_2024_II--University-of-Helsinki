# Write your solution here
# If you use the classes made in the previous exercise, copy them here
class Task:
    id = 0

    @classmethod
    def new_id(cls) -> int:
        cls.id += 1
        return cls.id

    def __init__(self, description: str, programmer: str, workload: int) -> None:
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.id = Task.new_id()
        self.finished = False

    def is_finished(self) -> bool:
        return self.finished

    def mark_finished(self) -> None:
        self.finished = True

    def __str__(self) -> str:
        status = 'FINISHED' if self.finished else 'NOT FINISHED'
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}'


class OrderBook:
    def __init__(self):
        self.__tasks = []

    def add_order(self, description: str, programmer: str, workload: int) -> None:
        self.__tasks.append(Task(description, programmer, workload))

    def all_orders(self) -> list:
        return self.__tasks

    def programmers(self) -> tuple:
        return list(set([task.programmer for task in self.__tasks]))

    def finished_orders(self) -> list:
        return [task for task in self.__tasks if task.is_finished()]

    def unfinished_orders(self) -> list:
        return [task for task in self.__tasks if not task.is_finished()]

    def mark_finished(self, id: int) -> None:
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return True

        raise ValueError('Wrong id!')

    def status_of_programmer(self, programmer: str) -> str:
        if programmer in self.programmers():    
            finished_tasks = [task for task in self.__tasks if task.programmer == programmer and task.is_finished()]
            not_finished_tasks = [task for task in self.__tasks if task.programmer == programmer and not task.is_finished()]

            finished_hours = sum([task.workload for task in finished_tasks])
            not_finished_hours = sum([task.workload for task in not_finished_tasks])

            tasks = f'tasks: finished {len(finished_tasks)} not finished {len(not_finished_tasks)}'
            hours = f'hours: done {finished_hours} scheduled {not_finished_hours}'

            return '{}, {}'.format(tasks, hours)
        
        raise ValueError('Never landed!')


class UserInterface:
    def __init__(self) -> None:
        self.__orderbook = OrderBook()

    def help(self) -> None:
        print('commands: ')
        print('0 exit')
        print('1 add order')
        print('2 list finished tasks')
        print('3 list unfinished tasks')
        print('4 mark task as finished')
        print('5 programmers')
        print('6 status of programmer')

    def add_order(self) -> None:
        description = input('description: ')
        programmer_and_workload = input('programmer and workload estimate: ')

        programmer, workload = programmer_and_workload.split()
        self.__orderbook.add_order(description, programmer, int(workload))

        print('added!')

    def finished_tasks(self) -> None:
        if self.__orderbook.finished_orders():
            for programmer in self.__orderbook.finished_orders():
                print(programmer)
        else:
            print('no finished tasks')
    
    def unfinished_tasks(self) -> None:
        for programmer in self.__orderbook.unfinished_orders():
            print(programmer)

    def mark_finished(self) -> None:
        id = int(input('id: '))

        if self.__orderbook.mark_finished(id):
            print('marked as finished')

    def programmers(self) -> None:
        for programmer in self.__orderbook.programmers():
            print(programmer)

    def status_of_programmer(self) -> None:
        programmer = input('programmer: ')

        output = self.__orderbook.status_of_programmer(programmer)
        print(output)

    def execute(self) -> None:
        self.help()

        while True:
            print()
            command = input('command: ')

            try:
                if command == '0':
                    break
                elif command == '1':
                    self.add_order()
                elif command == '2':
                    self.finished_tasks()
                elif command == '3':
                    self.unfinished_tasks()
                elif command == '4':
                    self.mark_finished()
                elif command == '5':
                    self.programmers()
                elif command == '6':
                    self.status_of_programmer()
            except:
                print('erroneous input')


ui = UserInterface()
ui.execute()
