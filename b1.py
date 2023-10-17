# Höfundur: Milos Petrovic
# Dagsetning: 17.10.2023
# Verkefni: Forritun 1B - Spurning 1

def farenheitToCelsius(f) -> float:
  return (5/9)*(f-32)

def main():
  tf = float(input("Hitastig á farengeit skala: "))
  print("Það eru : {:4.2f} gráður á Celsius".format(farenheitToCelsius(tf)))

main()
