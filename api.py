from fastapi import FastAPI
from pydantic import BaseModel
from parser.pluto_parser import PlutoParser

app = FastAPI(title="LibreCube PLUTO API", version="0.1.0")

class PlutoCode(BaseModel):
    code: str

@app.get("/")
def read_root():
    return {
        "status": "Active",
        "project": "ZED PLUTO Plugin Prototype",
        "endpoints": ["/parse", "/format", "/lint"]
    }

@app.post("/parse")
async def parse(payload: PlutoCode):
    return {"status": "parsed", "content": payload.code}

@app.post("/format")
async def format_code(payload: PlutoCode):
    formatted = PlutoParser.format_pluto(payload.code)
    return {"status": "success", "formatted": formatted}

@app.post("/lint")
async def lint_code(payload: PlutoCode):
    results = PlutoParser.lint_pluto(payload.code)
    return {"status": "success", "results": results}