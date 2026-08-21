class MemoryStore:
    def __init__(self): self.records=[]
    def add(self, record): self.records.append(record)
    def all(self): return list(self.records)
