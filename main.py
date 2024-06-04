def video_check(video_path : str) -> None:
    from vid_property import property_out
    property_out(video_path)

def video_path_out():
    from os import path
    return '/'.join([path.abspath('.').replace('\\', '/'), 'vid_src', 'clip_00.mp4'])
def main():
    video_path = video_path_out()
    video_check(video_path)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run("main()")

    # import time
    # start_time = time.process_time()
    # end_time = time.process_time()
    # print(end_time - start_time)