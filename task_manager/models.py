class Task:
    def __init__(self, descricao, prioridade=2, concluida=False):
        self.descricao = descricao
        self.prioridade = prioridade
        self.concluida = concluida

    def marcar_como_concluida(self):
        if self.concluida:
            return False, "Tarefa já está concluída."
        
        self.concluida = True
        return True, f"Tarefa '{self.descricao}' marcada como concluída!"
    
    def to_dict(self):
        return {
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "concluida": self.concluida
        }
    
    @staticmethod
    def from_dict(data):
        return Task(
            descricao=data["descricao"],
            prioridade=data.get("prioridade", 2),
            concluida=data.get("concluida", False)
        )
        