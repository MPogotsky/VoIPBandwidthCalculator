import pytest
from src.VoIP_Calculator.HeaderTemplate import Header


def test_codec_frames_per_packet_calculations() -> None:
    """
    Test checks how Header calculates total size of given protocol
    """
    headers_with_out_in_bytes = {
        Header():                                         0,
        Header(["RTP"]):                                  12,
        Header(["RTP", "UDP"]):                           20,
        Header(["RTP", "UDP", "IPv4"]):                   40,
        Header(["RTP", "UDP", "IPv6"]):                   60,
        Header(["RTP", "UDP", "IPv4", "ethernet 802.3"]): 78,
        Header(["RTP", "UDP", "IPv6", "ethernet 802.3"]): 98
    }

    for header_with_protocol_set, expected_out in headers_with_out_in_bytes.items():
        total_size_bytes = header_with_protocol_set.total_size_bits / 8
        assert (total_size_bytes == expected_out)
