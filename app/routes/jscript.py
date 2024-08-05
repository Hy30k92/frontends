from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

# 라우터 생성
jscript_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')

# 라우트 설정


@jscript_router.get('/')
async def index(req: Request):
    return templates.TemplateResponse('js/index.html', {'request': req})

@jscript_router.get('/hello')
async def hello(req: Request):
    return templates.TemplateResponse('js/01hello.html', {'request': req})

@jscript_router.get('/type')
async def type(req: Request):
    return templates.TemplateResponse('js/02type.html', {'request': req})