from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.routes.css import css_router
from app.routes.html import html_router
from app.routes.jscript import jscript_router
from app.routes.sungjuk import sungjuk_router

app = FastAPI()
templates = Jinja2Templates(directory="views/templates")  # jinja2 설정

# 외부 라우트 설정
app.include_router(sungjuk_router, prefix='/sungjuk')
app.include_router(html_router, prefix='/html')
app.include_router(css_router, prefix='/css')
app.include_router(jscript_router, prefix='/js')


# index 라우트
@app.get("/", response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse('index.html', {'request': req})

# hello 라우트
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

