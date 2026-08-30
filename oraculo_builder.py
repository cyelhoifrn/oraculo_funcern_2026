"""
=========================================================
🧠 ORÁCULO FUNCERN 2026
Builder Oficial
=========================================================
"""

from pathlib import Path
import sqlite3
import subprocess
import webbrowser
import os

VERSAO = "2.0.0"

BASE = Path(__file__).parent
BACKEND = BASE / "backend"

ITENS = [
    "backend",
    "frontend",
    "knowledge",
    "database",
    "docs",
    "logs",
    "scripts",
    "tests",
    "uploads",
    "backups",
    "README.md"
]


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione ENTER...")


# ------------------------------------
# Verificar Projeto
# ------------------------------------

def verificar_projeto():

    print()

    ok = 0

    for item in ITENS:

        caminho = BASE / item

        if caminho.exists():
            print(f"✅ {item}")
            ok += 1
        else:
            print(f"❌ {item}")

    print()

    print(f"Estrutura: {ok}/{len(ITENS)}")

    pausar()


# ------------------------------------
# Banco
# ------------------------------------

def criar_banco():

    pasta = BASE / "database"

    pasta.mkdir(exist_ok=True)

    banco = pasta / "oraculo.db"

    conexao = sqlite3.connect(banco)

    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questoes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        disciplina TEXT,
        assunto TEXT,
        enunciado TEXT,
        resposta TEXT
    )
    """)

    conexao.commit()

    conexao.close()

    print()

    print("🟢 Banco pronto.")

    pausar()


# ------------------------------------
# Servidor
# ------------------------------------

def executar_servidor():

    print()

    print("Iniciando servidor...")

    subprocess.run(
        [
            "python",
            "-m",
            "uvicorn",
            "app.main:app",
            "--reload"
        ],
        cwd=BACKEND
    )


# ------------------------------------
# Navegador
# ------------------------------------

def abrir_navegador():

    webbrowser.open("http://127.0.0.1:8000")

    print()

    print("Navegador aberto.")

    pausar()


# ------------------------------------
# Menu
# ------------------------------------

def menu():

    while True:

        limpar()

        print("=" * 55)
        print("🧠 ORÁCULO BUILDER")
        print("=" * 55)
        print(f"Versão {VERSAO}")
        print()
        print("1 - Verificar Projeto")
        print("2 - Criar Banco")
        print("3 - Executar Servidor")
        print("4 - Abrir Navegador")
        print()
        print("0 - Sair")
        print("=" * 55)

        op = input("Escolha: ")

        if op == "1":
            verificar_projeto()

        elif op == "2":
            criar_banco()

        elif op == "3":
            executar_servidor()

        elif op == "4":
            abrir_navegador()

        elif op == "0":
            break

        else:
            print("Opção inválida.")
            pausar()


if __name__ == "__main__":
    menu()