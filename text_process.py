from PIL import ImageFont


def text_wrap(text: str, font: ImageFont, max_width: float) -> list:
    """
        'this function break the multiline text in line required by max_Width'
    :param text: MultiLine text
    :param font: Font of the text
    :param max_width: max_width of image to wrap the text
    :return: list of lines
    """
    lines = []

    # if width of text is ok, don't do anything
    if font.getbbox(text)[2] <= max_width:
        lines.append(text)
    else:
        # split the text based on white space and

        words = text.split(' ')
        i = 0

        # append every word to a line while its width is shorter than max width

        while i < len(words):
            line = ''
            while i < len(words) and font.getbbox(line + words[i])[2] <= (max_width-10):
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1

                # when the line gets longer than the max width do not append the word,
                # add the line to the lines array

            lines.append(line)

    return lines
