from fastapi import FastAPI

from tdd_project.core.config import settings


class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            version='0.1.0',
            title=settings.PROJECT_NAME,
            root_path=settings.ROOT_PATH,
        )


app = App()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get(settings.API_V1_STR + '/healthcheck')
def healthcheck():
    return {'status': 'ok'}


@app.get(settings.API_V1_STR + '/info')
def info():
    return {
        'project_name': settings.PROJECT_NAME,
        'database_url': settings.DATABASE_URL,
    }
