import sublime, sublime_plugin

class LatexAlignMatrixCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if len(self.view.sel()) != 1:
            print("latex_align_matrix: Must have exactly one selection.")
            return
        sel = self.view.sel()[0]
        min_indent = 0
        row_breaks = {}
        row_widths = {}
        matr = []
        for i, line in enumerate(self.view.lines(sel)):
            row_str = self.view.substr(line).rstrip()
            if row_str.endswith('\\\\'):
                row_breaks[i] = True
                row_str = row_str[0:-2]
            else:
                row_breaks[i] = False
            row = []
            indent = len(row_str) - len(row_str.lstrip())
            if i == 0 or indent < min_indent:
                min_indent = indent
            for j, x in enumerate(row_str.split('&')):
                x = x.strip()
                row.append(x)
                if (not row_widths.has_key(j)) or row_widths[j] < len(x):
                    row_widths[j] = len(x)
            matr.append(row)
        
        lines = [min_indent * ' ' + ' & '.join([
            x + (row_widths[j] - len(x)) * ' '
              + (' \\\\' if j == len(row) - 1 and row_breaks[i] else '')
            for j,x in enumerate(row)]) for i,row in enumerate(matr)]
        
        sel = sel.cover(self.view.line(sel.begin())).cover(self.view.line(sel.end()))
        self.view.replace(edit, sel, '\n'.join(lines))
