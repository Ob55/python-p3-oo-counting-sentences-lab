#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        if self.value.endswith('.'):
            return True
        else:
            return False

    def is_question(self):
        if self.value.endswith('?'):
            return True
        else:
            return False

    def is_exclamation(self):
        if self.value.endswith('!'):
            return True
        else:
            return False

    def count_sentences(self):
        sentences = [s.strip() for s in self.value.split('.') if s.strip()]
        sentences += [s.strip() for s in self.value.split('?') if s.strip()]
        sentences += [s.strip() for s in self.value.split('!') if s.strip()]
        return len(sentences)


