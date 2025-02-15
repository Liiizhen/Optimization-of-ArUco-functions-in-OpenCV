import numpy as np
import cv2
from random import random, randint

MIP36h12 = [0xd2b63a09d, 0x6001134e5, 0x1206fbe72, 0xff8ad6cb4, 0x85da9bc49, 0xb461afe9c,
            0x6db51fe13, 0x5248c541f, 0x8f34503, 0x8ea462ece, 0xeac2be76d, 0x1af615c44,
            0xb48a49f27, 0x2e4e1283b, 0x78b1f2fa8, 0x27d34f57e, 0x89222fff1, 0x4c1669406,
            0xbf49b3511, 0xdc191cd5d, 0x11d7c3f85, 0x16a130e35, 0xe29f27eff, 0x428d8ae0c,
            0x90d548477, 0x2319cbc93, 0xc3b0c3dfc, 0x424bccc9, 0x2a081d630, 0x762743d96,
            0xd0645bf19, 0xf38d7fd60, 0xc6cbf9a10, 0x3c1be7c65, 0x276f75e63, 0x4490a3f63,
            0xda60acd52, 0x3cc68df59, 0xab46f9dae, 0x88d533d78, 0xb6d62ec21, 0xb3c02b646,
            0x22e56d408, 0xac5f5770a, 0xaaa993f66, 0x4caa07c8d, 0x5c9b4f7b0, 0xaa9ef0e05,
            0x705c5750, 0xac81f545e, 0x735b91e74, 0x8cc35cee4, 0xe44694d04, 0xb5e121de0,
            0x261017d0f, 0xf1d439eb5, 0xa1a33ac96, 0x174c62c02, 0x1ee27f716, 0x8b1c5ece9,
            0x6a05b0c6a, 0xd0568dfc, 0x192d25e5f, 0x1adbeccc8, 0xcfec87f00, 0xd0b9dde7a,
            0x88dcef81e, 0x445681cb9, 0xdbb2ffc83, 0xa48d96df1, 0xb72cc2e7d, 0xc295b53f,
            0xf49832704, 0x9968edc29, 0x9e4e1af85, 0x8683e2d1b, 0x810b45c04, 0x6ac44bfe2,
            0x645346615, 0x3990bd598, 0x1c9ed0f6a, 0xc26729d65, 0x83993f795, 0x3ac05ac5d,
            0x357adff3b, 0xd5c05565, 0x2f547ef44, 0x86c115041, 0x640fd9e5f, 0xce08bbcf7,
            0x109bb343e, 0xc21435c92, 0x35b4dfce4, 0x459752cf2, 0xec915b82c, 0x51881eed0,
            0x2dda7dc97, 0x2e0142144, 0x42e890f99, 0x9a8856527, 0x8e80d9d80, 0x891cbcf34,
            0x25dd82410, 0x239551d34, 0x8fe8f0c70, 0x94106a970, 0x82609b40c, 0xfc9caf36,
            0x688181d11, 0x718613c08, 0xf1ab7629, 0xa357bfc18, 0x4c03b7a46, 0x204dedce6,
            0xad6300d37, 0x84cc4cd09, 0x42160e5c4, 0x87d2adfa8, 0x7850e7749, 0x4e750fc7c,
            0xbf2e5dfda, 0xd88324da5, 0x234b52f80, 0x378204514, 0xabdf2ad53, 0x365e78ef9,
            0x49caa6ca2, 0x3c39ddf3, 0xc68c5385d, 0x5bfcbbf67, 0x623241e21, 0xabc90d5cc,
            0x388c6fe85, 0xda0e2d62d, 0x10855dfe9, 0x4d46efd6b, 0x76ea12d61, 0x9db377d3d,
            0xeed0efa71, 0xe6ec3ae2f, 0x441faee83, 0xba19c8ff5, 0x313035eab, 0x6ce8f7625,
            0x880dab58d, 0x8d3409e0d, 0x2be92ee21, 0xd60302c6c, 0x469ffc724, 0x87eebeed3,
            0x42587ef7a, 0x7a8cc4e52, 0x76a437650, 0x999e41ef4, 0x7d0969e42, 0xc02baf46b,
            0x9259f3e47, 0x2116a1dc0, 0x9f2de4d84, 0xeffac29, 0x7b371ff8c, 0x668339da9,
            0xd010aee3f, 0x1cd00b4c0, 0x95070fc3b, 0xf84c9a770, 0x38f863d76, 0x3646ff045,
            0xce1b96412, 0x7a5d45da8, 0x14e00ef6c, 0x5e95abfd8, 0xb2e9cb729, 0x36c47dd7,
            0xb8ee97c6b, 0xe9e8f657, 0xd4ad2ef1a, 0x8811c7f32, 0x47bde7c31, 0x3adadfb64,
            0x6e5b28574, 0x33e67cd91, 0x2ab9fdd2d, 0x8afa67f2b, 0xe6a28fc5e, 0x72049cdbd,
            0xae65dac12, 0x1251a4526, 0x1089ab841, 0xe2f096ee0, 0xb0caee573, 0xfd6677e86,
            0x444b3f518, 0xbe8b3a56a, 0x680a75cfc, 0xac02baea8, 0x97d815e1c, 0x1d4386e08,
            0x1a14f5b0e, 0xe658a8d81, 0xa3868efa7, 0x3668a9673, 0xe8fc53d85, 0x2e2b7edd5,
            0x8b2470f13, 0xf69795f32, 0x4589ffc8e, 0x2e2080c9c, 0x64265f7d, 0x3d714dd10,
            0x1692c6ef1, 0x3e67f2f49, 0x5041dad63, 0x1a1503415, 0x64c18c742, 0xa72eec35,
            0x1f0f9dc60, 0xa9559bc67, 0xf32911d0d, 0x21c0d4ffc, 0xe01cef5b0, 0x4e23a3520,
            0xaa4f04e49, 0xe1c4fcc43, 0x208e8f6e8, 0x8486774a5, 0x9e98c7558, 0x2c59fb7dc,
            0x9446a4613, 0x8292dcc2e, 0x4d61631, 0xd05527809, 0xa0163852d, 0x8f657f639,
            0xcca6c3e37, 0xcb136bc7a, 0xfc5a83e53, 0x9aa44fc30, 0xbdec1bd3c, 0xe020b9f7c,
            0x4b8f35fb0, 0xb8165f637, 0x33dc88d69, 0x10a2f7e4d, 0xc8cb5ff53, 0xde259ff6b,
            0x46d070dd4, 0x32d3b9741, 0x7075f1c04, 0x4d58dbea0, 0x000000000, 0xfffffffff]

def id_to_bits(id):
    return [float(bit) for bit in format(MIP36h12[id], '036b')]

def get_marker(id, size = 512, border_width = 1.0):

    marker = np.zeros((8, 8, 4), dtype=np.uint8)
    marker[0:8,0:8] = (0, 0, 0, 255.0)
    marker[1:7,1:7] = cv2.cvtColor(np.reshape(np.asarray([(i * 255.0) for i in id_to_bits(id)])
                                                .astype(np.uint8), (6, 6)), cv2.COLOR_GRAY2BGRA)
    
    canvas = np.ones((size, size, 4), dtype = np.uint8) * 255.0
    canvas[:,:,3] = 0

    center = size//2
    bg_size = int(size - 2 * (size / 10) * (1 - border_width))
    canvas[center - bg_size//2:center + bg_size//2, 
           center - bg_size//2:center + bg_size//2, 3] = 255.0
    
    wo_border = int(size - 2 * (size / 10))
    canvas[(size - wo_border) // 2:(size + wo_border) // 2,
        (size - wo_border) // 2:(size + wo_border) // 2] = \
            cv2.resize(marker, (wo_border, wo_border), interpolation=cv2.INTER_NEAREST)

    corners = [[(size - wo_border) // 2, (size - wo_border) // 2],
               [(size - wo_border) // 2, (size + wo_border) // 2 - 1],
               [(size + wo_border) // 2 - 1, (size + wo_border) // 2 - 1],
               [(size + wo_border) // 2 - 1, (size - wo_border) // 2]]

    return canvas, corners

ids_as_bits = [id_to_bits(i) for i in range(250)]
def find_id(bits):

    rot0 = bits.flatten()
    rot90 = np.rot90(bits, 1).flatten()
    rot180 = np.rot90(bits, 2).flatten()
    rot270 = np.rot90(bits, 3).flatten()

    distances = [int(np.min([np.sum(np.abs(rot0 - check_bits)),
                np.sum(np.abs(rot90 - check_bits)),
                np.sum(np.abs(rot180 - check_bits)),
                np.sum(np.abs(rot270 - check_bits))])) 
                for check_bits in ids_as_bits]
    
    id = int(np.argmin(distances))

    return (id, distances[id])

if __name__ == '__main__':
    marker, corners = get_marker(randint(0, 250), border_width = random())
    for c in corners:
        cv2.circle(marker, (c[0], c[1]), 5, (0, 255, 0, 255), -1, lineType=cv2.LINE_AA)
    cv2.imwrite('test_aruco.png', marker)