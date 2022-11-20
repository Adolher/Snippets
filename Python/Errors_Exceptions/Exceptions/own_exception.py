class OwnException(Exception):
    def __init__(self, value) -> None:
        self.value = value
    def __str__(self) -> str:
        return f"This is my own Exception with value '{self.value}'"

try:
    value = 7
    raise OwnException(value)
except OwnException as e:
    print(e)