from .CodecTemplate import Codec

CodecSets = {
    # "<codec_name> <bit_rate>": Codec(bit_rate [kbps], sample_size [Bytes])
    "G.723.1 5.3kbps": Codec(5.3, 20, 30)
}
