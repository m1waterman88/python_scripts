#!/usr/bin/env python3

"""Create a simple game to get better acquainted with Python OOP."""


class GameObject:
    """Create superclass for forthcoming game objects."""

    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name: str) -> None:
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self) -> str:
        return f"{self.class_name}\n{self.desc}"


class Goblin(GameObject):
    """Define goblin subclass."""

    def __init__(self, name: str) -> None:
        self.class_name = "goblin"
        self.health = 3
        self._desc = "A foul creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc

        if self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        else:
            health_line = "It is dead."

        return f"{self._desc}\n{health_line}"

    @desc.setter
    def desc(self, value):
        self._desc = value


def hit(noun: str) -> str:
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]

        if type(thing) == Goblin:
            thing.health -= 1

            if thing.health < 0:
                message = "It's already dead... I can't watch."
            elif thing.health == 0:
                message = f"You killed the {thing.class_name}!"
            else:
                message = f"You hit the {thing.class_name}."
        else:
            message = f"There is no {noun} here."

        return message


goblin = Goblin("Gobbly")


def examine(noun: str) -> str:
    """Return object's description."""
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()

    return f"There is no {noun} here."


def get_input() -> str:
    command = input(": ").split()
    verb_word = command[0]

    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print(f'Unknown verb: "{verb_word}"')
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing..."))


def say(noun: str) -> str:
    if noun == "nothing...":
        return f"You said {noun}"
    else:
        return f'You said "{noun}"'


verb_dict = {
    "examine": examine,
    "hit": hit,
    "say": say
}

while True:
    get_input()
