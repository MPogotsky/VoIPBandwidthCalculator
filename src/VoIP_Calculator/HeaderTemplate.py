from .HeaderSets import ProtocolHeaderSizesInBytes as ProtoHeader


class Header:
    def __init__(self, protocols: list = None):
        self.protocols = protocols
        if protocols is None:
            self.total_size_bits = 0
        else:
            self.total_size_bits = self.__calculate_header_size()

    def __calculate_header_size(self) -> int:
        total_size: int = 0

        for protocol in self.protocols:
            total_size += ProtoHeader.get(protocol)

        return total_size * 8  # return total header size in bits, as we use bits later in calculations
