# Exercício 4.1 — API REST de uma aplicação de TODO list (POST/GET/PUT)

**Aluno:** Anderson  
**Disciplina:** IDP-TD 2026  
**Framework:** FastAPI + Uvicorn  

## O que esta API faz

API REST que serve de backend de uma aplicação de TODO list — gerencia tarefas (`{id, titulo, concluida}`), com armazenamento em memória, rodando em `http://localhost:8000`. Implementa POST (criar), GET (ler) e PUT (atualizar).

## Estrutura

```
app/main.py              — implementação da API
requirements.txt         — dependências (fastapi, uvicorn)
.autograde-exercise      — marcador do autograder
README.md                — este arquivo
```

## Como rodar

```bash
pip install -r requirements.txt
uvicorn app.main:app --port 8000
```

## Endpoints

| Método | Rota            | Descrição                             |
|--------|-----------------|---------------------------------------|
| GET    | `/health`       | liveness — `{"status":"ok"}`          |
| POST   | `/tarefas`      | cria tarefa a partir de `{"titulo": "..."}` |
| GET    | `/tarefas/{id}` | lê uma tarefa (404 se não existe)     |
| GET    | `/tarefas`      | lista todas                           |
| PUT    | `/tarefas/{id}` | atualiza titulo e concluida           |

## Decisões de implementação

- **Framework:** FastAPI pela simplicidade, tipagem automática com Pydantic e documentação interativa (/docs).
- **Store:** dicionário `dict[int, dict]` em memória com chave auto-incrementada (`next_id`).
- **404:** `HTTPException(status_code=404)` do próprio FastAPI, que retorna `{"detail": "tarefa não encontrada"}`.
- **Atualização parcial:** os campos `titulo` e `concluida` em PUT são opcionais — só altera o que for enviado.
