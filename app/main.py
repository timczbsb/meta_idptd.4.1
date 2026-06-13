from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

store: dict[int, dict] = {}
next_id = 1


class TarefaInput(BaseModel):
    titulo: str


class TarefaUpdate(BaseModel):
    titulo: str | None = None
    concluida: bool | None = None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tarefas")
def criar(tarefa: TarefaInput):
    global next_id
    item = {"id": next_id, "titulo": tarefa.titulo, "concluida": False}
    store[next_id] = item
    next_id += 1
    return item


@app.get("/tarefas/{id}")
def ler(id: int):
    if id not in store:
        raise HTTPException(status_code=404, detail="tarefa não encontrada")
    return store[id]


@app.get("/tarefas")
def listar():
    return list(store.values())


@app.put("/tarefas/{id}")
def atualizar(id: int, updates: TarefaUpdate):
    if id not in store:
        raise HTTPException(status_code=404, detail="tarefa não encontrada")
    item = store[id]
    if updates.titulo is not None:
        item["titulo"] = updates.titulo
    if updates.concluida is not None:
        item["concluida"] = updates.concluida
    return item
