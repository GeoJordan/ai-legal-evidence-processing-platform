class EvidenceStatistics:

    def __init__(self, values=None):
        self.values = values or {}

    def get(self, key):
        return self.values.get(key, 0)

    def items(self):
        return self.values.items()