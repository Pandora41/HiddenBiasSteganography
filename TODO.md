## TODO

- [ ] Test on diverse image datasets (e.g., CIFAR-10 classifier as a carrier model)
- [ ] Compare with float32 LSB steganography — modify only the mantissa LSBs of weights instead of full replacement (subtler, harder to detect statistically)
- [ ] Review training-time watermarking (Uchida et al., 2017) as a proper baseline comparison for the model fingerprinting use case
- [ ] Add Related Work section to paper — mention deep stego methods (HiDDeN, SteganoGAN) as image-domain context, NOT direct comparison
- [ ] Add encryption layer (XOR or AES) before embedding to prevent plain-ASCII readout
- [ ] Support PyTorch .pt/.pth checkpoint format
- [ ] Write formal paper draft (expand Experiments + add Results + Conclusion sections)
- [ ] Submit to arXiv or IEEE student conf?
