import sys
from pprint import pprint

hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

packet_decode = {
    "001": 1,
    "010": 2,
    "011": 3,
    "100": 4,
    "101": 5,
    "110": 6,
    "111": 7
}


# Function calculates the decimal equivalent
# to given binary number
# Credit: https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/
def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def get_next_packet(id, bitstream, it):
    data_str = ""
    if id == 4:
        while it < len(bitstream):
            section = bitstream[it:it+5]
            it += 5
            last_group = (section[0] == '0')
            data_str += section[1:5]

            if not last_group:
                continue
            else:
                binaryToDecimal(int(data_str))
                data_str = ""
                while it < len(bitstream) and bitstream[it] == '0':
                    it += 1
            it += 1
        return data_str
    else:
        pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Need input file.")

    f = open(sys.argv[1])
    data = f.read().rstrip()

    bitstream = ""

    for i in data:
        bitstream += hex_to_bin[i]

    #print(bitstream)
    
    # How many packets deep the current bitstream is
    # If an operator packet has subsequent packets, increase depth by one
    packet_depth = 0

    it = 0
    packet_data = {}

    packet_data["ver"] = packet_decode[bitstream[it:it+3]]
    it += 3
    packet_data["type_id"] = packet_decode[bitstream[it:it+3]]
    it += 3

    data_str = ""

    if packet_data["type_id"] == 4:
        while it < len(bitstream):
            section = bitstream[it:it+5]
            it += 5
            last_group = (section[0] == '0')
            data_str += section[1:5]

            if not last_group:
                continue
            else:
                packet_data["data"] = binaryToDecimal(int(data_str))
                data_str = ""
                while it < len(bitstream) and bitstream[it] == '0':
                    it += 1
            it += 1
    else:
        while it < len(bitstream):
            next_packet_len = (11 if bitstream[it] == '1' else 15)
            it += 1
            # Next 11 bits are the number of packets contained by this packet
            if next_packet_len == 11:
                pass
            # Next 15 bits are the number of bits in subsequent packets
            else:




    pprint(packet_data, indent=4, width=60)