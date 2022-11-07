from .CodecSets import ITU_T_and_IETF_Defined_Codec_Interval_Standards


class Codec:
    def __init__(self, name: str, bit_rate: float, sample_interval: float = None, frames: int = None):
        """
        Class that specifies and calculates codec related parameters.
        :param name: codec name with bit rate
        :param bit_rate: codec bit rate
        :param sample_interval: codec sampling interval
        :param frames: number of frames in one packet
        """
        self.name = name
        self.bit_rate = bit_rate

        if sample_interval is None and frames is None:
            raise Exception("Specify codecs sample interval or number of frames")

        if sample_interval is None:
            self.frame_number = frames
            self.sample_interval = self.__calculate_codec_sample_interval()
        else:
            self.sample_interval = sample_interval
            self.frame_number = self.__calculate_number_of_frames()

    def __calculate_number_of_frames(self) -> int:
        """
        Count number of frames needed
        :return: number of frames in voice payload
        """
        for codec_family, standard_interval in ITU_T_and_IETF_Defined_Codec_Interval_Standards.items():
            if codec_family in self.name:
                return int(self.sample_interval / standard_interval)

    def __calculate_codec_sample_interval(self) -> float:
        """
        Count codec sample interval
        :return: codec sample interval in ms
        """
        for codec_family, standard_interval in ITU_T_and_IETF_Defined_Codec_Interval_Standards.items():
            if codec_family in self.name:
                return float(self.frame_number * standard_interval)
