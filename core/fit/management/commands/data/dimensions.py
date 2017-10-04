try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

text = StringIO("""Id|Name|Divisor|Description
1|Cognitive|6|NULL
2|Emotional|6|NULL
3|Physical|8|NULL
4|Financial|5|NULL""")
