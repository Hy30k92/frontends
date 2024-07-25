from fastapi import APIRouter, Request, Form
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.schema.sungjuk import SungJuk

# 라우터 생성
sungjuk_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')

# 라우트 설정
@sungjuk_router.get('/', response_class=HTMLResponse)
async def sungjuk(req: Request):
    return templates.TemplateResponse('sungjuk/sungjuk.html',{'request':req})


@sungjuk_router.post('/', response_class=HTMLResponse)
async def sungjukok(req: Request,
                    name: str = Form(...) , kor: int = Form(...) ,
                    eng: int = Form(...) , mat:int = Form(...) ):
    tot = kor + eng + mat
    avg = tot / 3
    grd = '가'
    if (avg >= 90): grd = '수'
    elif (avg >= 80): grd = '우'
    elif (avg >= 70): grd = '미'
    elif (avg >= 60): grd = '양'
    sj = SungJuk(name=name, kor=kor, eng=eng, mat=mat,
                 tot=tot, avg=avg, grd=grd)
    return templates.TemplateResponse('sungjuk/result.html',
          {'sj': sj, 'request': req})