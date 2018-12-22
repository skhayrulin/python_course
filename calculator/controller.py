from .token import Token, Parser, CommandToken
from .command import Context, CommandConstructor, Command


class Controller:
    def __init__(
            self,
            parser: Parser,
            constructor: CommandConstructor,
    ) -> None:
        self.__parser = parser
        self.__constructor = constructor

    def run(self) -> None:
        context = self.__create_context()

        context.set_run_state(True)
        while context.is_running():
            raw_line = self.__read_raw_line()

            tokens = self.__parse_tokens(raw_line)

            command = self.__construct_command(tokens)

            self.__execute_command(command, context)

            self.__write_result(context)

    def __create_context(self) -> Context:
        return Context()

    def __read_raw_line(self) -> str:
        return input("> ")

    def __parse_tokens(self, line: str) -> [Token]:
        return self.__parser.process(line)

    def __construct_command(self, tokens: [Token]) -> Command:
        command_token = self.__get_command_token(tokens)
        command_name = command_token.get_value()
        command = self.__constructor.create(command_name)
        return command

    def __get_command_token(self, tokens: [Token]) -> CommandToken:
        return tokens[0]

    def __execute_command(self, command: Command, context: Context) -> bool:
        command.execute(left_operand, right_operand)
        return True

    def __write_result(self, context: Context) -> None:
        print(context)
