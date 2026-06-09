import httpx
from fastapi import APIRouter, HTTPException, Request

router = APIRouter(prefix="/proxy", tags=["Proxy"])

TOOL_REGISTRY_URL = "http://localhost:8003"
TOOL_EXECUTOR_URL = "http://localhost:8004"
API_GATEWAY_URL = "http://localhost:8000"


@router.get("/herramientas")
async def listar_herramientas():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{TOOL_REGISTRY_URL}/herramientas/")
        if r.status_code != 200:
            raise HTTPException(status_code=r.status_code, detail=r.text)
        return r.json()


@router.post("/ejecutar")
async def ejecutar_herramienta(request: Request):
    body = await request.json()
    sesion_id = body.get("sesion_id")

    try:
        async with httpx.AsyncClient(timeout=60) as client:
            if not sesion_id:
                # Crear objetivo automático
                r_obj = await client.post(
                    f"{API_GATEWAY_URL}/objetivos/",
                    json={
                        "usuario_id": 1,
                        "url_objetivo": "http://target.local"
                    }
                )
                print(f"Objetivo creado: {r_obj.status_code} {r_obj.text}")
                objetivo_id = r_obj.json().get("objetivo_id")

                # Crear sesión automática
                r_ses = await client.post(
                    f"{API_GATEWAY_URL}/sesiones/",
                    json={"objetivo_id": objetivo_id}
                )
                print(f"Sesión creada: {r_ses.status_code} {r_ses.text}")
                sesion_id = r_ses.json().get("sesion_id")

            payload = {
                "herramienta": body.get("herramienta"),
                "params": body.get("params", {}),
                "sesion_id": sesion_id,
                "orden_ejecucion": body.get("orden_ejecucion", 1),
            }
            print(f"Enviando a tool_executor: {payload}")

            r = await client.post(f"{TOOL_EXECUTOR_URL}/ejecutar/", json=payload)
            print(f"tool_executor respondió: {r.status_code} {r.text}")
            if r.status_code != 200:
                raise HTTPException(status_code=r.status_code, detail=r.text)
            return r.json()
    except Exception as e:
        print(f"ERROR EN PROXY EJECUTAR: {e}")
        raise


@router.get("/ejecutar/tareas/{tarea_id}")
async def obtener_tarea(tarea_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{TOOL_EXECUTOR_URL}/ejecutar/tareas/{tarea_id}")
        if r.status_code != 200:
            raise HTTPException(status_code=r.status_code, detail=r.text)
        return r.json()