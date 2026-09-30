from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from database import create_table, add_user, get_users
from gemini_generator import generate_plan


app = FastAPI()

templates = Jinja2Templates(directory="templates")

create_table()


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/generate", response_class=HTMLResponse)
def generate(
    request: Request,
    name: str = Form(...),
    age: int = Form(...),
    goal: str = Form(...)
):

    plan = generate_plan(goal)

    add_user(name, age, goal, plan)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "name": name,
            "plan": plan
        }
    )


@app.get("/users", response_class=HTMLResponse)
def users(request: Request):

    data = get_users()

    return templates.TemplateResponse(
        "all_users.html",
        {
            "request": request,
            "users": data
        }
    )
