import random
from typing import Generator, List, Tuple


def gen_event() -> Generator[Tuple[str, str], None, None]:
    players: List[str] = ['alice', 'bob', 'charlie', 'dylan']
    actions: List[str] = [
        'run', 'eat', 'sleep', 'grab', 'move',
        'climb', 'swim', 'release', 'use'
    ]

    while True:
        name: str = random.choice(players)
        action: str = random.choice(actions)
        yield (name, action)


def consume_event(events: List[Tuple[str, str]]) -> Generator[Tuple[str, str],
                                                              None, None]:
    while events:
        event: Tuple[str, str] = random.choice(events)
        events.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_stream = gen_event()

    for i in range(1000):
        event: Tuple[str, str] = next(event_stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    print()

    event_list: List[Tuple[str, str]] = []
    temp_stream = gen_event()
    for _ in range(10):
        event_list.append(next(temp_stream))

    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
