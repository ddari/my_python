s = "Мой дядя самых честных правил,Когда не в шутку занемог,Он уважать себя заставил И лучше выдумать не мог"
s=(' '.join([ word for word in s.split() if not word.startswith('м') ]))
print(s)
