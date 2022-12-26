from .CodecSets import ITU_T_and_IETF_Defined_Codec_Interval_Standards


class Codec:
    def __init__(self, name: str, voice_payload_size: int = None, frames: int = None):
        """
        Class that specifies and calculates codec related parameters.
        :param name: codec name with bit rate
        :param voice payload size: length of voice chunk
        :param frames: number of frames in one packet
        """

        self.name = name
        self.bit_rate = self.__get_default_bitrate()
        if voice_payload_size is None and frames is None:
            raise Exception("Specify voice payload size or number of frames")

        if voice_payload_size is None:
            self.frame_number = frames
            self.voice_payload_size = self.__calculate_voice_payload_size()
        else:
            self.voice_payload_size = voice_payload_size
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
                return int(self.voice_payload_size / standard_data[1])

    def __calculate_voice_payload_size(self) -> int:
        """
        Get voice payload size that represents the number of voice that
        going to be transmitted via network in one packet
        :return: voice payload size in bits
        """
        for codec, data in ITU_T_and_IETF_Defined_Codec_Interval_Standards.items():
            if codec in self.name:
                return int(self.frame_number * data[1])  # data[1] is codec standard frame size