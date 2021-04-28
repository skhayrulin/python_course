from typing import Type


class Operand:
    pass


class Context:
    def __init__(self):
        self.__is_running = False

    def set_run_state(self, state: bool) -> None:
        self.__is_running = state

    def is_running(self) -> bool:
        return self.__is_running

    def get_operands(self) -> [Operand]:
        pass

    def get_left_operand(self) -> Operand:
        pass

    def get_right_operand(self) -> Operand:
        pass

    def get_variables(self):
        pass

    def set_variable(self, var) -> None:
        pass

    def set_left_operand(self, op: Operand):
        pass

    def set_right_operand(self, op: Operand):
        pass


class Command:
    def execute(self, context: Context) -> None:
        pass


class CommandConstructor:
    def __init__(self):
        self.__command_dict = {}

    def register(self, name: str, command_class: Type[Command]) -> None:
        self.__command_dict[name] = command_class

    def create(self, name: str) -> Command:
        command_class = self.__command_dict[name]
        return command_class()


class PlusCommand(Command):
    def execute(self, context: Context):
        pass
