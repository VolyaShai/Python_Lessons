class Road:
    def mass_of_asphalt(self, _length, _width, thickness):
        try:
            _length, _width, thickness = float(_length), float(_width), float(thickness)
            print(f"Масса асфальта составляет {_length * _width * thickness * 25 / 1000} тонн")
        except ValueError:
            print("Введите числа!")


a = Road()
a.mass_of_asphalt(input(f"Введите длину асфальта: "), input("Введите ширину асфальта: "),
                  input("Введите толщину асфальта: "))
