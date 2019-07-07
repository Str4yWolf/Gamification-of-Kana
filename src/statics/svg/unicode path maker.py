# generate links to unicode website "fileformat.info"
# 
# include this in html
#
# to open pages: input_loop{ click link*, CTRL+Tab, Tab }
#
# to download SVGs: input_loop{ click SVG link*, CTRL+S, Enter, CTRL+W )}
#
# *activate mouse keys (Windows) with Alt+Shift+NumLock and use Num5 instead
#
# use own codepoints if custom is set True; 
# else generate links with range function and adjusting link template of String
custom = True
codepoints = "963f, 52a0, 6563, 591a, 5948, 516b, 672b, 4e5f, 826f, 548c, 4r95, 5229, 4e09, 6bd4, 4ec1, 5343, 4e4b, 5e7e, 6a5f, 4f0a, 5b87, 4e45, 9808, 5dde, 5ddd, 5974, 4e0d, 725f, 7531, 6d41, 6075, 973c, 5973, 90e8, 7962, 5929, 4e16, 4ecb, 6c5f, 65bc, 5df1, 66fd, 6b62, 4e43, 4fdd, 6bdb, 8207, 5442, 4e4e, 5c13".split(", ")

libSVM_reformatted = open("katakana_paths.txt", "a")
if custom:
  for code in codepoints:
    line = "<a href=\"https://www.fileformat.info/info/unicode/char/" + code + "/index.htm\" target=\"_blank\">" + code + "</a><br />"
    libSVM_reformatted.write(str(line))
    libSVM_reformatted.write("\n")
else:
  for i in range(160, 256):
    line = "<a href=\"https://www.fileformat.info/info/unicode/char/30" + hex(i)[2:] + "/index.htm\" target=\"_blank\">" + hex(i) + "</a><br />"
    libSVM_reformatted.write(str(line))
    libSVM_reformatted.write("\n")
libSVM_reformatted.close()
