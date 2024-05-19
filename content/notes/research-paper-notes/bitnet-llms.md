---
title: "BitNet: Scaling 1-bit Transformers for LLMs"
date: 2024-03-16T11:54:58+08:00
type: book
weight: 1
toc: true
comments: true
---

## Background

- LLMs is just a bunch of optimized matrices in N layers with floating-point weights.
- Generation of LLMs means doing a bunch of matrix multiplication. And doing floating point operations is expensive in terms of energy consumption.

- These numbers in matrices have a certain precision (32-bit, 16-bit, 8-bit, etc.). Based on the precision, the energy consumption varies.

- With increasing size of LLMs, deployment and training of such models have raised environmental concerns due to high energy consumption.

## What did the authors try to accomplish?

- This paper proposes a Transformer architecture called `BitNet` which uses 1-bit weights (0 or 1).

- Usually, we do training and quantization separately. But, in this paper, the authors propose a method to do quantization during training.

- As a result, the memory footprint is reduced and inference is expected faster.

## What are the key elements of the approach?

- The authors proposed a **new linear layer** with binary weights (+1 or -1) instead of conventional floating-point weights.

#### BitLinear

- LayerNorm is introduced before activation quantization to ensure stability of the model. Mean is centered to zero.

- $\gamma$ and $\beta$ are learned scaling factors for layers.

$$
\bar{x} = \text{Clip}(x \times \frac{1}{\gamma}, -1, 1)
$$

**Techniques used in BitLinear:**

1. Large learning rate - Because there is zero precision in the weights, small learning rates don't have much effect.

2. Straight-through estimator (STE) to approximate the gradient during backpropagation. (Don't fully understand how this works)

3. Mixed precision training - Gradients & activations are high precision; linear layers in attention block are low precision.

Weights centered to be zero-mean (what does this mean?) before binarization.

- scaling factor $\beta$ is used after binarization to reduce l2 error between the original and binarized weights.

## What can we use/remember from the paper??

1. If this proposed approach is scalable and stable in bigger datasets - it would significantly reduce the cost of using LLMs.
2. A new type of compute device specifically optimized for addition could take advantage of this approach.

## References

- https://arxiv.org/abs/2310.11453
- https://github.com/kyegomez/BitNet
<!-- ## TL;DR


- With increasing size of LLMs, deployment and training of such models have raised environmental concerns due to high energy consumption.

- This paper proposes a novel 1-bit Transformer architecture for LLMs called `BitNet` which uses 1-bit weights (scalable and stable).

- The results show that `BitLinear` achieves competitve performances while substantially reducing memory footprint and energy consumption compared to other quantization methods.

## What did the authors try to accomplish?

- The authors tried to address the environmental concerns raised by the deployment and training of large language models (LLMs) by proposing a novel 1-bit Transformer architecture for LLMs called `BitNet`.

## What are the key elements of the approach?

### BitLinear

{{< figure src="/blog/bitnet-llms-arch.png" width="1000px" title="">}}

The authors proposed a new linear layer with binary weights (+1 or -1) instead of conventional floating-point weights.

- Weights centered to be zero-mean (what does this mean?) before binarization.
- scaling factor $\beta$ is used after binarization to reduce l2 error between the original and binarized weights.

Further, activations are quantized to 8-bit precision; Absmax quantization is used.

- LayerNorm is introduced before activation quantization to preserve the variance of activations.

- quantization is performed per tensor during training while per token during inference - for stability and efficiency.

---

Post-training quanitzation

- existing LLM models are quantized to lower precision making them consume less memory and faster inference.

---

## What can I use from the paper??

## Conclusion

## What other references should I follow?

- BiT: robustly binarized multi-distilled transformer. NeurIPS 2022. -->
