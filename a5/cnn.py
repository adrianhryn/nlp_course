#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CS224N 2018-19: Homework 5
"""

### YOUR CODE HERE for part 1i

import torch
import torch.nn as nn
import torch.nn.functional as F


class CNN(nn.Module):

    def __init__(self, embed_size: int = 50, m_word: int = 21,k: int = 5, f: int = None):
        super(CNN, self).__init__()

        self.conv = nn.Conv1d(in_channels=embed_size, out_channels=f, kernel_size=k)
        self.max_pool = nn.MaxPool1d(m_word-k+1)

    def forward(self, x_reshaped):
        x_conv = self.conv(x_reshaped)
        x_conv_out = self.max_pool(F.relu(x_conv))

        return torch.squeeze(x_conv_out, -1)

### END YOUR CODE

