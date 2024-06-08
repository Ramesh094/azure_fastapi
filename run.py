from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum


app = FastAPI()

# predefining values of path parameters for post operatrion
class StatusEnum(Enum):
    active = 'active'
    inactive = 'inactive'
    pending = 'pending'


class Item(BaseModel):
    name : str
    count : int
    price: float
    status: StatusEnum

@app.post('/add/')
async def add_item(item:Item):
    return {'message': f'{item.name} count of {item.count} at price of {item.price}'}


# fastapi made for asynchronous calls


@app.get('/')
async def greet():
    return f'Welcome you all'

# predefined path parameters for get operation
class Toss(Enum):
    one = 'Head'
    two = "Tail"


@app.get('/hello/{name}')
async def greet(name :Toss):
    return f'Hello {name}'





# predefined path and query parameters for get operation:
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

class Path(str, Enum):
    top1 = 'sriram'
    top2 = 'nani'
    top3 = 'ramesh'

class MyModel(BaseModel):
    name : Path

@app.post('/info/{topper}')
async def new(topper: Path, q:MyModel=None):
    return {'topper': topper, "top": q.name if q else None}

# this is to check the history of pr
# this is to check the history of pr2