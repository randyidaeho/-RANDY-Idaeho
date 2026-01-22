from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    cmd = request.query_params.get("run", "me")
    return f"""
    <html>
      <body style="background:#000;color:#fff;font-family:sans-serif;text-align:center;padding:50px;">
        <h1>$TIMEŒ</h1>
        <p