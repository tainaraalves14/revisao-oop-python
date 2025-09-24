class Task:
    async def run(self):
        raise NotImplementedError

class PrintTask(Task):
    def __init__(self, message):
        self.message = message

    async def run(self):
        await asyncio.sleep(1)
        print(self.message)

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    async def run_all(self):
        await asyncio.gather(*(task.run() for task in self.tasks))

# Uso
manager = TaskManager()
manager.add_task(PrintTask("Olá"))
manager.add_task(PrintTask("Mundo"))
asyncio.run(manager.run_all())
