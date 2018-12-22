from .token import Parser
from .command import *
from .controller import Controller


command_constructor = CommandConstructor()
# command_constructor.register("EXIT", None)
command_constructor.register("ADD", PlusCommand)


controller = Controller(
    parser=Parser(),
    constructor=command_constructor,
)

controller.run()





# >>> ADD 5 5
raw_line = "ADD 5 123"
# parser
tokens = [CommandToken("ADD"), NumberToken("5"), NumberToken("123")]
# constructor
command = PlusCommand()

command.execute(context)
