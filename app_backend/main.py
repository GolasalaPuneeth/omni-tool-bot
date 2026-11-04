# from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import FastAPI,Request,Depends
from contextlib import asynccontextmanager
from RoutesLayer import assistant_router
# from DatabaseLayer import init_db
import time

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("---------------> Pull up")
    # await init_db()
    yield
    print("---------------> Pull Down")
    
app = FastAPI(title="Omni bot Backend",
              description="A conversational AI application that helps users ask questions, get instant answers, and complete tasks through natural language interactions. Built to provide personalized, context-aware responses, streamline support workflows, and improve user engagement across web and mobile experiences.",
               version="1.0.0",
               lifespan=lifespan)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000
    response.headers["X-Response-Time"] = f"{execution_time:.2f} ms"
    return response

app.include_router(assistant_router,prefix="/api")
# app.include_router(testcases)

# as sample code for refference

# @app.get("/test_point/")
# async def test_endpoint():
#     return ['Hwllo']