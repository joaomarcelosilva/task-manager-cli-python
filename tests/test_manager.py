import unittest
import os
import json

from manager import TaskManager


class TestTaskManager(unittest.TestCase):

    TEST_FILE = "tasks.json"

    def setUp(self):
        # limpa o arquivo antes de cada teste
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

        self.manager = TaskManager()

    def tearDown(self):
        # remove o arquivo após cada teste
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_add_task(self):

        sucesso, mensagem = self.manager.add_task("Estudar Python", 1)

        self.assertTrue(sucesso)
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].descricao, "Estudar Python")

    def test_remove_task(self):

        self.manager.add_task("Tarefa teste", 2)

        sucesso, mensagem = self.manager.remove_task(0)

        self.assertTrue(sucesso)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_complete_task(self):

        self.manager.add_task("Finalizar projeto", 1)

        sucesso, mensagem = self.manager.complete_task(0)

        self.assertTrue(sucesso)
        self.assertTrue(self.manager.tasks[0].concluida)

    def test_edit_task(self):

        self.manager.add_task("Tarefa antiga", 3)

        sucesso, mensagem = self.manager.edit_task(
            0,
            "Tarefa atualizada",
            1
        )

        self.assertTrue(sucesso)
        self.assertEqual(self.manager.tasks[0].descricao, "Tarefa atualizada")
        self.assertEqual(self.manager.tasks[0].prioridade, 1)

    def test_sort_by_priority(self):

        self.manager.add_task("Baixa prioridade", 3)
        self.manager.add_task("Alta prioridade", 1)
        self.manager.add_task("Media prioridade", 2)

        tarefas = self.manager.list_tasks()

        self.assertEqual(tarefas[0].prioridade, 1)
        self.assertEqual(tarefas[1].prioridade, 2)
        self.assertEqual(tarefas[2].prioridade, 3)

    def test_stats(self):

        self.manager.add_task("Tarefa 1", 1)
        self.manager.add_task("Tarefa 2", 2)
        self.manager.add_task("Tarefa 3", 2)

        self.manager.complete_task(0)

        stats = self.manager.get_stats()

        self.assertEqual(stats["total"], 3)
        self.assertEqual(stats["concluidas"], 1)
        self.assertEqual(stats["pendentes"], 2)

        self.assertEqual(stats["alta"], 1)
        self.assertEqual(stats["media"], 2)
        self.assertEqual(stats["baixa"], 0)


if __name__ == "__main__":
    unittest.main()