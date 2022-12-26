import pytest
from src.VoIP_Calculator.Codec import Codec


def test_codec_null_exception() -> None:
    with pytest.raises(Exception):
        codec = Codec("G.711 64kbps")


def test_codec_frames_per_packet_calculations() -> None:
    """
    Test checks how Codec calculates number of frames needed
    based on bit rate and sample interval.
    """
    codec_sets_with_out = {
        Codec("G.711 64kbps", voice_payload_size=10):        1,
        Codec("G.711 64kbps", voice_payload_size=40):        4,
        Codec("G.728 12.8kbps", voice_payload_size=10.0):    2,
        Codec("G.729 8kbps", voice_payload_size=20.0):       2
    }

    for codec, expected_out in codec_sets_with_out.items():
        test_codec = codec
        assert (test_codec.frame_number == expected_out)
