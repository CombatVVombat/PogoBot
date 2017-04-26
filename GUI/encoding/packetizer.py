
class Packetizer:
    def __init__(self, IGuiController):
        self.guiController = IGuiController

    def packetize(self, delimeter, frameLength, source):
        # Each 'packet' is a bytearray of length 'frameLength'
        packets = []
        packet = bytearray()
        for byte in source:
            if byte != delimeter:
                packet.append(byte)
            else:
                if len(packet) != frameLength:
                    packet = bytearray()
                else:
                    packets.append(packet)
                    packet = bytearray()
        return packets













def buildPacket(frameLength):
    #frameLength = number of data bytes in frame, not counting zero delimeter
    global rawByteStream
    packet = bytearray()
    if len(rawByteStream) > frameLength:    # need enough bytes to build a packet
        for i in rawByteStream:
            if(i == 0):
                break
            else:
                packet.append(i)
        if len(packet) != frameLength:      # started in the middle of a frame, discard
            del rawByteStream[0:len(packet)+1]
        else:
            del rawByteStream[0:len(packet)+1]
            return packet