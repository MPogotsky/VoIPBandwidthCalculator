import pytest
from src.VoIP_Calculator.VoIP_Calculator import VoIP_Calculator
from src.VoIP_Calculator.CodecTemplate import Codec
from src.VoIP_Calculator.HeaderTemplate import Header


def test_voice_payload_size_calculations_on_sample_interval() -> None:
    """
    Test checks how voice_payload_size in bits is calculated
    based on bit rate and sample interval.
    """
    codec_sets_with_out = {
        Codec("G.711 64kbps", sample_interval=0.125):     8,
        Codec("G.711 64kbps", sample_interval=10.0):      640,
        Codec("G.728 12.8kbps", sample_interval=10.0):    128,
        Codec("G.729 8kbps", sample_interval=20.0):       160
    }

    for codec, expected_payload_size in codec_sets_with_out.items():
        headers = Header()
        calculator = VoIP_Calculator(headers, codec)

        assert (calculator.get_voice_payload_size() == expected_payload_size)


def test_voice_payload_size_calculations_on_number_of_frames() -> None:
    """
    Test checks how voice_payload_size in bits is calculated
    based on bit rate and a number of frames.
    """
    codec_sets_with_out = {
        Codec("G.711 64kbps", frames=1):         8,
        Codec("G.711 64kbps", frames=80):        640,
        Codec("G.728 12.8kbps", frames=16):      128,
        Codec("G.729 8kbps", frames=2):          160
    }

    for codec, expected_payload_size in codec_sets_with_out.items():
        headers = Header()
        calculator = VoIP_Calculator(headers, codec)

        assert (calculator.get_voice_payload_size() == expected_payload_size)


def test_codec_pps_calculations() -> None:
    """
    Test checks how VoIP_Calculator calculates packet
    rate for several codecs with no additional headers
    and one some sample interval.
    """
    codec_sets_with_pps = {
        Codec("G.711 64kbps", sample_interval=40):      25,
        Codec("G.729 8kbps", sample_interval=20):       50,
        Codec("G.723.1 5.3kbps", sample_interval=30):   33.3
    }

    for codec, expected_pps in codec_sets_with_pps.items():
        headers = Header()
        calculator = VoIP_Calculator(headers, codec)

        assert (calculator.get_pps() == expected_pps)
