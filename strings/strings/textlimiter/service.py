# coding=utf-8
__author__ = 'lgavinho'

import textwrap
import numpy as np


class TextFormatter:

    MINIMUM_NUMBER_OF_WORDS_PER_LINE = 2
    BREAK_LINE = '\n'
    BREAK_PARAGRAPH = '\n\n'
    WORD_SEPARATOR = ' '

    source_text = ''

    def __init__(self, text):
        self.source_text = text

    def get_words(self, source):
        source_lines = source.split(self.BREAK_LINE)
        words = []
        for line in source_lines:
            line_words = line.split(self.WORD_SEPARATOR)
            # remove empty words
            filtered = list(filter(None, line_words))
            words += filtered
        return words

    def get_order_to_add_spaces_to_justify_text(self, number_of_words):
        even = number_of_words % 2 == 0
        if even:
            array_size = number_of_words
        else:
            array_size = number_of_words - 1
        columns_size = int(array_size/2)
        rows_size = 2
        a = np.arange(array_size).reshape(rows_size, columns_size)
        b = np.fliplr(a)
        row_position = 0
        column_position = 0
        order_to_add_spaces = []
        if even:
            column_position = 1
            order_to_add_spaces = [b[0, 0]]

        while column_position < columns_size and row_position < rows_size:
            order_to_add_spaces.append(b[row_position, column_position])
            if row_position == 0:
                row_position = 1
            else:
                row_position = 0
                column_position += 1
        return order_to_add_spaces

    def justify_text_line(self, text, line_size_chars=40):
        # check if it is already justify
        if len(text) == line_size_chars:
            return text

        words = self.get_words(source=text)
        number_of_words = len(words)

        if number_of_words <= self.MINIMUM_NUMBER_OF_WORDS_PER_LINE:
            return text

        word_order_to_add_spaces = self.get_order_to_add_spaces_to_justify_text(number_of_words=number_of_words)
        number_of_spaces_to_add_in_line = line_size_chars - len(text)
        current_position_to_add_space = 0
        words_spaces = {}
        for number_of_spaces in range(1, number_of_spaces_to_add_in_line + 1):
            add_space_to = word_order_to_add_spaces[current_position_to_add_space]
            current_position_to_add_space += 1
            if current_position_to_add_space >= len(word_order_to_add_spaces):
                current_position_to_add_space = 0

            if add_space_to in words_spaces:
                words_spaces[add_space_to] += 1
            else:
                words_spaces[add_space_to] = 1

        # build the line
        new_line = ''
        for word_position in range(0, number_of_words):
            number_of_extra_spaces = 0
            if word_position in words_spaces:
                number_of_extra_spaces = words_spaces[word_position]
            spaces = ' ' * (number_of_extra_spaces + 1)
            new_line += words[word_position] + spaces

        return new_line.rstrip()

    def cleanup_text(self):
        all_paragraphs = self.source_text.split(self.BREAK_PARAGRAPH)
        output = ''
        for paragraph in all_paragraphs:
            lines = paragraph.split(self.BREAK_LINE)
            for line in lines:
                cleaned_extra_spaces = line.replace('  ', ' ')
                cleaned_line = cleaned_extra_spaces.rstrip().lstrip()
                output += cleaned_line + self.BREAK_LINE
            if output != '':
                output += self.BREAK_LINE
        return output

    def limiter(self, line_size_chars=40):
        text = self.cleanup_text()
        if text == '':
            return self.source_text

        # Wrap this text.
        wrapper = textwrap.TextWrapper(width=line_size_chars)
        all_paragraphs = self.source_text.split(self.BREAK_PARAGRAPH)
        output = ''
        for paragraph in all_paragraphs:
            wrapped = wrapper.fill(text=paragraph)
            if output != '':
                output += self.BREAK_PARAGRAPH
            output += wrapped
        return output

    def limiter_and_justify(self, line_size_chars=40):
        if self.source_text == '':
            return self.source_text

        text = self.limiter(line_size_chars=line_size_chars)
        # justify each line
        if text == '':
            return text

        all_paragraphs = text.split(self.BREAK_PARAGRAPH)
        output = ''
        for paragraph in all_paragraphs:
            lines = paragraph.split(self.BREAK_LINE)
            for line in lines:
                justified_line = self.justify_text_line(text=line, line_size_chars=line_size_chars)
                output += justified_line + self.BREAK_LINE
            if output != '':
                output += self.BREAK_LINE
        return output



