"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class video_t(object):
    __slots__ = ["timestamp", "stream"]

    def __init__(self):
        self.timestamp = 0
        self.stream = [ 0 for dim0 in range(921600) ]

    def encode(self):
        buf = BytesIO()
        buf.write(video_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">q", self.timestamp))
        buf.write(struct.pack('>921600h', *self.stream[:921600]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != video_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return video_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = video_t()
        self.timestamp = struct.unpack(">q", buf.read(8))[0]
        self.stream = struct.unpack('>921600h', buf.read(1843200))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if video_t in parents: return 0
        tmphash = (0x33605d0574735bf7) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if video_t._packed_fingerprint is None:
            video_t._packed_fingerprint = struct.pack(">Q", video_t._get_hash_recursive([]))
        return video_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

