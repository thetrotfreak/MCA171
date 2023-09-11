def printf(
    *value: object, sep: str | None = " ", end: str | None = "\n", width: int = 78
):
    print("-" * width)
    print(value)
    print("-" * width)
