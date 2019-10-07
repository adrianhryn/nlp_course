#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CS224N 2018-19: Homework 5
"""

### YOUR CODE HERE for part 1h

import torch
import torch.nn as nn
import torch.nn.functional as F


class Highway(nn.Module):

    def __init__(self, embedsize):
        super(Highway, self).__init__()

        self.weigths_projection = nn.Linear(embedsize, embedsize)
        self.weigts_gate = nn.Linear(embedsize, embedsize)

    def forward(self, x_conv_out):
        x_proj = F.relu(self.weigths_projection(x_conv_out))
        x_gate = torch.sigmoid(self.weigts_gate(x_conv_out))

        x_highway = torch.mul(x_gate, x_proj) + torch.mul(x_conv_out, 1-x_gate)
        return x_highway

### END YOUR CODE 

