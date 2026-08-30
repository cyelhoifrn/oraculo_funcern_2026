from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["Status"])


@router.get("/status")
def status():

    return {
        "status": "online",
        "versao": "1.2.0",
        "sistema": "ORÁCULO FUNCERN"
    }