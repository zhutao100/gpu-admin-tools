#
# SPDX-FileCopyrightText: Copyright (c) 2018-2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: MIT
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#

import array
from collections.abc import ByteString
import sys


def ints_from_data(data, size):
    return [
        int.from_bytes(data[i: i + size], byteorder=sys.byteorder)
        for i in range(0, len(data), size)
    ]


def int_from_data(data, size):
    del size  # unused
    return int.from_bytes(data, byteorder=sys.byteorder)


def data_from_int(integer, size=4):
    return integer.to_bytes(size, byteorder=sys.byteorder)


def bytearray_view_from_int_array(int_array: list[int], type_code: str = "I") -> ByteString:
    a = array.array(type_code)
    a.fromlist(int_array)
    return memoryview(a.tobytes()).toreadonly()


def array_view_from_bytearray(ba, type_code: str = 'I') -> ByteString:
    a = array.array(type_code)
    a.frombytes(ba)
    return memoryview(a).toreadonly()


def read_ints_from_path(path, offset, int_size, int_num=-1):
    with open(path, 'rb') as f:
        f.seek(offset, 0)
        if int_num == -1:
            size = -1
        else:
            size = int_size * int_num

        return ints_from_data(f.read(size), int_size)
