import random


def rand_message(messages: dict[int, str], weights: list[int] | None = None) -> tuple[str, int]:
    if not weights:
        return random.choice(messages)
    ran_number: list[int] = random.choices(
        range(1, len(messages) + 1), weights=weights, k=1
    )
    index: int = ran_number[0]
    text: str = messages[index]
    return text, index
