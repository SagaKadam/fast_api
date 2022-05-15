from fastapi import FastAPI
from enum import Enum # for data validations

app = FastAPI()

class AvailableMenu(str, Enum):
    indian = 'indian'
    american = 'american'

    food_items = {
        'indian': ['samosa', 'dosa'],
        'american': ['hot dog', 'burger']
    }

@app.get("/hello")
async def hello():
    return "hello, sagar!"

# parameterized endpoint
@app.get("/hi/{name}")
async def hi(name):
    return f"hi, {name}"

@app.get("/get_items/{menu}")
async def get_items(menu: AvailableMenu):
    menus = AvailableMenu()
    return menus.food_items.get(menu)