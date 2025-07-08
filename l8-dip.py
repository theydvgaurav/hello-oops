# DIP(Dependency Inversion Principle) -  High-level modules should not depend on
# low-level modules. Both should depend on abstractions. Abstractions should not depend on
# details. Details should depend on abstractions.


"""

DIP Violating LSP

"""


class LocalStorage:
    def save(self):
        print("saved on local disk")


class CloudStorage:
    def save(self):
        print("saved on cloud")


class ReportService:
    def __init__(self):
        self.cloud_storage = CloudStorage()

    def generate(self):
        self.cloud_storage.save()


"""

DIP Compliant code

"""


class Storage:
    def save(self):
        pass


class LocalStorage(Storage):
    def save(self):
        print("saved on local disk")


class CloudStorage(Storage):
    def save(self):
        print("saved on cloud")


class ReportService:
    def __init__(self, storage: Storage):
        self.storage = storage

    def generate(self):
        self.storage.save()


ReportService(storage=CloudStorage())
ReportService(storage=LocalStorage())

"""
 if more than 1 storage type is needed 
"""


class Storage:
    def save(self):
        pass


class LocalStorage(Storage):
    def save(self):
        print("Saved locally")


class CloudStorage(Storage):
    def save(self):
        print("Saved to cloud")


class CompositeStorage(Storage):
    def __init__(self, storages: list[Storage]):
        self.storages = storages

    def save(self):
        for storage in self.storages:
            storage.save()


class ReportService:
    def generate_report(self, storage: Storage):
        print("Generating report...")
        storage.save()
