#!/usr/bin/env python3

# class MyString:
#   pass


# class MyString:

#     def __init__(self, value=""):
#         self._value = value

#     @property
#     def value(self):
#         """The stored string value."""
#         return self._value

#     @value.setter
#     def value(self, string_val):
#         """Sets the string value, enforcing type check and informative message."""
#         if not isinstance(string_val, str):
#             raise TypeError("The value must be a string.")
#         self._value = string_val

#     def is_sentence(self):
#         """Checks if the string ends with a period (.)."""
#         return self._value.endswith(".")

#     def is_question(self):
#         """Checks if the string ends with a question mark (?)."""
#         return self._value.endswith("?")

#     def is_exclamation(self):
#         """Checks if the string ends with an exclamation mark (!)."""
#         return self._value.endswith("!")

#     def count_sentences(self):
#         """Counts the number of sentences in the string, handling different punctuation."""
#         value = self.value
#         sentences = []

#         # Split on all sentence-ending punctuation (.?!) and remove empty strings
#         for punct in ['.', '!', '?']:
#             sentences.extend(s.strip() for s in value.split(punct) if s)

#         return len(sentences)


class MyString:

  def __init__(self, value = ""):
    self._value = value
    
  def get_value(self):
    return self._value

  def set_value(self, stringVal):
    if (type(stringVal) == str):
      self._value = stringVal
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
    return self._value.endswith(".")

  def is_question(self):
    return self._value.endswith("?")

  def is_exclamation(self):
    return self._value.endswith("!")

  def count_sentences(self):
    value = self.value
    for punc in ['!','?']:
        value = value.replace(punc, '.')
    
    sentences = [s for s in value.split('.') if s]
    
    return len(sentences)