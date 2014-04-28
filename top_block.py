#!/usr/bin/env python2
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Sun Apr 27 14:34:09 2014
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.offset = offset = 0.0003
        self.multiple = multiple = 2
        self.biasTwo = biasTwo = 0
        self.biasOne = biasOne = 0
        self.baseFrequency = baseFrequency = 100
        self.ampTwo = ampTwo = 0.5
        self.ampOne = ampOne = 0.15

        ##################################################
        # Blocks
        ##################################################
        _offset_sizer = wx.BoxSizer(wx.VERTICAL)
        self._offset_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_offset_sizer,
        	value=self.offset,
        	callback=self.set_offset,
        	label='offset',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._offset_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_offset_sizer,
        	value=self.offset,
        	callback=self.set_offset,
        	minimum=-0.001,
        	maximum=0.001,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_offset_sizer)
        _multiple_sizer = wx.BoxSizer(wx.VERTICAL)
        self._multiple_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_multiple_sizer,
        	value=self.multiple,
        	callback=self.set_multiple,
        	label="multiple",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._multiple_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_multiple_sizer,
        	value=self.multiple,
        	callback=self.set_multiple,
        	minimum=0,
        	maximum=3,
        	num_steps=50,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_multiple_sizer)
        _biasTwo_sizer = wx.BoxSizer(wx.VERTICAL)
        self._biasTwo_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_biasTwo_sizer,
        	value=self.biasTwo,
        	callback=self.set_biasTwo,
        	label="biasTwo",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._biasTwo_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_biasTwo_sizer,
        	value=self.biasTwo,
        	callback=self.set_biasTwo,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_biasTwo_sizer)
        _biasOne_sizer = wx.BoxSizer(wx.VERTICAL)
        self._biasOne_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_biasOne_sizer,
        	value=self.biasOne,
        	callback=self.set_biasOne,
        	label="biasOne",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._biasOne_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_biasOne_sizer,
        	value=self.biasOne,
        	callback=self.set_biasOne,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_biasOne_sizer)
        _baseFrequency_sizer = wx.BoxSizer(wx.VERTICAL)
        self._baseFrequency_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_baseFrequency_sizer,
        	value=self.baseFrequency,
        	callback=self.set_baseFrequency,
        	label='baseFrequency',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._baseFrequency_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_baseFrequency_sizer,
        	value=self.baseFrequency,
        	callback=self.set_baseFrequency,
        	minimum=0,
        	maximum=1000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_baseFrequency_sizer)
        _ampTwo_sizer = wx.BoxSizer(wx.VERTICAL)
        self._ampTwo_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_ampTwo_sizer,
        	value=self.ampTwo,
        	callback=self.set_ampTwo,
        	label="ampTwo",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._ampTwo_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_ampTwo_sizer,
        	value=self.ampTwo,
        	callback=self.set_ampTwo,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_ampTwo_sizer)
        _ampOne_sizer = wx.BoxSizer(wx.VERTICAL)
        self._ampOne_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_ampOne_sizer,
        	value=self.ampOne,
        	callback=self.set_ampOne,
        	label="ampOne",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._ampOne_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_ampOne_sizer,
        	value=self.ampOne,
        	callback=self.set_ampOne,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_ampOne_sizer)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_vff((biasOne, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((biasTwo, ))
        self.audio_sink_0 = audio.sink(samp_rate, "default", False)
        self.analog_sig_source_x_2 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 0.0001, 0.5, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, baseFrequency*multiple+offset, ampTwo, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, baseFrequency, ampOne, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.audio_sink_0, 1))
        self.connect((self.blocks_multiply_xx_1, 0), (self.audio_sink_0, 0))
        self.connect((self.analog_sig_source_x_2, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.analog_sig_source_x_2, 0), (self.blocks_multiply_xx_0, 0))


# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2.set_sampling_freq(self.samp_rate)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self.analog_sig_source_x_1.set_frequency(self.baseFrequency*self.multiple+self.offset)
        self._offset_slider.set_value(self.offset)
        self._offset_text_box.set_value(self.offset)

    def get_multiple(self):
        return self.multiple

    def set_multiple(self, multiple):
        self.multiple = multiple
        self.analog_sig_source_x_1.set_frequency(self.baseFrequency*self.multiple+self.offset)
        self._multiple_slider.set_value(self.multiple)
        self._multiple_text_box.set_value(self.multiple)

    def get_biasTwo(self):
        return self.biasTwo

    def set_biasTwo(self, biasTwo):
        self.biasTwo = biasTwo
        self._biasTwo_slider.set_value(self.biasTwo)
        self._biasTwo_text_box.set_value(self.biasTwo)
        self.blocks_add_const_vxx_0.set_k((self.biasTwo, ))

    def get_biasOne(self):
        return self.biasOne

    def set_biasOne(self, biasOne):
        self.biasOne = biasOne
        self._biasOne_slider.set_value(self.biasOne)
        self._biasOne_text_box.set_value(self.biasOne)
        self.blocks_add_const_vxx_0_0.set_k((self.biasOne, ))

    def get_baseFrequency(self):
        return self.baseFrequency

    def set_baseFrequency(self, baseFrequency):
        self.baseFrequency = baseFrequency
        self._baseFrequency_slider.set_value(self.baseFrequency)
        self._baseFrequency_text_box.set_value(self.baseFrequency)
        self.analog_sig_source_x_1.set_frequency(self.baseFrequency*self.multiple+self.offset)
        self.analog_sig_source_x_0.set_frequency(self.baseFrequency)

    def get_ampTwo(self):
        return self.ampTwo

    def set_ampTwo(self, ampTwo):
        self.ampTwo = ampTwo
        self._ampTwo_slider.set_value(self.ampTwo)
        self._ampTwo_text_box.set_value(self.ampTwo)
        self.analog_sig_source_x_1.set_amplitude(self.ampTwo)

    def get_ampOne(self):
        return self.ampOne

    def set_ampOne(self, ampOne):
        self.ampOne = ampOne
        self.analog_sig_source_x_0.set_amplitude(self.ampOne)
        self._ampOne_slider.set_value(self.ampOne)
        self._ampOne_text_box.set_value(self.ampOne)

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
    tb = top_block()
    tb.Start(True)
    tb.Wait()

