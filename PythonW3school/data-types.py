x_values = [
    "Hello World",
    20,
    20.5,
    1j,
    ["apple", "banana", "cherry"],
    ("apple", "banana", "cherry"),
    range(6),
    {"name": "John", "age": 36},
    {"apple", "banana", "cherry"},
    frozenset({"apple", "banana", "cherry"}),
    True,
    b"Hello",
    bytearray(5),
    memoryview(bytes(5)),
    None
]

for value in x_values:
    print(f"x = {value} \t {type(value)}")
