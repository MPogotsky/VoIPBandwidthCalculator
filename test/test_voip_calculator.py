import pytest
from src.VoIP_Calculator.VoIP_Calculator import VoIP_Calculator
from src.VoIP_Calculator.CodecTemplate import Codec


def test_voice_payload_size_calculations_on_sample_interval() -> None:
    """
    Test checks how voice_payload_size in bits is calculated
    based on bit rate and sample interval.
    """
    codec_sets_with_out = {
        Codec("G.711 64kbps", 64, sample_interval=0.125):     8,
        Codec("G.711 64kbps", 64, sample_interval=10.0):      640,
        Codec("G.728 16kbps", 16, sample_interval=10.0):      160,
        Codec("G.729 8kbps", 8, sample_interval=20.0):        160
    }

    for codec, expected_out in codec_sets_with_out.items():
        headers = 0
        calculator = VoIP_Calculator(headers, codec)

        assert (calculator.get_voice_payload_size() == expected_out)


def test_voice_payload_size_calculations_on_number_of_frames() -> None:
    """
    Test checks how voice_payload_size in bits is calculated
    based on bit rate and a number of frames.
    """
    codec_sets_with_out = {
        Codec("G.711 64kbps", 64, frames=1):         8,
        Codec("G.711 64kbps", 64, frames=80):        640,
        Codec("G.728 16kbps", 16, frames=16):        160,
        Codec("G.729 8kbps",   8, frames=2):         160
    }

    for codec, expected_out in codec_sets_with_out.items():
        headers = 0
        calculator = VoIP_Calculator(headers, codec)

        assert (calculator.get_voice_payload_size() == expected_out)


def test_codec_pps_calculations():
    """
    Test checks how VoIP_Calculator calculates packet
    rate for several codecs with no additional headers
    and one some sample interval.
    """
    codec_sets_with_pps = {
        Codec("G.711 64kbps", 64, sample_interval=40):      25,
        Codec("G.729 8kbps", 8, sample_interval=20):        50,
        Codec("G.723.1 5.3kbps", 5.3, sample_interval=30):  33.3
    }

    for codec, expected_pps in codec_sets_with_pps.items():
        headers = 0
        calculator = VoIP_Calculator(headers, codec)

        assert (calculator.get_pps() == expected_pps)


