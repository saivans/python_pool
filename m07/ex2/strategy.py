from ex1.capability import HealCapability, TransformCapability
from abc import ABC, abstractmethod
from .exception import InvalidCombination


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature) -> str:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return True

    def act(self, creature) -> str:
        if not self.is_valid(creature):
            raise InvalidCombination(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature) -> str:
        if not self.is_valid(creature):
            raise InvalidCombination(
                f"Invalid Creature '{creature.name}'"
                " for this aggressive strategy"
            )
        return "\n".join([
            creature.transform(),
            creature.attack(),
            creature.revert()
        ])


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature) -> str:
        if not self.is_valid(creature):
            raise InvalidCombination(
                f"Invalid Creature '{creature.name}'"
                " for this defensive strategy"
            )

        return "\n".join([
            creature.attack(),
            creature.heal()
        ])
