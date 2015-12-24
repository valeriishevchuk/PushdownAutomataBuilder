from context_free_grammar import ContextFreeGrammar
from pda_builder import PdaBuilder

if __name__ == '__main__':
    rules = {
                'S': [
                        ['S', 'S'],
                        ['(', 'S', ')'],
                        ['(', ')']
                     ]
            }
    grammar = ContextFreeGrammar(frozenset(['S']), frozenset(['(', ')']), rules, 'S')

    pda_builder = PdaBuilder()
    pda = pda_builder.build_from_cf_grammar('Well-formed parentheses', grammar)
    pda.print_info()
