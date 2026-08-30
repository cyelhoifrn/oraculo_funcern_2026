from pathlib import Path

print("=" * 60)
print("🧠 INSTALADOR DO ORÁCULO FUNCERN 2026")
print("=" * 60)

BASE = Path.cwd()

pastas = [
    "backend",
    "backend/app",
    "backend/app/api",
    "backend/app/core",
    "backend/app/database",
    "backend/app/models",
    "backend/app/schemas",
    "backend/app/services",
    "backend/app/prompts",
    "backend/app/uploads",
    "backend/app/migrations",

    "frontend",
    "frontend/assets",
    "frontend/css",
    "frontend/js",
    "frontend/img",

    "knowledge",
    "knowledge/provas",
    "knowledge/documentos",
    "knowledge/editais",
    "knowledge/dna",
    "knowledge/autores",
    "knowledge/estatisticas",

    "uploads",
    "logs",
    "docs",
    "scripts",
    "tests",
    "backups",

    "database"
]

arquivos = [
    "README.md",
    "CHANGELOG.md",
    "ROADMAP.md",
    ".gitignore",

    "backend/app/main.py",
    "backend/requirements.txt",
    "backend/.env.example",

    "frontend/index.html",

    "knowledge/README.md",
    "docs/README.md"
]

for pasta in pastas:
    caminho = BASE / pasta
    caminho.mkdir(parents=True, exist_ok=True)
    print(f"📁 {pasta}")

for arquivo in arquivos:
    caminho = BASE / arquivo

    if not caminho.exists():
        caminho.touch()
        print(f"📄 {arquivo}")

print("\n✅ Estrutura criada com sucesso!")
print("\nProjeto:")
print(BASE)