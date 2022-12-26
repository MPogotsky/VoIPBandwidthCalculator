import pytest
from src.VoIP_Calculator.VoIP_Calculator import VoIP_Calculator
from src.VoIP_Calculator.Codec import Codec
from src.VoIP_Calculator.Header import Header


def test_voip_calculator_bandwidth_calculations_for_RTP_protocol() -> None:
    """
    Test checks how VoIP_Calculator calculates bandwidth
    for several codecs with "RTP" protocol
    and one some sample interval.
    """
    voip_calculator = VoIP_Calculator()
    headers = Header(["RTP"])

    set_of_parameters = {
        (headers, Codec("G.711 64kbps", voice_payload_size=20)): 68.8,
        (headers, Codec("G.729 8kbps", voice_payload_size=20)): 12.8,
        (headers, Codec("G.729 8kbps", voice_payload_size=1000)): 8.1,
        (headers, Codec("G.723.1 5.3kbps", voice_payload_size=30)): 8.5
    }

    for parameter, expected_bandwidth in set_of_parameters.items():
        voip_calculator.calculate(parameter[0], parameter[1])
        assert (voip_calculator.get_bandwidth() == expected_bandwidth)


def test_voip_calculator_bandwidth_calculations_for_UDP_protocol() -> None:
    """
    Test checks how VoIP_Calculator calculates bandwidth
    for several codecs with additional headers ("RTP+"UDP")
    and one some sample interval.
    """
    voip_calculator = VoIP_Calculator()
    headers = Header(["RTP", "UDP"])

    set_of_parameters = {
        (headers, Codec("G.711 64kbps", voice_payload_size=20)): 72,
        (headers, Codec("G.729 8kbps", voice_payload_size=20)): 16,
        (headers, Codec("G.729 8kbps", voice_payload_size=1000)): 8.2,
        (headers, Codec("G.723.1 5.3kbps", voice_payload_size=90)): 7.1,
        (headers, Codec("G.728 12.8kbps", voice_payload_size=90)): 14.6
    }

    for parameter, expected_bandwidth in set_of_parameters.items():
        voip_calculator.calculate(parameter[0], parameter[1])
        assert (voip_calculator.get_bandwidth() == expected_bandwidth)


def test_voip_calculator_for_sets_of_protocols() -> None:
    """
    Test checks how VoIP_Calculator calculates bandwidth and packet
    rate for several codecs, protocol set and frames.
    """

    voip_calculator = VoIP_Calculator()

    set_of_parameters = {
        (Header(["RTP", "UDP", "IPv4", "ethernet 802.3"]),
         Codec("G.711 64kbps", frames=2), 1):               (95.2, 50),
        (Header(["RTP", "UDP", "IPv6"]),
         Codec("G.729 8kbps", voice_payload_size=20), 2):   (64, 100),
        (Header(["RTP", "UDP", "IPv4", "ethernet 802.3"]),
         Codec("G.729 8kbps", voice_payload_size=20), 1):   (39.2, 50),
        (Header(["RTP", "UDP", "IPv4", "ethernet 802.3"]),
         Codec("G.723.1 5.3kbps", frames=3), 1):            (12.2, 11.1),
        (Header(["RTP", "UDP", "IPv6", "ethernet 802.3"]),
         Codec("G.723.1 5.3kbps", frames=3), 3):            (42, 33.3)
    }

    for parameter, expected_out in set_of_parameters.items():
        voip_calculator.calculate(parameter[0], parameter[1], parameter[2])
        assert (voip_calculator.get_bandwidth() == expected_out[0])
        assert (voip_calculator.get_pps() == expected_out[1])
