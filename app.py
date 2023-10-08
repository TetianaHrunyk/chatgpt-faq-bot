from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.api.endpoints.faq import faq_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(faq_router)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def docs_redirect():
    response = RedirectResponse(url="/docs")
    return response
