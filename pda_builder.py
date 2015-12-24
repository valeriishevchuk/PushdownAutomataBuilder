from collections import defaultdict
from pushdown_automaton import PushdownAutomaton

class PdaBuilder:
    def __init__(self):
        pass

    def build_from_cf_grammar(self, name, grammar):
        start_state = 1
        final_state = 2
        states = frozenset([start_state, final_state])
        input_alphabet = grammar.terminals
        stack_alphabet = grammar.terminals | grammar.non_terminals
        start_stack = grammar.start_symbol
        rules = {}

        for left, right in grammar.rules.items():
            key = (start_state, None, left)
            if key not in rules:
                rules[key] = defaultdict(list)

                rules[key][start_state] += right

        for terminal in grammar.terminals:
            key = (start_state, terminal, terminal)
            if key not in rules:
                rules[key] = defaultdict(list)

            rules[key][start_state].append(PushdownAutomaton.Eps())

        key = (start_state, '#', PushdownAutomaton.Eps())
        rules[key] = defaultdict(list)
        rules[key][final_state].append(PushdownAutomaton.Eps())

        return PushdownAutomaton(name, states, input_alphabet, stack_alphabet,
                                 start_state, final_state, rules, start_stack)
