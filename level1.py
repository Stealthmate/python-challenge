# http://www.pythonchallenge.com/pc/def/map.html

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

alph = "".join(chr(x) for x in range(ord("a"), ord("z") + 1))
t = str.maketrans(alph, alph[2:] + alph[:2])
# print(text.translate(t))

target = "map".translate(t)
print(f"http://www.pythonchallenge.com/pc/def/{target}.html")
