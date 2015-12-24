class PushdownAutomaton:
    class Eps:
        def __str__(self):
            return u'\u03B5'

    def __init__(self, name, states, input_alphabet, stack_alphabet,
                       start_state, final_state, rules, start_stack):
        self.__name = name
        self.__states = states
        self.__input_alphabet = input_alphabet
        self.__stack_alphabet = stack_alphabet
        self.__start_state = start_state
        self.__final_state = final_state
        self.__rules = rules
        self.__start_stack = start_stack

    @property
    def name(self):
        return self.__name

    @property
    def states(self):
        return self.__states

    @property
    def input_alphabet(self):
        return self.__input_alphabet

    @property
    def stack_alphabet(self):
        return self.__stack_alphabet

    @property
    def start_state(self):
        return self.__start_state

    @property
    def final_state(self):
        return self.__final_state

    @property
    def rules(self):
        return self.__rules

    @property
    def start_stack(self):
        return self.__start_stack

    def print_info(self):
        print('Name:', self.__name)
        print('States:', ', '.join(map(str, self.__states)))
        print('Input alphabet:', ', '.join(self.__input_alphabet))
        print('Stack alphabet:', ', '.join(self.__stack_alphabet))
        print('Start state:', self.__start_state)
        print('Final state:', self.__final_state)
        print('Start stack symbol:', self.__start_stack)
        print('Rules:')

        index = 0
        for rule in self.__rules.items():
            for new_state in rule[1]:
                for new_stack in rule[1][new_state]:
                    index += 1
                    print('\tRule #{}'.format(index))
                    print('\t\tFrom state:', rule[0][0])
                    print('\t\tInput:', rule[0][1])
                    print('\t\tFrom stack:', rule[0][2])
                    print('\t\tTo state:', new_state)
                    print('\t\tTo stack:', new_stack)










 
