from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getbbox(text)[2] <= max_width:
        print("font size = ", font.getbbox(text)[2])
        print(type(font))
        lines.append(text)
    else:
        # split the line by spaces to get words
        words = text.split(' ')
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ''
            while i < len(words) and font.getbbox(line + words[i])[2] <= (max_width-15):
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word,
            # add the line to the lines array
            lines.append(line)
    return lines


def draw_text(text):
    # open the background file
    img = Image.open('apj.jpg')

    # size() returns a tuple of (width, height)
    img_width, img_hight = img.size
    print("image size", img.size)
    # create the ImageFont instance
    font_file_path = 'fonts/Avenir-Medium.ttf'
    font = ImageFont.truetype('arial.ttf', size=50, encoding="unic")
    font_hight = font.getbbox('hg',)[-1]
    # get shorter lines
    lines = text_wrap(text, font, img_width // 2)
    print(lines)  # ['This could be a single line text ', 'but its too long to fit in one. ']
    y = img_hight //3
    draw = ImageDraw.Draw(img)
    for i in lines:
        draw.text((img_width // 2, y), i, font=font)
        y += font_hight
    # img.show()
    print("DONE")


if __name__ == '__main__':
    # draw_text("This could be a single line text but its too long to fit in one.")
    draw_text("“Don't take rest after your first victory because if you fail in second,more lips are waiting to say that your first victory was just luck.”")
