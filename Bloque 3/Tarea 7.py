#re
def computepay(horas, tarifa):
    if horas > 40:
        horas_extra = horas - 40
        pago = (40 * tarifa) + (horas_extra * tarifa * 1.5)
    else:
        pago = horas * tarifa
    return pago

horas = float(input("Ingresar horas: "))
tarifa = float(input("Ingresar tarifa: "))

salario = computepay(horas, tarifa)

print("Salario:", salario)
