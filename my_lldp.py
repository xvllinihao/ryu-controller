from scapy.contrib import lldp

class LLDPTopology(lldp.LLDPDU):
    def __init__(self):
        super(LLDPTopology, self).__init__()
