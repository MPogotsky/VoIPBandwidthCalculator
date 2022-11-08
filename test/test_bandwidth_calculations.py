import pytest
from src.VoIP_Calculator.VoIP_Calculator import VoIP_Calculator
from src.VoIP_Calculator.CodecTemplate import Codec
from src.VoIP_Calculator.HeaderTemplate import Header


def test_voip_calculator_bandwidth_calculations_for_RTP_protocol() -> None:
    """
    Test checks how VoIP_Calculator calculates packet
    rate for several codecs with "RTP" protocol
    and one some sample interval.
    """
    headers = Header(["RTP"])

    voip_with_bandwidth = {
        VoIP_Calculator(headers, Codec("G.711 64kbps", 64, sample_interval=20)):      68.8,
        VoIP_Calculator(headers, Codec("G.729 8kbps", 8, sample_interval=20)):        12.8,
        VoIP_Calculator(headers, Codec("G.729 8kbps", 8, sample_interval=1000)):      8.1,
        VoIP_Calculator(headers, Codec("G.723.1 5.3kbps", 5.3, sample_interval=30)):  8.5
    }

    for calculator, expected_bandwidth in voip_with_bandwidth.items():
        assert (calculator.get_bandwidth() == expected_bandwidth)


def test_voip_calculator_bandwidth_calculations_for_UDP_protocol() -> None:
    """
    Test checks how VoIP_Calculator calculates packet
    rate for several codecs with additional headers ("RTP+"UDP")
    and one some sample interval.
    """
    headers = Header(["RTP", "UDP"])

    voip_with_bandwidth = {
        VoIP_Calculator(headers, Codec("G.711 64kbps", 64, sample_interval=20)):      72,
        VoIP_Calculator(headers, Codec("G.729 8kbps", 8, sample_interval=20)):        16,
        VoIP_Calculator(headers, Codec("G.729 8kbps", 8, sample_interval=1000)):      8.2,
        VoIP_Calculator(headers, Codec("G.723.1 5.3kbps", 5.3, sample_interval=90)):  7.1
    }

    for calculator, expected_bandwidth in voip_with_bandwidth.items():
        assert (calculator.get_bandwidth() == expected_bandwidth)


def test_voip_calculator_bandwidth_calculations_for_sets_of_protocols() -> None:
    """
    Test checks how VoIP_Calculator calculates packet
    rate for several codecs, protocol set and frames.
    """

    voip_with_bandwidth = {
        VoIP_Calculator(Header(["RTP", "UDP", "IPv4", "ethernet 802.3"]),
                        Codec("G.711 64kbps", 64, frames=160)):              95.2,
        VoIP_Calculator(Header(["RTP", "UDP", "IPv6"]),
                        Codec("G.729 8kbps", 8, sample_interval=20)):        32,
        VoIP_Calculator(Header(["RTP", "UDP", "IPv4", "ethernet 802.3"]),
                        Codec("G.729 8kbps", 8, sample_interval=20)):        39.2,
        VoIP_Calculator(Header(["RTP", "UDP", "IPv4", "ethernet 802.3"]),
                        Codec("G.723.1 5.3kbps", 5.3, frames=3)):            12.2,
        VoIP_Calculator(Header(["RTP", "UDP", "IPv6", "ethernet 802.3"]),
                        Codec("G.723.1 5.3kbps", 5.3, frames=3)):            14.0,
    }

    for calculator, expected_bandwidth in voip_with_bandwidth.items():
        assert (calculator.get_bandwidth() == expected_bandwidth)
