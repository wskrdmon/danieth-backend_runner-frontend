# Backend Runner

## Requisitos

- Docker Desktop corriendo
- Archivo `.env` en esta carpeta

## Configuración inicial

Crea el archivo `.env` en `backend_runner/` con estas variables:

```env
DATABASE_URL=postgresql+asyncpg://usuario:password@host:5432/nombre_db
TOOL_REGISTRY_URL=http://tool_registry:8003
```

## Levantar el sistema

```powershell
cd backend_runner
docker compose up --build -d
```

## Registrar herramientas en la BDD

El seeder corre automáticamente al levantar. Si necesitas volver a correrlo manualmente:

```powershell
docker compose run --rm seeder
```

## Servicios disponibles

| Servicio       | URL                              |
|----------------|----------------------------------|
| api_gateway    | http://localhost:8002/docs       |
| tool_registry  | http://localhost:8003/docs       |
| tool_executor  | http://localhost:8004/docs       |

## Herramientas registradas

| Nombre    | Descripcion                                      |
|-----------|--------------------------------------------------|
| nmap      | Escaner de puertos y deteccion de servicios      |
| sqlmap    | Deteccion y explotacion de inyecciones SQL       |
| nuclei    | Escaner de vulnerabilidades basado en templates  |
| xsstrike  | Deteccion de vulnerabilidades XSS                |
| curl      | Realiza peticiones HTTP/HTTPS                    |
| ls        | Lista archivos y directorios                     |
| cat       | Muestra el contenido de un archivo               |

## Ver logs

```powershell
docker logs runner-seeder
docker logs runner-tool-registry
docker logs runner-tool-executor
docker logs runner-api-gateway
```

## Bajar el sistema

```powershell
docker compose down
```

Para bajar y eliminar la BDD (reset completo):

```powershell
docker compose down --volumes
```
