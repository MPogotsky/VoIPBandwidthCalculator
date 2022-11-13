from .Codec import Codec
from .Header import Header


class VoIP_Calculator(object):
    def __init__(self, header: Header, codec: Codec, channels: int = 1):
        self.__header = header
        self.__codec = codec
        self.__number_of_channels = channels

        self.__voice_payload_size = self.__calculate_voice_payload_size()
        self.__packet_rate = self.__calculate_packet_rate()
        self.__bandwidth = self.__calculate_bandwidth()

    def __calculate_voice_payload_size(self) -> float:
        """
        Get voice payload size that represents the number of bytes
        that are captured by the Digital Signal Processor
        :return: voice payload size in bits
        """
        voice_payload_size = (self.__codec.bit_rate * 1000) * (self.__codec.sample_interval * 10 ** -3)
        return round(voice_payload_size, 1)

    def __calculate_packet_rate(self) -> float:
        """
        Packet rate represents the number of packets that need to be
        transmitted every second in order to deliver the codec bit rate.
        :return: packet rate in pps
        """
        bit_rate_bps = self.__codec.bit_rate * 1000
        packet_rate = bit_rate_bps / self.__voice_payload_size
        packet_rate = packet_rate * self.__number_of_channels
        return round(packet_rate, 1)

    def __calculate_total_packet_size(self) -> float:
        """
        Count total packet size that consists of bytes of
        protocol header together with voice payload.
        :return: packet size in bits
        """
        return self.__header.total_size_bits + self.__voice_payload_size

    def __calculate_bandwidth(self) -> float:
        """
        Calculate VoIP bandwidth.
        :return: bandwidth in kbps
        """
        total_packet_size = self.__calculate_total_packet_size()
        bandwidth = (total_packet_size * self.__packet_rate) / 1000

        return round(bandwidth, 1)

    def get_voice_payload_size(self) -> float:
        """
        :return: voice payload size in bits as float
        """
        return self.__voice_payload_size

    def get_bandwidth(self) -> float:
        """
        :return: bandwidth in kbps as float
        """
        return self.__bandwidth

    def get_bandwidth_as_string(self) -> str:
        """
        :return: bandwidth in kbps as str
        """
        return str(self.__bandwidth) + "kbps"

    def get_pps(self) -> float:
        """
        :return: packet rate in pps as float
        """
        return self.__packet_rate

    def get_pps_as_string(self):
        """
        :return: packet rate in pps as string
        """
        return str(self.__packet_rate) + "pps"
