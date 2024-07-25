from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

# 라우터 생성
sungjuk_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')

# 라우트 설정
@sungjuk_router.get('/', response_class=HTMLResponse)
async def sungjuk(req: Request):
    return templates.TemplateResponse('sungjuk/sungjuk.html',{'request':req})


@sungjuk_router.post('/', response_class=HTMLResponse)
async def sungjukok():
    pass


