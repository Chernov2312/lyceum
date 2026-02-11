class PositiveIntegerConverter:
    regex = r'[0-9]*[1-9][0-9]*'

    def to_python(self, value):
        try:
            int_value = int(value)
            if int_value <= 0:
                raise ValueError(
                    'Значение должно быть положительным целым числом'
                )
            return int_value
        except ValueError:
            raise ValueError(
                f'{value} не является корректным положительным целым числом'
            )

    def to_url(self, value):
        if value <= 0:
            raise ValueError(f'{value} должно быть положительным целым числом')
        return str(value)
