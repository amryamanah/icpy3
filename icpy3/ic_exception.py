__author__ = 'amryf'



class IC_Exception(Exception):
    """
    An exception for the IC imaging control software. It contains a message
    property which is a string indicating what went wrong.

    error code -3 has multiple possible interpretations, sometimes from the same function!

    :param errorCode: Error code to be used to look up error message.
    """

    @property
    def message(self):
        return self._error_codes[self.error_code]

    @property
    def error_code(self):
        return self._error_code

    _error_codes = {
        #//////////////////////////////////////////////////////////////////////////
        #/*! A return value of IC_SUCCESS indicates that a function has been performed
        #without an error.
        #*/
        1   :   'IC SUCCESS', #< Return value for success.
        #//////////////////////////////////////////////////////////////////////////
        #/*! If a function returns IC_ERROR, then something went wrong.
        #*/
        0   :   'IC ERROR',#< Return value that indicates an error.
        #//////////////////////////////////////////////////////////////////////////
        #/*! This error indicates, that an HGRABBER handle has not been created yet. Please
	    #see IC_CreateGrabber() for creating an HGRABBER handle.
        #*/
       -1   :   'IC NO HANDLE',#< No device handle. HGRABBER is NULL.
        #//////////////////////////////////////////////////////////////////////////
        #/*! This return values indicates that no device has been opened. Please refer to
        #IC_OpenVideoCaptureDevice().
        #*/
       -2   :   'IC NO DEVICE', #///< No device opened, but HGRABBER is valid.
        #//////////////////////////////////////////////////////////////////////////
        # /*! This return value indicates, that the video capture device is not in live mode,
        #     but live mode is for the current function call required. Please refer to
        # 	IC_StartLive().
        # */
        #
        # #define IC_NOT_AVAILABLE -3     ///< Property not avaiable, but HGRABBER is valid.
        # //////////////////////////////////////////////////////////////////////////
        # /*! This return value indicates, that the video capture device does not support
        # 	the specified property.
        # */
        #
        # #define IC_NO_PROPERTYSET -3     ///< The Propertyset was not queried.
        # //////////////////////////////////////////////////////////////////////////
        # /*! This return value indicates, that the porperty set was not queried for
        # 	the current grabber handle. Please check, whether IC_QueryPropertySet()
        # 	was called once before using the function.
        # */
        #
        # #define IC_DEFAULT_WINDOW_SIZE_SET -3     ///< The live display window size could not be set
        # //////////////////////////////////////////////////////////////////////////
        # /*! This return value indicates, that setting of a custom live display window size
        # 	failed, because IC_SetDefaultWindowPosition() was not called with parameter false
        # 	somewhere before.
        # 	@sa IC_SetDefaultWindowPosition
        # 	@sa IC_SetWindowPosition
        # */
        # #define IC_NOT_IN_LIVEMODE -3 ///< A device has been opened, but is is not in live mode.
        #
       -3   :   'IC NOT AVAILABLE / IC NO PROPERTYSET / IC DEFAULT WINDOW SIZE SET / IC NOT IN LIVEMODE',
        # //////////////////////////////////////////////////////////////////////////
        # /*! This return value indicates, that a device does not support the requested property, or
        # 	the name of a property was written in wrong way.
        #
        # 	@sa IC_GetPropertyValueRange
        # */
       -4   :   'IC PROPERTY ITEM NOT AVAILABLE',#///< A requested property item is not available
        # //////////////////////////////////////////////////////////////////////////
        # /*! This return value indicates, that a device does not support the requested element property, or
        # 	the name of an element was written in wrong way.
        #
        # 	@sa IC_GetPropertyValueRange
        # */
       -5   :   'IC PROPERTY ELEMENT NOT AVAILABLE', #///< A requested element of a given property item is not available
        # //////////////////////////////////////////////////////////////////////////
        # /*! This return value indicates, that a property element does not support
        #     the request, that is wanted. e.g. Exposure Auto has no range, therefore
        # 	IC_GetPropertyValueRange(hGrabber, "Epxosure","Auto", &min, &max )
        # 	will return IC_PROPERTY_ELEMENT_WRONG_INTERFACE.
        #
        # 	@sa IC_GetPropertyValueRange
        # */
       -6   :   'IC PROPERTY ELEMENT WRONG INTERFACE', #///< A requested element has not the interface, which is needed.
        # //////////////////////////////////////////////////////////////////////////
        # /*! This return value indicates, that there was an index passed, which
        # 	was out of range of the number of available elements
        #
        # 	@sa IC_ListDevicesbyIndex
       -7   :   'IC INDEX OUT OF RANGE', #///< A requested element has not the interface, which is needed.
        # /////////////////////////////////////////////////////////////////////////

     -100   :   'UNKNOWN ERROR',
     -101   :   'UNKNOWN DEVICE FEATURE',
     -102   :   'VIDEO NORM INDEX OUT OF RANGE',
     -103   :   'VIDEO FORMAT INDEX OUT OF RANGE',
     -104   :   'VIDEO NORM RETURNED NULL TYPE',
     -105   :   'VIDEO FORMAT RETURNED NULL TYPE',
     -106   :   'DEVICE NAME NOT FOUND'

    }


    def __init__(self, error_code):
        # if error code does not match expected codes then assign invalid code
        if error_code in self._error_codes:
            self._error_code = error_code
        else:
            self._error_code = -100
        super().__init__(self._error_code)