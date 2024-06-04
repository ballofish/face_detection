def property_out(video_path: str) -> list:
    '''
    return the video property as width, height, fps, fourcc, frame_count
        width               : float
        height              : float
        fps                 : float
        fourcc              : str
        frame_count         : float
        run_time            : float
        checking frame num  : int
    '''
    # import cv2
    from cv2 import VideoCapture
    try:
        '''
        Create VideoCapture instance
            Usage 1 : Using Camera, take streaming video from system camera
                cv2.VideoCapture(index, apiPreference=None) -> retval
                    index : if you want open default system camera like webcam in labtop index = 0
                        if you have several built-in camera put index ordering number
                    apiPreference : choose prefer camera handling method
                    retval : return cv2.VideoCapture object
            Usage 2 : Read video file or web like Youtube
                cv2.VideoCapture(filename, apiPreference=None) -> retval
                    filename : name of video file, sequence of video frame, video streaming url etc.
                        ex) 'video.avi','img_%02d.jpg','protocol://host:post/script?params|auth'
                    apiPreference : choose prefer camera handling method
                    retval : return cv2.VideoCapture object
                
        cv2.VideoCapture method
        
        cv2.VideoCapture.open(index, apiPreference=None) -> retval
        (if you create instance as VideoCapture(0), don't need this method)
            retval : success -> True, Fail -> False
            
        cv2.VideoCapture.isOpened() -> retval
            retval : success -> True, Fail -> False
            
        cv.VideoCapture.get(propId) -> retval
            propId : could use as number starting at 0
            ex) print('Frame width:', video.get(cv2.CAP_PROP_FRAME_WIDTH))
            ex) print('Frame width:', video.get(3))
                CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds or video capture timestamp.
                CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
                CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file: 0 - start of the film, 1 - end of the film.
                CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
                CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
                CV_CAP_PROP_FPS Frame rate.
                CV_CAP_PROP_FOURCC 4-character code of codec.
                CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
                CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve().
                CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
                CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
                CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
                CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
                CV_CAP_PROP_HUE Hue of the image (only for cameras).
                CV_CAP_PROP_GAIN Gain of the image (only for cameras).
                CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
                CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
                CV_CAP_PROP_WHITE_BALANCE_U The U value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
                CV_CAP_PROP_WHITE_BALANCE_V The V value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
                CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
                CV_CAP_PROP_ISO_SPEED The ISO speed of the camera (note: only supported by DC1394 v 2.x backend currently)
                CV_CAP_PROP_BUFFERSIZE Amount of frames stored in internal buffer memory (note: only supported by DC1394 v 2.x backend currently)
            retval : success -> True, Fail -> False
            
        default(and maximum size) width x height : 640 x 480
        
        cv2.VideoCapture.set(propId, value) -> retval
            propId : could use as number starting at 0
                CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
                CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
                CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file: 0 - start of the film, 1 - end of the film.
                CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
                CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
                CV_CAP_PROP_FPS Frame rate.
                CV_CAP_PROP_FOURCC 4-character code of codec.
                 CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
                CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve().
                CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
                CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
                CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
                CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
                CV_CAP_PROP_HUE Hue of the image (only for cameras).
                CV_CAP_PROP_GAIN Gain of the image (only for cameras).
                CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
                CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
                CV_CAP_PROP_WHITE_BALANCE_U The U value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
                CV_CAP_PROP_WHITE_BALANCE_V The V value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
                CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
                CV_CAP_PROP_ISO_SPEED The ISO speed of the camera (note: only supported by DC1394 v 2.x backend currently)
                CV_CAP_PROP_BUFFERSIZE Amount of frames stored in internal buffer memory (note: only supported by DC1394 v 2.x backend currently)
            value : Value of the property.
        '''
        video_obj = VideoCapture(video_path, apiPreference=None)
        property_list = []
        # extract width,height,fps,fourcc,frame_count
        for i in range(3,8):
            property_list.append(video_obj.get(i))
        # (float)fourcc to (string)fourcc
        fourcc = int(property_list[3])
        property_list[3] = chr(fourcc & 0xff) + chr((fourcc >> 8) & 0xff) + chr((fourcc >> 16) & 0xff) + chr((fourcc >> 24) & 0xff)
        # append run_time : frame_count / fps
        property_list.append(property_list[-1] / property_list[2])
        print(property_list)
        # append checking frame num per seconds
        property_list.append(round(property_list[2]))
    except Exception as e:
        print('EXCEPT! main/video_check/property_out')
        print(e)
    else:
        return property_list
    finally:
        video_obj.release()