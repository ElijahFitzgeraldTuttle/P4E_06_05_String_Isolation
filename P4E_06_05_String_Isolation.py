str = 'X-DSPAN-Confidence: 0.8475 '
colon = str.find(':')
print(colon)
piece = str[colon + 1:]
piece = piece.strip()
print(piece)