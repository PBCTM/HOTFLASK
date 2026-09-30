import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class num(BaseModel):
    a: float
    b: float

api=FastAPI(title="CTM WEB SERVER")

@api.get('/test')
def test():
    return("Test was successful")

@api.post(path='/sum',status_code=209)
def sum(class_num: num) -> float:
    print(class_num.a)
    print(class_num.b)
    return(int(class_num.a)+int(class_num.b))

if __name__=="__main__":
    uvicorn.run(app="web:api",host="127.0.0.1",port=8080,reload=True)

