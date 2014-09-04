__author__ = 'gengjie'


def quick_sort(ls):
    return [] if ls == [] else quick_sort([y for y in ls[1:] if y < ls[0]]) + [ls[0]] + quick_sort(
        [y for y in ls[1:] if y >= ls[0]])

if __name__ == '__main__':
    l1 = [3,56,8,1,34,56,89,234,56,231,45,90,33,66,88,11,22]
    l2 = quick_sort(l1)
    print l1
    print l2