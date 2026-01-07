#! venv/bin/python3

def calculate_total(subtotal: float, rate: float = 20) -> float:
    '''
    calculate total amount, given subtotal and vat rate
    vat rate should be provided as a percentage
    >>> calculate_total(100, 20)
    120.0
    >>> calculate_total(10, 50)
    15.0
    '''
    vat = (rate / 100) * subtotal
    return subtotal + vat

if __name__ == '__main__':
    print(calculate_total(100, 20))