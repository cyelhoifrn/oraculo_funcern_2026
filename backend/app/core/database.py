from pathlib import Path
import sqlite3

# Caminho até a raiz do projeto
ROOT = Path(__file__).resolve().parents[3]

# Banco criado pelo Builder
DATABASE_PATH = ROOT / "database" / "oraculo.db"


def get_connection():
    """
    Retorna uma conexão com o banco SQLite.
    """
    return sqlite3.connect(DATABASE_PATH)


def verificar_conexao():
    """
    Testa se o banco pode ser aberto.
    """
    try:
        conn = get_connection()
        conn.execute("SELECT 1")
        conn.close()
        return True
    except Exception:
        return False