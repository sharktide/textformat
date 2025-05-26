class WordArt:
    """ Generates customizable word art banners """

    @staticmethod
    def banner(text, char="█", width=50):
        """ Creates a formatted word art banner """
        top = char * width
        middle = f"{char} {text.center(width - 4)} {char}"
        return f"{top}\n{middle}\n{top}"
