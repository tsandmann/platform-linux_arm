# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os.path import join

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()

env.Append(
    CPPFLAGS=[
        "-mcpu=cortex-a53",
        "-mtune=cortex-a53",
        "-mfloat-abi=hard",
        "-mfpu=neon-fp-armv8",
        "-O2",
        "-Wformat=2",
        "-Wall",
        "-Wextra",
        "-Winline"
    ],

    LIBS=[
        "pthread"
    ]
)
