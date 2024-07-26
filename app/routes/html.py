from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

# 라우터 생성
html_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')

# 라우트 설정
@html_router.get('/')
async def index(req: Request):
    return templates.TemplateResponse('html/index.html', {'request': req})

@html_router.get('/layout')
async def layout(req: Request):
    return templates.TemplateResponse('html/01layout.html', {'request': req})

@html_router.get('/text')
async def text(req: Request):
    return templates.TemplateResponse('html/02text.html', {'request': req})

@html_router.get('/link')
async def link(req: Request):
    return templates.TemplateResponse('html/03link.html', {'request': req})

@html_router.get('/list')
async def list(req: Request):
    return templates.TemplateResponse('html/04list.html', {'request': req})

@html_router.get('/table')
async def table(req: Request):
    return templates.TemplateResponse('html/05table.html', {'request': req})



