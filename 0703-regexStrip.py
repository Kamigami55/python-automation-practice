import re

def regexStrip(content, removeWords=""):
    stripRegex = re.compile(r'[ '+removeWords+']*([^ '+removeWords+'].*[^ '+removeWords+'])[ '+removeWords+']*')
    return stripRegex.sub(r'\1', content)

print(regexStrip("     Hello, world!     "))
print(regexStrip("  abc Yooo cba    ", "bca"))
