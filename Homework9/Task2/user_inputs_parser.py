import re


class Parser:

    def complex_figure_parser(self, figure: str):
        pattern = re.compile(r'\d+|\-\d+')
        result = pattern.findall(figure)
        if len(result) == 1:
            if 'i' in figure:
                a, b = 0, ''.join(result)
            else:
                a, b = ''.join(result), 0
        else:
            a, b = result
        return a, b
