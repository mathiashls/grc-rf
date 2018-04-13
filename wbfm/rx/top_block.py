#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Tue Mar  6 10:26:44 2018
##################################################

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import osmosdr
import sip
import sys

class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 2
        self.samp_rate = samp_rate = 2.88e6
        self.freq = freq = 93.7e6

        ##################################################
        # Blocks
        ##################################################
        self._volume_layout = Qt.QVBoxLayout()
        self._volume_tool_bar = Qt.QToolBar(self)
        self._volume_layout.addWidget(self._volume_tool_bar)
        self._volume_tool_bar.addWidget(Qt.QLabel("volume"+": "))
        self._volume_counter = Qwt.QwtCounter()
        self._volume_counter.setRange(0, 20, 1)
        self._volume_counter.setNumButtons(2)
        self._volume_counter.setValue(self.volume)
        self._volume_tool_bar.addWidget(self._volume_counter)
        self._volume_counter.valueChanged.connect(self.set_volume)
        self._volume_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._volume_slider.setRange(0, 20, 1)
        self._volume_slider.setValue(self.volume)
        self._volume_slider.setMinimumWidth(200)
        self._volume_slider.valueChanged.connect(self.set_volume)
        self._volume_layout.addWidget(self._volume_slider)
        self.top_layout.addLayout(self._volume_layout)
        self._freq_layout = Qt.QVBoxLayout()
        self._freq_tool_bar = Qt.QToolBar(self)
        self._freq_layout.addWidget(self._freq_tool_bar)
        self._freq_tool_bar.addWidget(Qt.QLabel("freq"+": "))
        self._freq_counter = Qwt.QwtCounter()
        self._freq_counter.setRange(76e6, 108e6, 200e3)
        self._freq_counter.setNumButtons(2)
        self._freq_counter.setValue(self.freq)
        self._freq_tool_bar.addWidget(self._freq_counter)
        self._freq_counter.valueChanged.connect(self.set_freq)
        self._freq_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._freq_slider.setRange(76e6, 108e6, 200e3)
        self._freq_slider.setValue(self.freq)
        self._freq_slider.setMinimumWidth(200)
        self._freq_slider.valueChanged.connect(self.set_freq)
        self._freq_layout.addWidget(self._freq_slider)
        self.top_layout.addLayout(self._freq_layout)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(0, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(30, 0)
        self.rtlsdr_source_0.set_bb_gain(30, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"QT GUI Plot", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        
        
        self.low_pass_filter_1 = filter.interp_fir_filter_fff(1, firdes.low_pass(
        	1, 48e3, 15e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(10, firdes.low_pass(
        	1, samp_rate, 100e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=samp_rate/10,
        	audio_decimation=6,
        )
        self.analog_fm_deemph_0 = analog.fm_deemph(fs=samp_rate/10, tau=75e-6)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.rtlsdr_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.analog_fm_deemph_0, 0))
        self.connect((self.analog_fm_deemph_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.qtgui_sink_x_0, 0))


# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))
        self._volume_counter.setValue(self.volume)
        self._volume_slider.setValue(self.volume)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 100e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_counter.setValue(self.freq)
        self._freq_slider.setValue(self.freq)
        self.rtlsdr_source_0.set_center_freq(self.freq, 0)

if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    qapp = Qt.QApplication(sys.argv)
    tb = top_block()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets

