from scipy.stats import chi2

def test(x, alpha, k):
    print('Проверяем критерий Пирсона для величены %s\r\n с %s степенями свободы\r\nи уровнем доверия %s' % (x, k, alpha))
    q1 = chi2.ppf(alpha, k)
    print('Квантиль q1 = %s' % q1)
    q2 = chi2.ppf(1 - alpha, k)
    print('Квантиль q2 = %s' % q2)
    res = x > q1 and x < q2
    print('Проверка гипотезы H0\r\nГопотеза H0 %s' % ({
        True:'верна',
         False:'не верна,\r\nпоэтому примем гипотезу H1'}[res],) )
    return res
