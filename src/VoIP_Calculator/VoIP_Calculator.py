from .Codec import Codec
from .Header import Header


class VoIP_Calculator(object):
    def __init__(self):
        self.__header = None
        self.__codec = None
        self.__number_of_channels = None

        self.__packet_rate = None
        self.__bandwidth = None

    def calculate(self, header: Header, codec: Codec, channels: int = 1):
        self.__header = header
        self.__codec = codec
        self.__number_of_channels = channels

        self.__packet_rate = self.__calculate_packet_rate()
        self.__bandwidth = self.__calculate_bandwidth()

    def __calculate_packet_rate(self) -> float:
        """
        Packet rate represents the number of packets that need to be
        transmitted every second in order to deliver the codec bit rate.
        :return: packet rate in pps
        """
        packet_rate = 1 / (self.__codec.voice_payload_size * 10 ** -3)
        packet_rate = packet_rate * self.__number_of_channels
        return round(packet_rate, 1)

    def __calculate_total_packet_size(self) -> float:
        """
        Count total packet size that consists of bytes of
        protocol header together with voice payload.
        :return: packet size in bits
        """
        return self.__header.total_size_bits + self.__codec.voice_payload_size

    def __calculate_bandwidth(self) -> float:
        """
        Calculate bandwidth.
        :return: bandwidth in kbps
        """
        bit_rate = self.__codec.bit_rate
        voice_payload_in_ms = self.__codec.voice_payload_size
        voice_payload_bits = bit_rate * voice_payload_in_ms  # kbps * ms = bits
        total_packet_size = self.__header.total_size_bits + voice_payload_bits
        bandwidth = (total_packet_size * self.__packet_rate)
        bandwidth = bandwidth / 1000  # in kbps
        return round(bandwidth, 1)

    def get_bandwidth(self) -> float:
        """
        :return: bandwidth in kbps as float
        """
        return self.__bandwidth

    def get_pps(self) -> float:
        """
        :return: packet rate in pps as float
        """
        return self.__packet_rate
