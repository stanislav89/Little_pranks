''' Написать функцию перевода размеров женского белья из международного во все остальные '''
''' Write a function for converting lingerie sizes from international to all others '''


def clothing_size():
    size_table = {
        'xxs': ['Ukraine: 42', 'Germany: 36', 'USA: 8', 'France: 38', 'England: 24'],
        'xs': ['Ukraine: 44', 'Germany: 38', 'USA: 10', 'France: 40', 'England: 26'],
        's': ['Ukraine: 46', 'Germany: 40', 'USA: 12', 'France: 42', 'England: 28'],
        'm': ['Ukraine: 48', 'Germany: 42', 'USA: 14', 'France: 44', 'England: 30'],
        'l': ['Ukraine: 50', 'Germany: 44', 'USA: 16', 'France: 46', 'England: 32'],
        'xl': ['Ukraine: 52', 'Germany: 46', 'USA: 18', 'France: 48', 'England: 34'],
        'xxl': ['Ukraine: 54', 'Germany: 48', 'USA: 20', 'France: 50', 'England: 36'],
        'xxxl': ['Ukraine: 56', 'Germany: 50', 'USA: 22', 'France: 52', 'England: 38']
    }
    international_size = input('*** Enter international size (XXS, XS, S, M, L, XL, XXL or XXXL): ').lower()
    for i in size_table:
        if international_size == i:
            print(size_table[i])
            break
        else:
            pass


clothing_size()
