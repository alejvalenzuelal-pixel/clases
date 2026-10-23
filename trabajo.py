"""MODULO 3: Reporte de pacientes por fecha y por mes."""
from collections import defaultdict

import datos


def mostrar_reporte():
    print("\n--- REPORTE DE PACIENTES ---")
    if not datos.pacientes:
        print("  No hay pacientes registrados.")
        return

    por_fecha = defaultdict(list)
    for p in datos.pacientes:
        por_fecha[p["fecha_ingreso"]].append(p)

    por_mes = defaultdict(int)

    print("\nPacientes por fecha:")
    for fecha in sorted(por_fecha):
        lista = por_fecha[fecha]
        print(f"\n  {fecha.strftime('%d-%m-%Y')}  ->  {len(lista)} paciente(s)")
        for p in lista:
            print(f"      - {p['rut']}  {p['nombre']}")
        por_mes[(fecha.year, fecha.month)] += len(lista)

    print("\nTotal de pacientes ingresados por mes:")
    for (anio, mes) in sorted(por_mes):
        print(f"  {mes:02d}-{anio}: {por_mes[(anio, mes)]}")

    print(f"\nTotal general: {len(datos.pacientes)}")