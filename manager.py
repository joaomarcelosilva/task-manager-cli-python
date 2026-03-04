from storage import load_tasks, save_tasks
from models import Task


class TaskManager:

    def __init__(self):
        raw_tasks = load_tasks()
        self.tasks = [Task.from_dict(task) for task in raw_tasks]
        self._sort_tasks()

    def _save(self):
        save_tasks([task.to_dict() for task in self.tasks])

    def _sort_tasks(self):
        self.tasks.sort(key=lambda task: task.prioridade)

    def add_task(self, descricao, prioridade):

        if descricao.strip() == "":
            return False, "Tarefa inválida."

        if prioridade not in [1, 2, 3]:
            return False, "Prioridade inválida."

        nova_tarefa = Task(descricao, prioridade)
        self.tasks.append(nova_tarefa)

        self._sort_tasks()
        self._save()

        return True, "Tarefa adicionada com sucesso!"

    def list_tasks(self):
        return self.tasks

    def remove_task(self, index):

        if not self.tasks:
            return False, "Nenhuma tarefa para remover."

        if index < 0 or index >= len(self.tasks):
            return False, "Índice inválido."

        tarefa_removida = self.tasks.pop(index)

        self._save()

        return True, f"Tarefa '{tarefa_removida.descricao}' removida com sucesso!"

    def complete_task(self, index):

        if not self.tasks:
            return False, "Nenhuma tarefa cadastrada."

        if index < 0 or index >= len(self.tasks):
            return False, "Índice inválido."

        if self.tasks[index].concluida:
            return False, "Tarefa já está concluída."

        self.tasks[index].concluida = True

        self._save()

        return True, f"Tarefa '{self.tasks[index].descricao}' marcada como concluída!"

    def edit_task(self, index, nova_descricao, nova_prioridade):

        if index < 0 or index >= len(self.tasks):
            return False, "Índice inválido."

        if nova_descricao.strip() == "":
            return False, "Descrição inválida."

        if nova_prioridade not in [1, 2, 3]:
            return False, "Prioridade inválida."

        self.tasks[index].descricao = nova_descricao
        self.tasks[index].prioridade = nova_prioridade

        self._sort_tasks()
        self._save()

        return True, "Tarefa atualizada com sucesso!"

    def get_stats(self):

        total = len(self.tasks)

        concluidas = sum(1 for task in self.tasks if task.concluida)

        pendentes = total - concluidas

        alta = sum(1 for task in self.tasks if task.prioridade == 1)
        media = sum(1 for task in self.tasks if task.prioridade == 2)
        baixa = sum(1 for task in self.tasks if task.prioridade == 3)

        return {
            "total": total,
            "concluidas": concluidas,
            "pendentes": pendentes,
            "alta": alta,
            "media": media,
            "baixa": baixa
        }