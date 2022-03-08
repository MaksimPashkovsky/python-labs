"""
Converting video (.mp4) to one comprised of dice image frames
Be careful with FPS
See example at: https://youtu.be/ssBlbT-4SPA
"""

import os
from dice_image import image_to_dice
from PIL import Image
import threading
from itertools import zip_longest


def video_to_dice(input_video, frames_dir, dice_frames_dir, dice_video, final_result, fps, num_of_dices):

    if not os.path.exists(frames_dir):
        os.mkdir(frames_dir)

    if not os.path.exists(dice_frames_dir):
        os.mkdir(dice_frames_dir)

    # Splitting input video into frames
    split_to_frames(input_video, fps, save_dir=frames_dir)

    files = os.listdir(frames_dir)
    # Converting each frame into dice image
    num_of_threads = 10

    parts = list(zip_longest(*[iter(files)]*num_of_threads))
    threads = []
    for part in parts:
        t = threading.Thread(target=func, args=(part, frames_dir, num_of_dices, dice_frames_dir))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    delete_files(frames_dir)

    # Converting dice frames to video
    frames_to_video(dice_frames_dir, fps, dice_video)

    delete_files(dice_frames_dir)

    # Adding sound from input video to dice video
    add_sound(input_video, dice_video, final_result)
    os.remove(dice_video)


def func(files, frames_dir, num_of_dices, dice_frames_dir):
    for file in files:
        if file is not None:
            image = Image.open(frames_dir + file)
            dice = image_to_dice(image, num_of_dices)
            dice.save(dice_frames_dir + file)


def split_to_frames(filename: str, fps: int, save_dir: str):
    command = ['ffmpeg',
               '-i', filename,
               '-r', str(fps),
               '-f', 'image2',
               save_dir + '%d.png']
    os.system(' '.join(command))


def frames_to_video(dice_frames_folder: str, fps: int, result: str):
    command = ['ffmpeg',
               '-r', str(fps),
               '-f', 'image2',
               '-i', dice_frames_folder + '%d.png',
               '-vf', 'pad=ceil(iw/2)*2:ceil(ih/2)*2',
               '-vcodec', 'libx264',
               '-crf', '25',
               '-pix_fmt', 'yuv420p',
               result]
    os.system(' '.join(command))


def add_sound(source: str, dest: str, result: str):
    command = ['ffmpeg',
               '-i', source,
               '-i', dest,
               '-map', '1:V:0',
               '-map', '0:a:0',
               '-c', 'copy',
               '-f', 'mp4',
               '-movflags', '+faststart',
               result]
    os.system(' '.join(command))


def delete_files(folder: str):
    files = os.listdir(folder)
    for file in files:
        os.remove(folder + file)


if __name__ == '__main__':

    input_video = 'bonus/image_to_dice_converter/input.mp4'
    frames_dir = 'bonus/image_to_dice_converter/frames/'
    dice_frames_dir = 'bonus/image_to_dice_converter/dice_frames/'
    dice_video = 'bonus/image_to_dice_converter/dicevideo.mp4'
    final_result = 'bonus/image_to_dice_converter/result.mp4'
    fps = 30
    num_of_dices = 4100

    video_to_dice(input_video, frames_dir, dice_frames_dir, dice_video, final_result, fps, num_of_dices)