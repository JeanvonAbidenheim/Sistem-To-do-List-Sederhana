from todo import TodoList

def main():
    todo = TodoList()

    while True:
        print("\n=== TO-DO LIST ===")
        print("1. Lihat tugas")
        print("2. Tambah tugas")
        print("3. Hapus tugas")
        print("4. keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            todo.show_task()

        elif choice == "2":
            task = input("Tugas baru: ")
            todo.add_task(task)

        elif choice == "3":
            index = input("Nomor tugas yang dihapus: ")
            todo.remove_task(index)

        elif choice == "4":
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()