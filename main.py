from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

class Job(BaseModel):
    source: str
    target: str
    min_delay: int
    max_delay: int
    max_per_account: int
    anti_spam: bool

@app.post("/start_job")
def start_job(job: Job):
    subprocess.Popen(["python3", "worker.py"])
    return {"status": "job started"}

@app.get("/status")
def status():
    return {"running": True}
