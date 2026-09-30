
import re

class TokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}

        self.patterns = r'''([.,;:"!?()']|--|\s)'''

    def encode(self, text):
        """Encodes text into unique IDs."""

        preprocessed = re.split(self.patterns, text)

        preprocessed = [
            item.strip()
            for item in preprocessed
            if item.strip()
        ]

        ids = [self.str_to_int[s] for s in preprocessed]

        return ids

    def decode(self, ids):
        """Decodes IDs into vocabulary words."""

        text = " ".join(
            self.int_to_str[i]
            for i in ids
        )

        text = re.sub(
            r'''\s+([,.?!"()'])''',
            r'\1',
            text
        )

        return text
