from fastapi import FastAPI
from sections.socio.infra.socioInfra import socio_router

class GatisticoAPI(FastAPI):
    def __init__(self, **kwargs):
        super().__init__(
            title="Gatístico API",
            description="API para gestionar socios en la aplicación Gatístico",
            version="1.0",
            **kwargs
        )
        

        self.include_router(socio_router, prefix="/socio", tags=["socio"])


app = GatisticoAPI()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)