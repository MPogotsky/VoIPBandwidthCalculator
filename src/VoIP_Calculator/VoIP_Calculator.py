from .CodecTemplate import Codec
from .CodecSets import CodecSets


class VoIP_Calculator(object):
    def __init__(self, headers: int, codec: Codec, N: int):
        self.headers = headers
        self.codec_bit_rate = codec.bit_rate
        self.codec_sample_size = codec.sample_size
        self.codec_sample_interval = codec.sample_interval
        self.n = N

        self._packet_rate = self._calculate_packet_rate()
        self._bandwidth = self._calculate_bandwidth()

    def _voice_payload_size(self) -> float:
        """
        ( codec_sample_interval[ms] * codec_bit_rate[kbps] ) / 8bit = x Bytes

        :return: VPS in Bytes
        """
        return (self.n * self.codec_sample_interval * self.codec_bit_rate) / 8

    def _total_packet_size(self) -> float:
        return self.headers + self._voice_payload_size()

    def _calculate_packet_rate(self) -> float:
        packet_rate = (self.codec_bit_rate * 1000) / (self._voice_payload_size() * 8)
        return round(packet_rate, 1)

    def _calculate_bandwidth(self) -> float:
        bandwidth = (self._total_packet_size() * self._packet_rate * 8) / 1000
        return round(bandwidth, 1)

    def get_bandwidth(self) -> str:
        return str(self._bandwidth) + "kbps"

    def get_pps(self) -> str:
        return str(self._packet_rate) + "pps"


def calculate():
    headers = 0
    calculator = VoIP_Calculator(headers, CodecSets["G.723.1 5.3kbps"], 5)
    print("PPS Average: ", calculator.get_pps())
    print("Bandwidth Average: ", calculator.get_bandwidth())
