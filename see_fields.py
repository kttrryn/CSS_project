
# see what columns are available for comments or posts to get from zst

import zstandard as zstd
import json

file_path = r"/zsts/Askpolitics_comments.zst"

with open(file_path, "rb") as fh:
    dctx = zstd.ZstdDecompressor()
    with dctx.stream_reader(fh) as reader:
        text_stream = ""
        while True:
            chunk = reader.read(2**20)
            if not chunk:
                break
            text_stream += chunk.decode("utf-8")
            lines = text_stream.split("\n")
            text_stream = lines.pop()
            for line in lines:
                if line.strip():
                    obj = json.loads(line)
                    print(obj.keys())
                    raise SystemExit