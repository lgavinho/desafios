# coding=utf-8
__author__ = 'lgavinho'

from django.test import TestCase
from django.conf import settings

from textlimiter.service import TextFormatter

class textFormatterTest(TestCase):

    fixtures_base = ''

    def setUp(self):
        self.fixtures_base = base = settings.BASE_DIR + '/textlimiter/fixtures/'

    def count_words(self, text):
        source_lines = text.split('\n')
        total_words = 0
        for line in source_lines:
            line_words = line.split(' ')
            # remove empty words
            filtered = list(filter(None, line_words))
            total_words += len(filtered)
        return total_words

    def test_limit_with_40_chars_sample1(self):
        # test parameter
        maxchars = 40
        # get fixtures
        sample = 'sample1.txt'
        file = open(self.fixtures_base + sample, 'r')
        text = file.read()
        # running service
        service = TextFormatter(text=text)
        result = service.limiter(line_size_chars=maxchars)

        # assert result size
        total_of_source_words = self.count_words(text=text)
        total_of_result_words = self.count_words(text=result)
        self.assertEqual(total_of_source_words, total_of_result_words)
        # assert size of each line
        splited = result.split('\n')
        for line in splited:
            self.assertTrue(len(line) <= maxchars)

    def test_limit_with_40_chars_sample2(self):
        # test parameter
        maxchars = 40
        # get fixtures
        sample = 'sample2.txt'
        file = open(self.fixtures_base + sample, 'r')
        text = file.read()
        # running service
        service = TextFormatter(text=text)
        result = service.limiter(line_size_chars=maxchars)

        # assert result size
        total_of_source_words = self.count_words(text=text)
        total_of_result_words = self.count_words(text=result)
        self.assertEqual(total_of_source_words, total_of_result_words)
        # assert size of each line
        splited = result.split('\n')
        for line in splited:
            self.assertTrue(len(line) <= maxchars)

    def test_limit_with_40_chars_sample3(self):
        # test parameter
        maxchars = 40
        # get fixtures
        sample = 'sample3.txt'
        file = open(self.fixtures_base + sample, 'r')
        text = file.read()
        # running service
        service = TextFormatter(text=text)
        result = service.limiter(line_size_chars=maxchars)

        # assert result size
        total_of_source_words = self.count_words(text=text)
        total_of_result_words = self.count_words(text=result)
        self.assertEqual(total_of_source_words, total_of_result_words)
        # assert size of each line
        splited = result.split('\n')
        for line in splited:
            self.assertTrue(len(line) <= maxchars)

    def test_limit_with_40_chars_sample4(self):
        # test parameter
        maxchars = 40
        # get fixtures
        sample = 'sample4.txt'
        file = open(self.fixtures_base + sample, 'r')
        text = file.read()
        # running service
        service = TextFormatter(text=text)
        result = service.limiter(line_size_chars=maxchars)

        # assert result size
        total_of_source_words = self.count_words(text=text)
        total_of_result_words = self.count_words(text=result)
        self.assertEqual(total_of_source_words, total_of_result_words)
        # assert size of each line
        splited = result.split('\n')
        for line in splited:
            self.assertTrue(len(line) <= maxchars)

    def test_limit_with_40_chars_empty_source(self):
        # test parameter
        maxchars = 40
        # running service
        service = TextFormatter(text='')
        result = service.limiter(line_size_chars=maxchars)
        self.assertEqual('', result)

    def test_limit_with_80_chars_sample4(self):
        # test parameter
        maxchars = 80
        # get fixtures
        sample = 'sample4.txt'
        file = open(self.fixtures_base + sample, 'r')
        text = file.read()
        # running service
        service = TextFormatter(text=text)
        result = service.limiter(line_size_chars=maxchars)

        # assert result size
        total_of_source_words = self.count_words(text=text)
        total_of_result_words = self.count_words(text=result)
        self.assertEqual(total_of_source_words, total_of_result_words)
        # assert size of each line
        splited = result.split('\n')
        for line in splited:
            self.assertTrue(len(line) <= maxchars)

    def test_justify_alignment(self):
        # test parameter
        maxchars = 40
        text = 'and the earth. Now the earth was'
        # running service
        service = TextFormatter(text=text)
        result = service.justify_text_line(text=text, line_size_chars=maxchars)
        self.assertEqual(maxchars, len(result))
        text = '"day," and the darkness he called'
        service = TextFormatter(text=text)
        result = service.justify_text_line(text=text, line_size_chars=maxchars)
        self.assertEqual(maxchars, len(result))


    def test_limit_with_40_chars_and_justify_sample1(self):
        # test parameter
        maxchars = 40
        # get fixtures
        sample = 'sample1.txt'
        file = open(self.fixtures_base + sample, 'r')
        text = file.read()
        # running service

        service = TextFormatter(text=text)
        result = service.limiter_and_justify(line_size_chars=maxchars)

        # assert size of each line
        all_lines = result.split('\n')
        for line in all_lines:
            if line != '\n\n':
                length_of_line = len(line)
                if length_of_line > 0 and self.count_words(line) > TextFormatter.MINIMUM_NUMBER_OF_WORDS_PER_LINE:
                    self.assertTrue(len(line) == maxchars)

    def test_limit_with_40_chars_and_justify_sample2(self):
        # test parameter
        maxchars = 40
        # get fixtures
        sample = 'sample2.txt'
        file = open(self.fixtures_base + sample, 'r')
        text = file.read()
        # running service

        service = TextFormatter(text=text)
        result = service.limiter_and_justify(line_size_chars=maxchars)

        # assert size of each line
        all_lines = result.split('\n')
        for line in all_lines:
            if line != '\n\n':
                length_of_line = len(line)
                if length_of_line > 0 and self.count_words(line) > TextFormatter.MINIMUM_NUMBER_OF_WORDS_PER_LINE:
                    self.assertTrue(len(line) == maxchars)

    def test_limit_with_40_chars_and_justify_sample3(self):
        # test parameter
        maxchars = 40
        # get fixtures
        sample = 'sample3.txt'
        file = open(self.fixtures_base + sample, 'r')
        text = file.read()
        # running service

        service = TextFormatter(text=text)
        result = service.limiter_and_justify(line_size_chars=maxchars)

        # assert size of each line
        all_lines = result.split('\n')
        for line in all_lines:
            if line != '\n\n':
                length_of_line = len(line)
                if length_of_line > 0 and self.count_words(line) > TextFormatter.MINIMUM_NUMBER_OF_WORDS_PER_LINE:
                    self.assertTrue(len(line) == maxchars)

    def test_limit_with_40_chars_and_justify_sample4(self):
        # test parameter
        maxchars = 40
        # get fixtures
        sample = 'sample4.txt'
        file = open(self.fixtures_base + sample, 'r')
        text = file.read()
        # running service

        service = TextFormatter(text=text)
        result = service.limiter_and_justify(line_size_chars=maxchars)

        # assert size of each line
        all_lines = result.split('\n')
        for line in all_lines:
            if line != '\n\n':
                length_of_line = len(line)
                if length_of_line > 0:
                    self.assertTrue(len(line) == maxchars)

    def test_limit_with_80_chars_and_justify_sample4(self):
        # test parameter
        maxchars = 80
        # get fixtures
        sample = 'sample4.txt'
        file = open(self.fixtures_base + sample, 'r')
        text = file.read()
        # running service

        service = TextFormatter(text=text)
        result = service.limiter_and_justify(line_size_chars=maxchars)

        # assert size of each line
        all_lines = result.split('\n')
        for line in all_lines:
            if line != '\n\n':
                length_of_line = len(line)
                if length_of_line > 0:
                    self.assertTrue(len(line) == maxchars)

    def test_limit_with_35_chars_and_justify_sample4(self):
        # test parameter
        maxchars = 35
        # get fixtures
        sample = 'sample4.txt'
        file = open(self.fixtures_base + sample, 'r')
        text = file.read()
        # running service

        service = TextFormatter(text=text)
        result = service.limiter_and_justify(line_size_chars=maxchars)

        # assert size of each line
        all_lines = result.split('\n')
        for line in all_lines:
            if line != '\n\n':
                length_of_line = len(line)
                if length_of_line > 0:
                    self.assertTrue(len(line) == maxchars)

    def test_limit_with_40_chars_and_justify_empty_source(self):
        # test parameter
        maxchars = 40
        # running service
        service = TextFormatter(text='')
        result = service.limiter_and_justify(line_size_chars=maxchars)
        self.assertEqual('', result)

    def test_limit_with_40_chars_and_justify_source_with_only_some_spaces(self):
        # test parameter
        maxchars = 40
        # running service
        service = TextFormatter(text='     ')
        result = service.limiter_and_justify(line_size_chars=maxchars)
        self.assertEqual('', result)

    def test_limit_with_41_chars_and_justify_sample5(self):
        # test parameter
        maxchars = 37
        # get fixtures
        sample = 'sample5.txt'
        file = open(self.fixtures_base + sample, 'r')
        text = file.read()
        # running service

        service = TextFormatter(text=text)
        result = service.limiter_and_justify(line_size_chars=maxchars)

        # assert size of each line
        all_lines = result.split('\n')
        for line in all_lines:
            if line != '\n\n':
                length_of_line = len(line)
                if length_of_line > 0:
                    self.assertTrue(len(line) == maxchars)