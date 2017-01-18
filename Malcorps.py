print 'How many malcorps did you find on planet Exflon?' ,
Exflon = raw_input()
print 'How many malcorps did you find on planet Mobiles?' ,
Mobiles = raw_input()
print 'How many malcorps did you find on planet Monsantoes?' ,
Monsantoes = raw_input()
Total = int(Exflon) + int(Mobiles) + int(Monsantoes)
print 'You found a total of %s Malcorps!' % Total
print 'The average number of Malcorps is %.2f' % (int(Total)/3.0)