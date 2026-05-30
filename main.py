
from fastapi import FastAPI
app = FastAPI(title="Store Intelligence")

@app.get("/metrics")
def metrics():
    return {"footfall":0,"occupancy":0,"avg_dwell_time":0}

@app.get("/funnel")
def funnel():
    return {"detected":0,"engaged":0,"purchase_sessions":0}

@app.get("/events")
def events():
    return []
