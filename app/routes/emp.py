from fastapi import APIRouter, Request, Form
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.schema.emp import Employee

# 라우터 생성
emp_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')


# 라우트 설정
@emp_router.get('/', response_class=HTMLResponse)
async def emp(req: Request):
    return templates.TemplateResponse('emp/emp.html', {'request': req})


@emp_router.post('/', response_class=HTMLResponse)
async def empok(req: Request,
                empid: str = Form(...), fname: str = Form(...), lname: str = Form(...),
                email: str = Form(...), phone: str = Form(...), hdate: str = Form(...),
                jobid: str = Form(...), sal: str = Form(...), comm: str = Form(...),
                mrgid: str = Form(...), deptid: str = Form(...)):
    emp = Employee(empid=empid, fname=fname, lname=lname, email=email, phone=phone, hdate=hdate,
              jobid=jobid, sal=sal, comm=comm, mrgid=mrgid, deptid=deptid)
    return templates.TemplateResponse('emp/empresult.html',
                                      {'emp': emp, 'request': req})
