from pydantic import BaseModel

# 컨테이너 클래스 - 여러개의 값들을 담기 위해 정의
class Employee(BaseModel):
    empid: str
    fname: str
    lname: str
    email: str
    phone: str
    hdate: str
    jobid: str
    sal: int
    comm: float
    mgrid: int
    deptid: int
