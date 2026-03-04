from task_manager.manager import TaskManager


def show_menu():
    print("\n====================================")
    print("        GERENCIADOR DE TAREFAS")
    print("====================================")

    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Marcar tarefa como concluída")
    print("5 - Editar tarefa")
    print("6 - Estatísticas")
    print("0 - Sair")


def show_tasks(tasks):

    if not tasks:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\n====================================")
    print("           LISTA DE TAREFAS")
    print("====================================")

    prioridade_map = {
        1: "Alta",
        2: "Média",
        3: "Baixa"
    }

    for i, tarefa in enumerate(tasks):

        status = "✓" if tarefa.concluida else " "
        prioridade = prioridade_map.get(tarefa.prioridade)

        print(f"{i+1} - [{status}] ({prioridade}) {tarefa.descricao}")


def show_stats(stats):

    print("\n====================================")
    print("            ESTATÍSTICAS")
    print("====================================")

    print(f"\nTotal de tarefas: {stats['total']}")
    print(f"Concluídas: {stats['concluidas']}")
    print(f"Pendentes: {stats['pendentes']}")

    print("\nPor prioridade:")

    print(f"Alta: {stats['alta']}")
    print(f"Média: {stats['media']}")
    print(f"Baixa: {stats['baixa']}")


def safe_input(message):
    try:
        return input(message)
    except KeyboardInterrupt:
        print("\nOperação cancelada.")
        return None


def main():

    manager = TaskManager()

    while True:

        show_menu()

        option = safe_input("\nEscolha uma opção: ")

        if option is None:
            continue

        if option == "1":

            descricao = safe_input("\nDigite a descrição da tarefa: ")

            if descricao is None:
                continue

            try:
                prioridade = int(safe_input("Digite a prioridade (1 Alta, 2 Média, 3 Baixa): "))
            except (ValueError, TypeError):
                print("\nDigite um número válido.")
                continue

            sucesso, mensagem = manager.add_task(descricao, prioridade)

            print(f"\n{mensagem}")

        elif option == "2":

            tarefas = manager.list_tasks()

            show_tasks(tarefas)

        elif option == "3":

            tarefas = manager.list_tasks()

            show_tasks(tarefas)

            try:
                index = int(safe_input("\nDigite o número da tarefa para remover: ")) - 1
            except (ValueError, TypeError):
                print("\nDigite um número válido.")
                continue

            sucesso, mensagem = manager.remove_task(index)

            print(f"\n{mensagem}")

        elif option == "4":

            tarefas = manager.list_tasks()

            show_tasks(tarefas)

            try:
                index = int(safe_input("\nDigite o número da tarefa para concluir: ")) - 1
            except (ValueError, TypeError):
                print("\nDigite um número válido.")
                continue

            sucesso, mensagem = manager.complete_task(index)

            print(f"\n{mensagem}")

        elif option == "5":

            tarefas = manager.list_tasks()

            show_tasks(tarefas)

            try:
                index = int(safe_input("\nDigite o número da tarefa para editar: ")) - 1
            except (ValueError, TypeError):
                print("\nDigite um número válido.")
                continue

            nova_descricao = safe_input("\nNova descrição: ")

            if nova_descricao is None:
                continue

            try:
                nova_prioridade = int(safe_input("Nova prioridade (1 Alta, 2 Média, 3 Baixa): "))
            except (ValueError, TypeError):
                print("\nDigite um número válido.")
                continue

            sucesso, mensagem = manager.edit_task(index, nova_descricao, nova_prioridade)

            print(f"\n{mensagem}")

        elif option == "6":

            stats = manager.get_stats()

            show_stats(stats)

        elif option == "0":

            print("\nEncerrando o sistema...")
            break

        else:

            print("\nOpção inválida.")


if __name__ == "__main__":
    main()