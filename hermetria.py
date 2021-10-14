from hermetrics.hamming import Hamming

ham = Hamming()

ham.distance('abcd', 'abce') # 1
ham.normalized_distance('abcd', 'abce') # 0.25
ham.similarity('abcd', 'abce') # 0.75

print(ham.distance('luis', 'luia'))