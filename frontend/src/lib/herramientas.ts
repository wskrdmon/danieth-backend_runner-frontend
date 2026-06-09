import { apiClient } from './api';

export async function listarHerramientas() {
  const { data } = await apiClient.get('/proxy/herramientas');
  return data;
}

export async function ejecutarHerramienta(payload: {
  herramienta: string;
  params?: Record<string, unknown>;
  sesion_id?: number;
  orden_ejecucion?: number;
}) {
  const { data } = await apiClient.post('/proxy/ejecutar', payload);
  return data;
}

export async function obtenerTarea(tareaId: number) {
  const { data } = await apiClient.get(`/proxy/ejecutar/tareas/${tareaId}`);
  return data;
}