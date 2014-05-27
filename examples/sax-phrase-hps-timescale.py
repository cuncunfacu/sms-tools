import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hamming, triang, blackmanharris
from scipy.fftpack import fft, ifft, fftshift
import math
import sys, os, functools, time

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../software/models/'))
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../software/transformations/'))

import hpsModel as HPS
import hpsTransformations as HPST
import utilFunctions as UF

if __name__ == '__main__':
	(fs, x) = UF.wavread(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../sounds/sax-phrase.wav'))
	w = np.blackman(601)
	N = 1024
	t = -100
	nH = 100
	minf0 = 350
	maxf0 = 700
	f0et = 5
	maxnpeaksTwm = 5
	minSineDur = .1
	harmDevSlope = 0.01
	Ns = 512
	H = Ns/4
	stocf = .2
	hfreq, hmag, hphase, mYst = HPS.hpsModelAnal(x, fs, w, N, H, t, nH, minf0, maxf0, f0et, harmDevSlope, minSineDur, Ns, stocf)
	timeScaling = np.array([0, 0, 0.211, 0.211, 0.39, 0.39, 0.618, 0.618, 0.816, 0.816, 0.879, 0.879, 1.077, 1.077+0.8, 1.149, 1.149+0.8, 2.172, 2.172, 2.184, 2.184, 2.680, 2.680, 2.837, 2.837, 3.276, 3.276, 4.397, 4.397, 4.614, 4.614, 4.818, 4.818, 4.852, 4.852, 5.068, 5.068, 6.176, 6.176, 6.612, 6.612, 6.843, 6.843, 7.258, 7.258, 7.309, 7.309, 8.009, 8.009, 8.229, 8.229, 8.782, 8.782, 8.842, 8.842, 9.379, 9.379])
	yhfreq, yhmag, ystocEnv = HPST.hpsTimeScale(hfreq, hmag, mYst, timeScaling)
	y, yh, yst = HPS.hpsModelSynth(yhfreq, yhmag, np.array([]), ystocEnv, Ns, H, fs)
	UF.play(y, fs)
		# wp.wavwrite(y,fs,'sax-phrase-total-synthesis.wav')
		# wp.wavwrite(yh,fs,'sax-phrase-harmonic-component.wav')
		# wp.wavwrite(yr,fs,'sax-phrase-residual-component.wav')
		# wp.wavwrite(yst,fs,'sax-phrase-stochastic-component.wav')
