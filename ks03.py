import lzma, base64
exec(lzma.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

