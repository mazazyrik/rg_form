import logging
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from schemas import FormSchema
from db import Form


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')


templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post('/api/form')
async def form(request: Request):
    data = await request.json()
    try:
        form = Form(name=data['name'], phone=data['phone'], age=data['age'],
                    category=data['category'], job=data['job'],
                    motivation=data['motivation'], sex=data['sex'])
        form.save()
    except Exception as e:
        logging.error(e)


@app.get('/api/forms')
async def get_form() -> list[FormSchema]:
    try:
        return Form.select()
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
