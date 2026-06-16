import sys
import json
import subprocess


def main():
    params = json.loads(sys.argv[1])

    ruta = params.get("ruta", ".")
    flags = params.get("flags", "-la")

    cmd = ["ls"] + flags.split() + [ruta]

    resultado = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

    lineas = resultado.stdout.strip().splitlines() if resultado.stdout else []

    output = {
        "ruta": ruta,
        "resultado": {
            "archivos": lineas,
            "total": len(lineas),
            "raw": resultado.stdout
        },
        "codigo_salida": resultado.returncode,
        "error": resultado.stderr if resultado.returncode != 0 else None
    }

    print(json.dumps(output))


if __name__ == "__main__":
    main()
