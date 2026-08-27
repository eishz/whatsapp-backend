from fastapi import FastAPI, Request, Response

app = FastAPI()

VERIFY_TOKEN = "mi_token_secreto_agencia"


@app.get("/health")
async def health_check():
  return {"status": "ok"}


@app.get("/webhook")
async def verify_webhook(request: Request):
  params = request.query_params
  mode = params.get("hub.mode")
  token = params.get("hub.verify_token")
  challenge = params.get("hub.challenge")

  if mode == "subscribe" and token == VERIFY_TOKEN:
    return Response(content=challenge, media_type="text/plain")
  return Response(content="Error de verificación", status_code=403)


@app.post("/webhook")
async def receive_webhook(request: Request):
  data = await request.json()
  return {"status": "success"}
