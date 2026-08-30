from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.status import router as status_router
from app.api.questoes import router as questoes_router

app = FastAPI(
    title="ORÁCULO FUNCERN",
    version="2.0.0"
)

BASE_DIR = Path(__file__).resolve().parents[2]

FRONTEND = BASE_DIR / "frontend"

TEMPLATES = Path(__file__).parent / "templates"

templates = Jinja2Templates(directory=str(TEMPLATES))

app.mount("/css", StaticFiles(directory=FRONTEND / "css"), name="css")
app.mount("/js", StaticFiles(directory=FRONTEND / "js"), name="js")
app.mount("/img", StaticFiles(directory=FRONTEND / "img"), name="img")

app.include_router(status_router)
app.include_router(questoes_router)


@app.get("/", include_in_schema=False)
async def dashboard(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "titulo": "ORÁCULO FUNCERN"
        }
    )


@app.get("/questoes", include_in_schema=False)
async def questoes():

    return FileResponse(FRONTEND / "index.html")