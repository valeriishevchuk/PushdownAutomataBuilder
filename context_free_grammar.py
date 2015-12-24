class ContextFreeGrammar:
    def __init__(self, non_terminals, terminals, rules, start_symbol):
        assert start_symbol in non_terminals
        self.__non_terminals = non_terminals
        self.__terminals = terminals
        self.__rules = rules
        self.__start_symbol = start_symbol

    @property
    def non_terminals(self):
        return self.__non_terminals

    @property
    def terminals(self):
        return self.__terminals

    @property
    def rules(self):
        return self.__rules

    @property
    def start_symbol(self):
        return self.__start_symbol
