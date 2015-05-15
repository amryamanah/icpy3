__author__ = 'amryf'


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .ic_grabber_dll import IC_GrabberDLL
from .ic_camera import IC_Camera
from .ic_exception import IC_Exception
from IPython import embed

class IC_ImagingControl(object):

    def init_library(self):
        """
        Initialise the IC Imaging Control library.
        """
        # remember device objects by unique name
        self._devices = []

        # no license key needed anymore
        err = IC_GrabberDLL.init_library(None)
        if err != 1:
            raise IC_Exception(err)

    def get_device_by_dialog(self):
        device = IC_Camera(show_dialog=True)
        self._devices.append(device)
        return device

    def get_device_by_file(self, filename):
        device = IC_Camera(setting_file=filename)
        self._devices.append(device)
        return device

    def close_library(self):
        """
        Close the IC Imaging Control library, and close and release all references to camera devices.
        """
        # release handle grabber objects of cameras as they won't be needed again.
        # try to close & delete each known device, but only if we own the reference to it!
        for device in self._devices:
                IC_GrabberDLL.release_grabber(device._handle)

        self._devices = None
        # close lib
        IC_GrabberDLL.close_library()
