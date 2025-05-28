from fastapi import APIRouter, UploadFile, File
from app.parsers.junit import parse_junit_xml

router = APIRouter()

@router.post("/results/upload")
async def upload_results(file: UploadFile = File(...)):
    contents = await file.read()
    path = f"/tmp/{file.filename}"
    with open(path, "wb") as f:
        f.write(contents)

    suites = parse_junit_xml(path)
    # store in DB (mock or real)
    return {"parsed_suites": [suite.dict() for suite in suites]}
