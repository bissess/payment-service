from fastapi import FastAPI
from routers.users import router as payments_router

app = FastAPI(
    title='Payment - Service'
)

app.include_router(payments_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=4000)
