#import re
from typing import Any, Dict, List, Text

from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
# from rasa.nlu.tokenizers import Token, Tokenizer
from rasa.nlu.tokenizers.tokenizer import Token, Tokenizer
# from rasa.nlu.training_data import Message, TrainingData
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData

from rasa.shared.nlu.constants import (
    RESPONSE,
    INTENT_RESPONSE_KEY,
    ENTITY_ATTRIBUTE_TYPE,
    ENTITY_ATTRIBUTE_GROUP,
    ENTITY_ATTRIBUTE_ROLE,
    NO_ENTITY_TAG,
    INTENT,
    ENTITIES,
    TEXT,
    ACTION_NAME,
    ACTION_TEXT,
)
from rasa.shared.nlu.training_data.message import Message

import MeCab

class KoreanTokenizer(Tokenizer, Component):

    defaults = {
        # Flag to check whether to split intents
        "intent_tokenization_flag": False,
        # Symbol on which intent should be split
        "intent_split_symbol": "_",
        # Text will be tokenized with case sensitive as default
        "case_sensitive": True,
    }

    supported_language_list = ["ko"]

    def __init__(self, component_config: Dict[Text, Any] = None) -> None:
        """Construct a new tokenizer using the WhitespaceTokenizer framework."""

        super().__init__(component_config)

        self.case_sensitive = self.component_config["case_sensitive"]

    
    def tokenize(self, message: Message, attribute: Text) -> List[Token]:
        mt = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ko-dic")
        text = message.get(attribute)
        parsed = mt.parse(text)
        if not parsed:
            return False
        x = parsed.replace("\n", "\t").split("\t")
        words = []
        for i in range(0, len(x) - 2, 2):
            w = x[i]
            words.append(w)

        running_offset = 0
        tokens = []
        for word in words:
            word_offset = text.index(word, running_offset)
            word_len = len(word)
            running_offset = word_offset + word_len
            tokens.append(Token(word, word_offset))
        return tokens

        # text = message.get(attribute)

        # if not self.case_sensitive:
        #     text = text.lower()
        # words = word_tokenize(text)

        # if not words:
        #     words = [text]

        # return self._convert_words_to_tokens(words, text)


