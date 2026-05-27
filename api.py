from fastapi import FastAPI
from pydantic import BaseModel
from AI_Research_agent import workflow
from fastapi.responses import JSONResponse

class Research_agent(BaseModel):
    topic:str

app=FastAPI()
@app.post("/research")
def research_query(request:Research_agent):
    topic=request.topic
    response=workflow.invoke({"topic":topic})
    return {"report": response["final"]}

@app.get("/")
def home():
    return JSONResponse(status_code=200,content="This is the research API home page ")