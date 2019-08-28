#!/usr/bin/env python3

#
#   This file is part of m.css.
#
#   Copyright © 2017, 2018, 2019 Vladimír Vondruš <mosra@centrum.cz>
#
#   Permission is hereby granted, free of charge, to any person obtaining a
#   copy of this software and associated documentation files (the "Software"),
#   to deal in the Software without restriction, including without limitation
#   the rights to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell copies of the Software, and to permit persons to whom the
#   Software is furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included
#   in all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#   THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#

import os

from _search import searchdata_filename, pretty_print
from python import EntryType

from test_python import BaseInspectTestCase

class Search(BaseInspectTestCase):
    def test(self):
        self.run_python({
            'SEARCH_DISABLED': False,
            'SEARCH_DOWNLOAD_BINARY': True,
            'PYBIND11_COMPATIBILITY': True
        })

        with open(os.path.join(self.path, 'output', searchdata_filename), 'rb') as f:
            serialized = f.read()
            search_data_pretty = pretty_print(serialized, entryTypeClass=EntryType)[0]
        #print(search_data_pretty)
        self.assertEqual(len(serialized), 1910)
        self.assertEqual(search_data_pretty, """
18 symbols
search [11]
||    .$
||     foo [6]
||     || .$
||     ||  enum [0]
||     ||  |   .$
||     ||  |    a_value [1]
||     ||  |     nother [2]
||     ||  a_method [3]
||     ||  | |     ($
||     ||  | |      ) [4]
||     ||  | property [5]
||     |unc_with_params [9]
||     ||              ($
||     ||               ) [10]
||     a_function [7]
||     |         ($
||     |          ) [8]
||     pybind [23]
||     |     .$
||     |      foo [18]
||     |       | .$
||     |       |  overloaded_method [14, 16, 12]
||     |       |                   ($
||     |       |                    ) [15, 17, 13]
||     |       unction [19]
||     |       |      ($
||     |       |       ) [20]
||     |       |      _with_params [21]
||     |       |      |           ($
||     |       |      |            ) [22]
||     sub [25]
||     |  .$
||     |   data_in_a_submodule [24]
|ub [25]
|| .$
||  data_in_a_submodule [24]
foo [6, 18]
|| .$
||  enum [0]
||  |   .$
||  |    a_value [1]
||  |     nother [2]
||  a_method [3]
||  | |     ($
||  | |      ) [4]
||  | property [5]
||  overloaded_method [14, 16, 12]
||  |                ($
||  |                 ) [15, 17, 13]
|unc_with_params [9]
||  |           ($
||  |            ) [10]
||  tion [19]
||  |   ($
||  |    ) [20]
||  |   _with_params [21]
||  |   |           ($
||  |   |            ) [22]
enum [0]
|   .$
|    a_value [1]
|     nother [2]
a_value [1]
||method [3]
|||     ($
|||      ) [4]
||property [5]
||function [7]
|||       ($
|||        ) [8]
|nother [2]
pybind [23]
|     .$
|      foo [18]
|       | .$
|       |  overloaded_method [14, 16, 12]
|       |                   ($
|       |                    ) [15, 17, 13]
|       unction [19]
|       |      ($
|       |       ) [20]
|       |      _with_params [21]
|       |      |           ($
|       |      |            ) [22]
overloaded_method [14, 16, 12]
|                ($
|                 ) [15, 17, 13]
data_in_a_submodule [24]
0: .Enum [prefix=6[:15], type=ENUM] -> #Enum
1: .A_VALUE [prefix=0[:20], type=ENUM_VALUE] -> -A_VALUE
2: .ANOTHER [prefix=0[:20], type=ENUM_VALUE] -> -ANOTHER
3: .a_method() [prefix=6[:15], suffix_length=2, type=FUNCTION] -> #a_method
4:  [prefix=3[:24], type=FUNCTION] ->
5: .a_property [prefix=6[:15], type=PROPERTY] -> #a_property
6: .Foo [prefix=11[:7], type=CLASS] -> Foo.html
7: .a_function() [prefix=11[:11], suffix_length=2, type=FUNCTION] -> #a_function
8:  [prefix=7[:22], type=FUNCTION] ->
9: .func_with_params() [prefix=11[:11], suffix_length=2, type=FUNCTION] -> #func_with_params
10:  [prefix=9[:28], type=FUNCTION] ->
11: search [type=MODULE] -> search.html
12: .overloaded_method(self, first: int, second: float) [prefix=18[:22], suffix_length=33, type=FUNCTION] -> #overloaded_method-27269
13:  [prefix=12[:46], suffix_length=31, type=FUNCTION] ->
14: .overloaded_method(self, arg0: int) [prefix=18[:22], suffix_length=17, type=FUNCTION] -> #overloaded_method-745a3
15:  [prefix=14[:46], suffix_length=15, type=FUNCTION] ->
16: .overloaded_method(self, arg0: int, arg1: Foo) [prefix=18[:22], suffix_length=28, type=FUNCTION] -> #overloaded_method-41cfb
17:  [prefix=16[:46], suffix_length=26, type=FUNCTION] ->
18: .Foo [prefix=23[:14], type=CLASS] -> Foo.html
19: .function() [prefix=23[:18], suffix_length=2, type=FUNCTION] -> #function-da39a
20:  [prefix=19[:33], type=FUNCTION] ->
21: .function_with_params() [prefix=23[:18], suffix_length=2, type=FUNCTION] -> #function_with_params-8f19c
22:  [prefix=21[:45], type=FUNCTION] ->
23: .pybind [prefix=11[:7], type=MODULE] -> pybind.html
24: .DATA_IN_A_SUBMODULE [prefix=25[:15], type=DATA] -> #DATA_IN_A_SUBMODULE
25: .sub [prefix=11[:7], type=MODULE] -> sub.html
(EntryType.PAGE, CssClass.SUCCESS, 'page'),
(EntryType.MODULE, CssClass.PRIMARY, 'module'),
(EntryType.CLASS, CssClass.PRIMARY, 'class'),
(EntryType.FUNCTION, CssClass.INFO, 'func'),
(EntryType.PROPERTY, CssClass.WARNING, 'property'),
(EntryType.ENUM, CssClass.PRIMARY, 'enum'),
(EntryType.ENUM_VALUE, CssClass.DEFAULT, 'enum val'),
(EntryType.DATA, CssClass.DEFAULT, 'data')
""".strip())

class LongSuffixLength(BaseInspectTestCase):
    def test(self):
        self.run_python({
            'SEARCH_DISABLED': False,
            'SEARCH_DOWNLOAD_BINARY': True,
            'PYBIND11_COMPATIBILITY': True
        })

        with open(os.path.join(self.path, 'output', searchdata_filename), 'rb') as f:
            serialized = f.read()
            search_data_pretty = pretty_print(serialized, entryTypeClass=EntryType)[0]
        #print(search_data_pretty)
        self.assertEqual(len(serialized), 633)
        # The parameters get cut off with an ellipsis
        self.assertEqual(search_data_pretty, """
3 symbols
search_long_suffix_length [4]
|                        .$
|                         many_parameters [0, 2]
|                                        ($
|                                         ) [1, 3]
many_parameters [0, 2]
|              ($
|               ) [1, 3]
0: .many_parameters(arg0: typing.Tuple[float, int, str, typing.List[…) [prefix=4[:30], suffix_length=53, type=FUNCTION] -> #many_parameters-06151
1:  [prefix=0[:52], suffix_length=51, type=FUNCTION] ->
2: .many_parameters(arg0: typing.Tuple[int, float, str, typing.List[…) [prefix=4[:30], suffix_length=53, type=FUNCTION] -> #many_parameters-31300
3:  [prefix=2[:52], suffix_length=51, type=FUNCTION] ->
4: search_long_suffix_length [type=MODULE] -> search_long_suffix_length.html
(EntryType.PAGE, CssClass.SUCCESS, 'page'),
(EntryType.MODULE, CssClass.PRIMARY, 'module'),
(EntryType.CLASS, CssClass.PRIMARY, 'class'),
(EntryType.FUNCTION, CssClass.INFO, 'func'),
(EntryType.PROPERTY, CssClass.WARNING, 'property'),
(EntryType.ENUM, CssClass.PRIMARY, 'enum'),
(EntryType.ENUM_VALUE, CssClass.DEFAULT, 'enum val'),
(EntryType.DATA, CssClass.DEFAULT, 'data')
""".strip())