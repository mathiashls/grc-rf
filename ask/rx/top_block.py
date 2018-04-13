#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Mar 27 10:45:15 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2.88e6
        self.freq_corr = freq_corr = 0
        self.freq = freq = 433e6
        self.cte = cte = -380e-3

        ##################################################
        # Blocks
        ##################################################
        _freq_corr_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_corr_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_corr_sizer,
        	value=self.freq_corr,
        	callback=self.set_freq_corr,
        	label='freq_corr',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_corr_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_corr_sizer,
        	value=self.freq_corr,
        	callback=self.set_freq_corr,
        	minimum=-100,
        	maximum=100,
        	num_steps=200,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_corr_sizer)
        _freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	label='freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	minimum=420e6,
        	maximum=434e6,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_sizer)
        _cte_sizer = wx.BoxSizer(wx.VERTICAL)
        self._cte_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_cte_sizer,
        	value=self.cte,
        	callback=self.set_cte,
        	label='cte',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._cte_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_cte_sizer,
        	value=self.cte,
        	callback=self.set_cte,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_cte_sizer)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=500e-3,
        	v_offset=1,
        	t_scale=100e-6,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=2,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(freq, 0)
        self.rtlsdr_source_0.set_freq_corr(freq_corr, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(30, 0)
        self.rtlsdr_source_0.set_bb_gain(30, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)

        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 480e3, 48e3, firdes.WIN_HAMMING, 6.76))
        self.channels_quantizer_0 = channels.quantizer(2)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((2, ))
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_float*1, 120)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_add_const_vxx_1 = blocks.add_const_vff((ord('0'), ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((cte, ))
        self.blks2_tcp_sink_0 = grc_blks2.tcp_sink(
        	itemsize=gr.sizeof_char*1,
        	addr='127.0.0.1',
        	port=3333,
        	server=False,
        )
        self.analog_agc_xx_0 = analog.agc_ff(1e-4, 1.0, 1.0)
        self.analog_agc_xx_0.set_max_gain(65536)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc_xx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.channels_quantizer_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.wxgui_scopesink2_0, 1))
        self.connect((self.blocks_add_const_vxx_1, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.analog_agc_xx_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.blks2_tcp_sink_0, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_1, 0))
        self.connect((self.channels_quantizer_0, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.channels_quantizer_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.wxgui_fftsink2_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 480e3, 48e3, firdes.WIN_HAMMING, 6.76))

    def get_freq_corr(self):
        return self.freq_corr

    def set_freq_corr(self, freq_corr):
        self.freq_corr = freq_corr
        self._freq_corr_slider.set_value(self.freq_corr)
        self._freq_corr_text_box.set_value(self.freq_corr)
        self.rtlsdr_source_0.set_freq_corr(self.freq_corr, 0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_slider.set_value(self.freq)
        self._freq_text_box.set_value(self.freq)
        self.rtlsdr_source_0.set_center_freq(self.freq, 0)

    def get_cte(self):
        return self.cte

    def set_cte(self, cte):
        self.cte = cte
        self._cte_slider.set_value(self.cte)
        self._cte_text_box.set_value(self.cte)
        self.blocks_add_const_vxx_0.set_k((self.cte, ))


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
