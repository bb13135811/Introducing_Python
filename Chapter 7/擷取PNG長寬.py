from construct import Struct, Magic, UBInt32, Const, String
fmt = Struct('png',
    Magic(b'\x89PNG\r\n\x1a\n'),
    UBInt32('length'),
    Const(String('type', 4), b'IHDR'),
    UBInt32('width'),
    UBInt32('height')
    )
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
    b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
result = fmt.parse(data)
print(result)