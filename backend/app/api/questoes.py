from pathlib import Path
import sqlite3

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api", tags=["Questões"])

BASE_DIR = Path(__file__).resolve().parents[3]
BANCO = BASE_DIR / "database" / "oraculo.db"


class QuestaoNova(BaseModel):

    disciplina: str
    assunto: str
    enunciado: str
    resposta: str


@router.get("/questoes")
def listar_questoes():

    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row

    cursor = conexao.cursor()

    cursor.execute("""

        SELECT

            id,
            disciplina,
            assunto,
            enunciado,
            resposta

        FROM questoes

        ORDER BY id DESC

    """)

    dados = [dict(x) for x in cursor.fetchall()]

    conexao.close()

    return dados


@router.post("/questoes")
def inserir_questao(questao: QuestaoNova):

    conexao = sqlite3.connect(BANCO)

    cursor = conexao.cursor()

    cursor.execute("""

        INSERT INTO questoes(

            disciplina,
            assunto,
            enunciado,
            resposta

        )

        VALUES (?,?,?,?)

    """,(

        questao.disciplina,
        questao.assunto,
        questao.enunciado,
        questao.resposta

    ))

    conexao.commit()

    novo_id = cursor.lastrowid

    conexao.close()

    return {

        "sucesso":True,
        "id":novo_id

    }