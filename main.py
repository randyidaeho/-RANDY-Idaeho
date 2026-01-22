from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
      <body style="background:#000;color:#fff;font-family:sans-serif;text-align:center;padding:50px;">
        <h1>$TIMEŒ</h1>
        <p>Hi from $time engine</p>
        <p>— Randy Idaeho</p>
        <p>Running on Render. Forever.</p>
        <p>Tip: tips.twitter.com/randyidaeho</p>
      </body>
    </html>
    """