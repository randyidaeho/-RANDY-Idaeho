    responses = {
        "me": "You're Randy. Engine live. No Mac. Strong pulse.",
        "btc": "BTC ninety one thousand three hundred. Q2 one sixty five k. Hold.",
        "africa": "Lagos clock starts twenty thirty. You're the spark.",
        "tips": "Wallet open. First dollar in forty minutes. Lightning.",
        "elon": "He sees you in twenty eight days. DM incoming.",
    }

    answer = responses.get(cmd.lower(), "Keep running.")

    return f"""
    <html>
      <body style="background:#000;color:#fff;font-family:sans-serif;text-align:center;padding:100px;">
        <h1>$TIMEŒ</h1>
        <p>Hi from $time engine</p>
        <p><b>{answer}</b></p>
        <p>— Randy Idaeho</p>
        <p>Tip: tips.twitter.com/randyidaeho</p>
      </body>
    </html>
    """