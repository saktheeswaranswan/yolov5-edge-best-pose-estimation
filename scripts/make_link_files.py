#!/usr/bin/env python

# Copyright (c) 2018-2021, Texas Instruments
# All Rights Reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import glob
import re
import argparse


def make_links(files, source_pattern, dest_pattern):
    for file_name in files:
        file_ext = os.path.splitext(file_name)[1]
        if file_ext in supported_ext:
            dest_filename = re.sub(source_pattern, dest_pattern, file_name)
            #print(file_name, new_filename)
            link_name = file_name + '.link'
            print(link_name)
            with open(link_name, 'w') as fp:
                fp.write(dest_filename)
            #


if __name__ == '__main__':
    # the cwd must be the root of the repository
    if os.path.split(os.getcwd())[-1] == 'scripts':
        os.chdir('../')
    #

    parser = argparse.ArgumentParser()
    parser.add_argument('version', type=str)
    cmds = parser.parse_args()

    supported_ext = ['.tf', '.tflite', '.pth', '.pt', '.ptl', '.onnx', '.json', '.params', '.prototxt', '.caffemodel']

    files = glob.glob('pretrained_models/models/*/*/*/*')
    source_pattern = '^pretrained_models/models/'
    dest_pattern = f'http://software-dl.ti.com/jacinto7/esd/modelzoo/gplv3/{cmds.version}/edgeai-yolov5/pretrained_models/models/'
    make_links(files, source_pattern, dest_pattern)

    files = glob.glob('pretrained_models/checkpoints/*/*/*/*/*/*')
    source_pattern = '^pretrained_models/checkpoints/'
    dest_pattern = f'http://software-dl.ti.com/jacinto7/esd/modelzoo/gplv3/{cmds.version}/edgeai-yolov5/pretrained_models/checkpoints/'
    make_links(files, source_pattern, dest_pattern)
