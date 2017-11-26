from scipy.stats import chi2

def test(x, alpha, k):
    q1 = chi2.ppf(alpha, k)
    q2 = chi2.ppf(1 - alpha, k)
    return x > q1 and x < q2
