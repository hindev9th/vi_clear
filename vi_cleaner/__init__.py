"""
vi_cleaner - Vietnamese text normalization library for text-to-speech

This package provides tools for normalizing Vietnamese text, including:
- Number normalization
- Date and time normalization
- Currency normalization
- Measurement unit normalization
- Abbreviation expansion
- Roman numeral conversion
- Symbol normalization
- And more
"""

import sys

# Check Python version
try:
    version_info = sys.version_info
    if version_info < (3, 7, 0):
        raise RuntimeError("vi_cleaner requires Python 3.7 or later")
except Exception:
    pass

###########################################################
# METADATA
###########################################################

__author__ = """Nguyen Hien"""
__email__ = 'hindev9th@gmail.com'
__version__ = '0.0.1'

###########################################################
# TOP-LEVEL MODULES
###########################################################

# Main cleaner class
from .vi_cleaner import ViCleaner

# Individual normalization modules
from .numberical_vi import normalize_number_vi
from .datestime_vi import normalize_date, normalize_time
from .currency_vi import normalize_currency_vi
from .measurement_vi import normalize_measurement_vi
from .roman_number_vi import normalize_roman_numbers
from .abbreviation_vi import normalize_abbreviations_vi, normalize_speacial_symbol_vi
from .acronym_vi import spell_acronyms_vi
from .letter_vi import normalize_letter_vi
from .symbol_vi import (
    DEFAULT_PIECE_MAX_LENGTH,
    DEFAULT_SENTENCE_MAX_LENGTH,
    vietnamese_re,
    vietnamese_without_num_re,
    vietnamese_set
)

# Utility modules
from .passage_utils import split_text_passages, combine_passages, split_long_passages
from .sentence_utils import get_pieces, split_text_sentences, combine_sentences

__all__ = [
    # Main class
    'ViCleaner',
    
    # Normalization functions
    'normalize_number_vi',
    'normalize_date',
    'normalize_time',
    'normalize_currency_vi',
    'normalize_measurement_vi',
    'normalize_roman_numbers',
    'normalize_abbreviations_vi',
    'normalize_speacial_symbol_vi',
    'spell_acronyms_vi',
    'normalize_letter_vi',
    
    # Constants and regex patterns
    'DEFAULT_PIECE_MAX_LENGTH',
    'DEFAULT_SENTENCE_MAX_LENGTH',
    'vietnamese_re',
    'vietnamese_without_num_re',
    'vietnamese_set',
    
    # Utility functions
    'split_text_passages',
    'combine_passages',
    'split_long_passages',
    'get_pieces',
    'split_text_sentences',
    'combine_sentences'
]