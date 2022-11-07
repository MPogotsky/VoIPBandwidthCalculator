import pytest
from src.VoIP_Calculator.VoIP_Calculator import VoIP_Calculator
from src.VoIP_Calculator.CodecTemplate import Codec
from src.VoIP_Calculator.HeaderSets import ProtocolHeaderSizesInBytes


def test_voip_calculator_bandwidth_calculations() -> None:
    """
    Test checks how VoIP_Calculator calculates packet
    rate for several codecs with no additional headers
    and one some sample interval.
    """
    headers = ProtocolHeaderSizesInBytes.get("RTP")

    voip_with_bandwidth = {
        VoIP_Calculator(headers, Codec("G.711 64kbps", 64, sample_interval=20)):      68.8,
        VoIP_Calculator(headers, Codec("G.729 8kbps", 8, sample_interval=20)):        12.8,
        VoIP_Calculator(headers, Codec("G.729 8kbps", 8, sample_interval=1000)):      8.1,
        VoIP_Calculator(headers, Codec("G.723.1 5.3kbps", 5.3, sample_interval=30)):  8.5
    }

    for calculator, expected_bandwidth in voip_with_bandwidth.items():
        assert (calculator.get_bandwidth() == expected_bandwidth)
