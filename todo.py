class TodoList:
    def __init__(self):
        self.task = []

    def show_task(self):
        if not self.tasks:
            print("Belum ada tugas.")
            return
        
        print("\nDaftar tugas: ")
        for i, task in enumerate(self.task, start=1):
            print(f"{i}. {task}")

    def add_task(self, task):
        self.task.append(task)
        print("Tugas ditambahkan.")

    def remove_task(self, index):
        try:
            index = int(index)
            if 1 <= index <= len(self.task):
                removed = self.task.pop(index - 1)
                print(f"Tugas '{removed}' dihapus.")
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")