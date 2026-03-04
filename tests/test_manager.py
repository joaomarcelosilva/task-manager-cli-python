import unittest
from task_manager.manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        # cria um manager com lista vazia
        self.manager = TaskManager()
        self.manager.tasks = []

    def test_add_task(self):
        success, _ = self.manager.add_task("Estudar Python", 1)

        self.assertTrue(success)
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].descricao, "Estudar Python")

    def test_remove_task(self):
        self.manager.add_task("Tarefa teste", 1)

        success, _ = self.manager.remove_task(0)

        self.assertTrue(success)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_complete_task(self):
        self.manager.add_task("Tarefa teste", 1)

        success, _ = self.manager.complete_task(0)

        self.assertTrue(success)
        self.assertTrue(self.manager.tasks[0].concluida)

    def test_sort_by_priority(self):
        self.manager.add_task("Baixa", 3)
        self.manager.add_task("Alta", 1)
        self.manager.add_task("Media", 2)

        tarefas = self.manager.list_tasks()

        self.assertEqual(tarefas[0].prioridade, 1)
        self.assertEqual(tarefas[1].prioridade, 2)
        self.assertEqual(tarefas[2].prioridade, 3)

    def test_stats(self):
        self.manager.add_task("T1", 1)
        self.manager.add_task("T2", 2)
        self.manager.add_task("T3", 3)

        self.manager.complete_task(0)

        stats = self.manager.get_stats()

        self.assertEqual(stats["total"], 3)
        self.assertEqual(stats["concluidas"], 1)
        self.assertEqual(stats["pendentes"], 2)


if __name__ == "__main__":
    unittest.main()