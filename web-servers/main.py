import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
    <h1>Hola Mundo!</h1>
    <video  width="640" height="360" controls>
        <source src="https://i.imgur.com/B6QKKcv.mp4" type="video/mp4">
    </video>
    """
    #{'name': 'Carlos'}

def run():
    store.get_categories()

if __name__ == '__main__':
    run()