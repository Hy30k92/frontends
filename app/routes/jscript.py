import sqlite3

from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
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


@jscript_router.get('/operator')
async def operator(req: Request):
    return templates.TemplateResponse('js/03operator.html', {'request': req})

@jscript_router.get('/condition')
async def condition(req: Request):
    return templates.TemplateResponse('js/04condition.html', {'request': req})

@jscript_router.get('/loof')
async def loof(req: Request):
    return templates.TemplateResponse('js/05loof.html', {'request': req})

@jscript_router.get('/array')
async def array(req: Request):
    return templates.TemplateResponse('js/06array.html', {'request': req})

@jscript_router.get('/while')
async def whiles(req: Request):
    return templates.TemplateResponse('js/07while.html', {'request': req})

@jscript_router.get('/function')
async def function(req: Request):
    return templates.TemplateResponse('js/08function.html', {'request': req})

@jscript_router.get('/callback')
async def callback(req: Request):
    return templates.TemplateResponse('js/09callback.html', {'request': req})

@jscript_router.get('/except')
async def excepts(req: Request):
    return templates.TemplateResponse('js/10except.html', {'request': req})

@jscript_router.get('/bom')
async def bom(req: Request):
    return templates.TemplateResponse('js/11bom.html', {'request': req})

@jscript_router.get('/dom')
async def dom(req: Request):
    return templates.TemplateResponse('js/12dom.html', {'request': req})

@jscript_router.get('/event')
async def event(req: Request):
    return templates.TemplateResponse('js/13event.html', {'request': req})

@jscript_router.get('/form')
async def form(req: Request):
    return templates.TemplateResponse('js/14form.html', {'request': req})

@jscript_router.get('/ajax')
async def ajax(req: Request):
    return templates.TemplateResponse('js/15ajax.html', {'request': req})

@jscript_router.get('/zipcode')
async def zipcode(req: Request):
    return templates.TemplateResponse('js/16zipcode.html', {'request': req})

@jscript_router.get('/ajaxzip')
async def ajaxzip(req: Request):
    return templates.TemplateResponse('js/17ajaxzip.html', {'request': req})

@jscript_router.get('/zip2013')
async def zip2013(req: Request):
    return templates.TemplateResponse('js/17ajaxzip.html', {'request': req})

# api
# http://127.0.0.1:8000/js/getsido
@jscript_router.get('/getsido')
async def getsido():
    # zipcode 테이블에서 시도 조회
    conn = sqlite3.connect('app/schema/python.db')
    cursor = conn.cursor()
    sql = 'select distinct sido from zipcode2013'
    cursor.execute(sql)
    sidos = cursor.fetchall()
    cursor.close()
    conn.close()
    # 조회된 결과를 json 으로 저장
    result = []
    for sido in sidos:
        result.append({'sido': sido[0]})

    return JSONResponse(content=result)

#http://127.0.0.1:8000/js/getgugun?sido=서울
@jscript_router.get('/getgugun')
async def getgugun(sido: str):
    # zipcode 테이블에서 구군 조회
    conn = sqlite3.connect('app/schema/python.db')
    cursor = conn.cursor()
    sql ='select distinct gugun from zipcode2013 where sido = ?'
    cursor.execute(sql, (sido,))
    guguns = cursor.fetchall()
    cursor.close()
    conn.close()
    # 조회된 결과를 json 으로 저장
    result = []
    for gugun in guguns:
        result.append({'gugun': gugun[0]})

    return JSONResponse(content=result)

#http://127.0.0.1:8000/js/getdong?sido=서을&gugun=강남구
@jscript_router.get('/getdong')
async def getdong(sido: str, gugun: str):
    # zipcode 테이블에서 읍면동 조회
    conn = sqlite3.connect('app/schema/python.db')
    cursor = conn.cursor()
    sql ='select distinct dong from zipcode2013 where sido = ? and gugun = ? '
    cursor.execute(sql, (sido, gugun,))
    dongs = cursor.fetchall()
    cursor.close()
    conn.close()
    # 조회된 결과를 json 으로 저장
    result = []
    for dong in dongs:
        result.append({'dong': dong[0]})

    return JSONResponse(content=result)