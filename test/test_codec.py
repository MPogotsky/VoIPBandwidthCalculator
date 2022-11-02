import pytest
from src.VoIP_Calculator.CodecTemplate import Codec


def test_codec_null_exception() -> None:
    with pytest.raises(Exception):
        codec = Codec("G.711 64kbps", 64)


def test_codec_frames_per_packet_calculations():
    """
    Test checks how Codec calculates number of frames needed
    based on bit rate and sample interval.
    """
    codec_sets_with_out = {
        Codec("G.711 64kbps", 64, sample_interval=0.125):     1,
        Codec("G.711 64kbps", 64, sample_interval=10.0):      80,
        Codec("G.728 16kbps", 16, sample_interval=10.0):      16,
        Codec("G.729 8kbps", 8, sample_interval=20.0):        2
    }

    for codec, expected_out in codec_sets_with_out.items():
        test_codec = codec
        assert (test_codec.frame_number == expected_out)
