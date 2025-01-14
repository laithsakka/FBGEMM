# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

from fbgemm_gpu.experimental.gen_ai.utils.loader import load_custom_library

# Load all custom gemm operators.
load_custom_library("//deeplearning/fbgemm/fbgemm_gpu/experimental/gen_ai:gemm_ops")
