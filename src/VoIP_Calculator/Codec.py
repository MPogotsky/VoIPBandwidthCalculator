from .CodecSets import ITU_T_and_IETF_Defined_Codec_Interval_Standards


class Codec:
    def __init__(self, name: str, sample_interval: float = None, frames: int = None):
        """
        Class that specifies and calculates codec related parameters.
        :param name: codec name with bit rate
        :param sample_interval: codec sampling interval
        :param frames: number of frames in one packet
        """

        self.name = name
        self.bit_rate = self.__get_default_bitrate()
        if sample_interval is None and frames is None:
            raise Exception("Specify codecs sample interval or number of frames")

        if sample_interval is None:
            self.frame_number = frames
            self.frame_size = self.__calculate_codec_sample_interval()
        else:
            self.frame_size = sample_interval
            self.frame_number = self.__calculate_number_of_frames()

    def __get_default_bitrate(self) -> int:
        for codec_family, standard_data in ITU_T_and_IETF_Defined_Codec_Interval_Standards.items():
            if codec_family in self.name:
                return standard_data[0]

    def __calculate_number_of_frames(self) -> int:
        """
        Count number of frames needed
        :return: number of frames in voice payload
        """
        for codec_family, standard_data in ITU_T_and_IETF_Defined_Codec_Interval_Standards.items():
            if codec_family in self.name:
                return int(self.frame_size / standard_data[1])

    def __calculate_codec_sample_interval(self) -> float:
        """
        Count codec sample interval
        :return: codec sample interval in ms
        """
        for codec_family, standard_data in ITU_T_and_IETF_Defined_Codec_Interval_Standards.items():
            if codec_family in self.name:
                return float(self.frame_number * standard_data[1])
