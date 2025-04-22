import sys

# Check python version
try:
    version_info = sys.version_info
    if version_info < (3, 6, 0):
        raise RuntimeError("vi-number requires Python 3.6 or later")
except Exception:
    pass

###########################################################
# METADATA
###########################################################

__author__ = """Lê Nguyên Hiện"""
__email__ = 'hindev9th@gmail.com'

# Version
__version__ = '1.0.3'


###########################################################
# TOP-LEVEL MODULES
###########################################################

from vi_number.number2word import n2w, n2w_single
from vi_number.word2number import w2n, w2n_couple, w2n_single

__all__ = ['w2n', 'w2n_couple', 'w2n_single', 'n2w', 'n2w_single']