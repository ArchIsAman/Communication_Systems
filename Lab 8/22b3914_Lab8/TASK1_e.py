#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class TASK1_e(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
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

        self.settings = Qt.QSettings("GNU Radio", "TASK1_e")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.variable_constellation = variable_constellation = digital.constellation_calcdist([1,(0.707+0.707j),1j,(-0.707+0.707j),-1,(-0.707-0.707j),-1j,(0.707-0.707j)], [0, 1, 2, 3, 4, 5, 6, 7],
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.variable_constellation.set_npwr(1.0)
        self.noise_amp = noise_amp = 0.1
        self.demod_delay = demod_delay = 14
        self.b4 = b4 = 0.0625
        self.b3 = b3 = -0.125
        self.b2 = b2 = 0.25
        self.b1 = b1 = -0.5
        self.alpha = alpha = 2.5
        self.a = a = 0

        ##################################################
        # Blocks
        ##################################################

        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'Constellation')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'Chunks to symbols output - constellation')
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, 'RRC_output_constellation')
        self.top_layout.addWidget(self.tab)
        self._noise_amp_range = qtgui.Range(0, 1, 0.1, 0.1, 200)
        self._noise_amp_win = qtgui.RangeWidget(self._noise_amp_range, self.set_noise_amp, "noise_amp", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_amp_win)
        self.root_raised_cosine_filter_0_0_0 = filter.fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                3,
                (8*50000),
                50000,
                1,
                (11*8)))
        self.root_raised_cosine_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                3,
                (50000*8),
                50000,
                1,
                (11*8)))
        self.root_raised_cosine_filter_0 = filter.interp_fir_filter_ccf(
            1,
            firdes.root_raised_cosine(
                3,
                (8*50000),
                50000,
                1,
                (11*8)))
        self.rational_resampler_xxx_1_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=20,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=20,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=20,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_const_sink_x_0_0_0_0_0_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_0_0_0.set_y_axis((-1.5), 1.5)
        self.qtgui_const_sink_x_0_0_0_0_0_0.set_x_axis((-1.5), 1.5)
        self.qtgui_const_sink_x_0_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_0_0_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0_0_0_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_0_0_0.qwidget(), Qt.QWidget)
        self.tab_layout_1.addWidget(self._qtgui_const_sink_x_0_0_0_0_0_0_win)
        self.qtgui_const_sink_x_0_0_0_0_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_0_0.set_y_axis((-1.5), 1.5)
        self.qtgui_const_sink_x_0_0_0_0_0.set_x_axis((-1.5), 1.5)
        self.qtgui_const_sink_x_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_0_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0_0_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_0_0.qwidget(), Qt.QWidget)
        self.tab_layout_2.addWidget(self._qtgui_const_sink_x_0_0_0_0_0_win)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis((-1.5), 1.5)
        self.qtgui_const_sink_x_0_0.set_x_axis((-1.5), 1.5)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.qwidget(), Qt.QWidget)
        self.tab_layout_0.addWidget(self._qtgui_const_sink_x_0_0_win)
        self.low_pass_filter_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                (400000*20),
                500000,
                200,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                (400000*20),
                500000,
                200,
                window.WIN_HAMMING,
                6.76))
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccf(8, [1])
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fir_filter_xxx_0_0 = filter.fir_filter_fff(8, [1])
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(8, [1])
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(variable_constellation)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc([1,(0.707+0.707j),1j,(-0.707+0.707j),-1,(-0.707-0.707j),-1j,(0.707-0.707j)], 1)
        self._demod_delay_range = qtgui.Range(0, 100, 1, 14, 200)
        self._demod_delay_win = qtgui.RangeWidget(self._demod_delay_range, self.set_demod_delay, "'demod_delay'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._demod_delay_win)
        self.blocks_unpack_k_bits_bb_1 = blocks.unpack_k_bits_bb(3)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_char*1, (100 + 48*4 + 48))
        self.blocks_pack_k_bits_bb_1 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(3)
        self.blocks_multiply_xx_0_2_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_2 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/aryan-tamboli/EE340 - Communication Lab/Lab_8-20241023/Original_Text.txt', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/aryan-tamboli/EE340 - Communication Lab/Lab_8-20241023/out5a.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_float_1 = blocks.complex_to_float(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self._b4_range = qtgui.Range(-1, 1, 0.1, 0.0625, 200)
        self._b4_win = qtgui.RangeWidget(self._b4_range, self.set_b4, "b4", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._b4_win)
        self._b3_range = qtgui.Range(-1, 1, 0.1, -0.125, 200)
        self._b3_win = qtgui.RangeWidget(self._b3_range, self.set_b3, "b3", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._b3_win)
        self._b2_range = qtgui.Range(-1, 1, 0.1, 0.25, 200)
        self._b2_win = qtgui.RangeWidget(self._b2_range, self.set_b2, "b2", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._b2_win)
        self._b1_range = qtgui.Range(-1, 1, 0.1, -0.5, 200)
        self._b1_win = qtgui.RangeWidget(self._b1_range, self.set_b1, "b1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._b1_win)
        self.analog_sig_source_x_0_2_0 = analog.sig_source_f((400000*20), analog.GR_COS_WAVE, 500000, 1, 0, 0)
        self.analog_sig_source_x_0_2 = analog.sig_source_f((400000*20), analog.GR_SIN_WAVE, 500000, 1, 0, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f((8*1e6), analog.GR_COS_WAVE, 500000, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f((400000*20), analog.GR_SIN_WAVE, 500000, 1, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise_amp, 0)
        self._alpha_range = qtgui.Range(0, 3, 0.1, 2.5, 200)
        self._alpha_win = qtgui.RangeWidget(self._alpha_range, self.set_alpha, "alpha", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._alpha_win)
        self._a_range = qtgui.Range(0, 10, 1, 0, 200)
        self._a_win = qtgui.RangeWidget(self._a_range, self.set_a, "a", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._a_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_1, 2))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.analog_sig_source_x_0_2, 0), (self.blocks_multiply_xx_0_2, 1))
        self.connect((self.analog_sig_source_x_0_2_0, 0), (self.blocks_multiply_xx_0_2_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_xx_0_2, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_xx_0_2_0, 1))
        self.connect((self.blocks_complex_to_float_1, 1), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_complex_to_float_1, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_const_sink_x_0_0_0_0_0_0, 0))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.qtgui_const_sink_x_0_0_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_2_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_1, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_unpack_k_bits_bb_1, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_1, 0), (self.blocks_pack_k_bits_bb_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_float_to_complex_0_0, 1))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_1_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_1_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_float_1, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.root_raised_cosine_filter_0_0, 0))
        self.connect((self.rational_resampler_xxx_1_0_0, 0), (self.root_raised_cosine_filter_0_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0_0, 0), (self.fir_filter_xxx_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "TASK1_e")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_constellation(self):
        return self.variable_constellation

    def set_variable_constellation(self, variable_constellation):
        self.variable_constellation = variable_constellation
        self.digital_constellation_decoder_cb_0.set_constellation(self.variable_constellation)

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.analog_noise_source_x_0.set_amplitude(self.noise_amp)

    def get_demod_delay(self):
        return self.demod_delay

    def set_demod_delay(self, demod_delay):
        self.demod_delay = demod_delay

    def get_b4(self):
        return self.b4

    def set_b4(self, b4):
        self.b4 = b4

    def get_b3(self):
        return self.b3

    def set_b3(self, b3):
        self.b3 = b3

    def get_b2(self):
        return self.b2

    def set_b2(self, b2):
        self.b2 = b2

    def get_b1(self):
        return self.b1

    def set_b1(self, b1):
        self.b1 = b1

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha

    def get_a(self):
        return self.a

    def set_a(self, a):
        self.a = a




def main(top_block_cls=TASK1_e, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
