from PIL import Image, ImageDraw
from itertools import product


def image_to_dice(image: Image, num_of_dices: int) -> Image:

    # Converting input image to greyscale format
    greyscale = image.convert('L')

    # Splitting image to pieces
    pieces = slice_image(greyscale, num_of_dices)
    print(f"Successfully splitted on {len(pieces)} parts")

    # Dynamically draw dices images of particular size
    size = pieces[0][0].height
    dices = create_dices(size)

    # Crop the input image to the proper size
    x_last = pieces[-1][1][2]
    y_last = pieces[-1][1][3]
    img = greyscale.crop((0, 0, x_last, y_last))

    for piece, box in pieces:
        brightness = 0
        for h in range(piece.height):
            for w in range(piece.width):
                brightness += piece.getpixel((h, w))
        average_brightness = brightness / (piece.width * piece.height)

        # Determine which die to use
        for n in range(1, 7):
            if average_brightness >= 255 - (255/6 * n):
                img.paste(dices[n], box)
                break
    return img


def slice_image(img: Image, pieces_limit: int) -> list[tuple[Image, tuple[int, int, int, int]]]:
    width, height = img.size

    # Begin with maximum possible size
    size = max(width, height)

    # Try to split to equal squares
    grid = product(range(0, height - height % size, size), range(0, width - width % size, size))

    # If number of pieces is too small, just reduce the size and try again
    while len(list(grid)) < pieces_limit:
        size -= 1
        grid = product(range(0, height - height % size, size), range(0, width - width % size, size))

    grid = product(range(0, height - height % size, size), range(0, width - width % size, size))

    # Increase the size to maximum possible value
    while len(list(grid)) > pieces_limit:
        size += 1
        grid = product(range(0, height - height % size, size), range(0, width - width % size, size))

    grid = product(range(0, height - height % size, size), range(0, width - width % size, size))

    pieces = list()
    for i, j in grid:
        box = (j, i, j + size, i + size)
        pieces.append((img.crop(box), box))
    return pieces


def create_dices(side: int) -> dict[int: Image]:
    faces = {1: [(3, 3)],
             2: [(1, 1), (5, 5)],
             3: [(1, 1), (3, 3), (5, 5)],
             4: [(1, 1), (1, 5), (5, 1), (5, 5)],
             5: [(1, 1), (1, 5), (3, 3), (5, 1), (5, 5)],
             6: [(1, 1), (1, 3), (1, 5), (5, 1), (5, 3), (5, 5)]}
    offset = side / 15
    dot_size = (side - 2 * offset) / 7
    px, py = 0, 0
    dices = {}
    for num in faces.keys():
        new_image = Image.new('L', (side, side), 255)
        draw = ImageDraw.Draw(new_image)
        for dx, dy in faces[num]:
            draw.rounded_rectangle((0, 0, new_image.width, new_image.height))
            rx, ry = dx * dot_size + dot_size / 2 + offset, dy * dot_size + dot_size / 2 + offset
            r = dot_size * 1.5 / 2
            draw.ellipse((rx - px - r, side - (ry - py) - r,
                          rx - px + r, side - (ry - py) + r),
                         fill=0)
        dices[num] = new_image
    return dices


if __name__ == '__main__':
    image = Image.open(r'bonus\image_to_dice_converter\image6.jpg')
    result = image_to_dice(image, 39_000)
    result.save(r'bonus\image_to_dice_converter\result6.png')
