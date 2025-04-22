import pytest
from vi_number.number2word import n2w, n2w_single
from vi_number.number2word.units import n2w_units
from vi_number.number2word.hundreds import n2w_hundreds
from vi_number.number2word.large_number import n2w_large_number, n2w_float_number


@pytest.mark.parametrize(
    "number,expected",
    [
        ('0', 'không'),
        ('1', 'một'),
        ('2', 'hai'),
        ('3', 'ba'),
        ('4', 'bốn'),
        ('5', 'năm'),
        ('6', 'sáu'),
        ('7', 'bảy'),
        ('8', 'tám'),
        ('9', 'chín'),
    ],
)
def test_n2w_units(number, expected):
    """Test conversion of single digit numbers to words."""
    assert n2w_units(number) == expected


def test_n2w_units_errors():
    """Test error handling for n2w_units."""
    with pytest.raises(ValueError):
        n2w_units('')  # Empty string
    
    with pytest.raises(ValueError):
        n2w_units('10')  # Number > 9


@pytest.mark.parametrize(
    "number,expected",
    [
        ('0', 'không'),
        ('1', 'một'),
        ('10', 'mười'),
        ('11', 'mười một'),
        ('15', 'mười lăm'),
        ('20', 'hai mươi'),
        ('21', 'hai mươi mốt'),
        ('25', 'hai mươi lăm'),
        ('100', 'một trăm'),
        ('101', 'một trăm lẻ một'),
        ('111', 'một trăm mười một'),
        ('121', 'một trăm hai mươi mốt'),
        ('200', 'hai trăm'),
        ('805', 'tám trăm lẻ năm'),
        ('815', 'tám trăm mười lăm'),
        ('825', 'tám trăm hai mươi lăm'),
        ('999', 'chín trăm chín mươi chín'),
    ],
)
def test_n2w_hundreds(number, expected):
    """Test conversion of numbers from 0-999 to words."""
    assert n2w_hundreds(number) == expected


def test_n2w_hundreds_errors():
    """Test error handling for n2w_hundreds."""
    with pytest.raises(ValueError):
        n2w_hundreds('')  # Empty string
    
    with pytest.raises(ValueError):
        n2w_hundreds('1000')  # Number > 999


@pytest.mark.parametrize(
    "number,expected",
    [
        ('1000', 'một nghìn'),
        ('1001', 'một nghìn không trăm lẻ một'),
        ('1100', 'một nghìn một trăm'),
        ('1234', 'một nghìn hai trăm ba mươi bốn'),
        ('10000', 'mười nghìn'),
        ('100000', 'một trăm nghìn'),
        ('1000000', 'một triệu'),
        ('1000001', 'một triệu không trăm lẻ một'),
        ('1234567', 'một triệu hai trăm ba mươi bốn nghìn năm trăm sáu mươi bảy'),
        ('1000000000', 'một tỷ'),
        ('1234567890', 'một tỷ hai trăm ba mươi bốn triệu năm trăm sáu mươi bảy nghìn tám trăm chín mươi'),
        ('-1234', 'âm một nghìn hai trăm ba mươi bốn'),
    ],
)
def test_n2w_large_number(number, expected):
    """Test conversion of large numbers to words."""
    assert n2w_large_number(number) == expected


@pytest.mark.parametrize(
    "number,expected",
    [
        ('1,5', 'một phẩy năm'),
        ('10,01', 'mười phẩy không một'),
        ('100,001', 'một trăm phẩy không không một'),
        ('1000,1', 'một nghìn phẩy một'),
        ('-1,5', 'âm một phẩy năm'),
    ],
)
def test_n2w_float_number(number, expected):
    """Test conversion of float numbers to words."""
    assert n2w_float_number(number) == expected


@pytest.mark.parametrize(
    "number,expected",
    [
        ('0', 'không'),
        ('1', 'một'),
        ('10', 'mười'),
        ('100', 'một trăm'),
        ('1000', 'một nghìn'),
        ('1000000', 'một triệu'),
        ('1000000000', 'một tỷ'),
        ('1,5', 'một phẩy năm'),
        ('1.000', 'một nghìn'),
        ('1.000.000', 'một triệu'),
        ('-1', 'âm một'),
        ('-1000', 'âm một nghìn'),
    ],
)
def test_n2w(number, expected):
    """Test the main n2w function."""
    assert n2w(number) == expected


@pytest.mark.parametrize(
    "number,expected",
    [
        ('0', 'không'),
        ('1', 'một'),
        ('123', 'một hai ba'),
        ('0908123456', 'không chín không tám một hai ba bốn năm sáu'),
    ],
)
def test_n2w_single(number, expected):
    """Test the n2w_single function."""
    assert n2w_single(number) == expected
