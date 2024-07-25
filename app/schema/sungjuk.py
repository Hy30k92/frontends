from pydantic import BaseModel

# 컨테이너 클래스 - 여러개의 값들을 담기 위해 정의
class SungJuk(BaseModel):
    name: str
    kor: int
    eng: int
    mat: int
    tot: int
    avg: float
    grd: str
