#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            print("The value must be a string.")
            self._value = ''

        else:
            self._value = value
            
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value
            
    def is_sentence(self):
        if self._value.endswith('.'):
            return True
        else:
            return False
        
    def is_question(self):
        if self._value.endswith('?'):
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self._value.endswith('!'):
            return True
        else:
            return False
        
    def count_sentences(self):
        sentence_endings = ['.', '?', '!']
        sentences = [s.strip() for s in self._value.split(' ') if any(s.endswith(end) for end in sentence_endings)]
        return len(sentences)