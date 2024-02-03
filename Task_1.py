class TaskQueue:
    def __init__(self):
        self.queue = []

    def to_queue(self, item):
        if len(self.queue) >= 20:
            raise Exception("Queue is full!")
        self.queue.append(item)

    def from_queue(self):
        if not self.queue:
            raise Exception("Queue is empty!")
        return self.queue.pop(0)

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def clear(self):
        self.queue = []

    def size(self) -> int:
        return len(self.queue)


