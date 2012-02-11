import sublime, sublime_plugin

class WordCountCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        buf = self.view.substr(sublime.Region(0, len(self.view)))
        sentences = buf.count('?') + buf.count('!') + buf.count('.')
        words = len(buf.split(None))
        lines = buf.count('\n') + 1
        chars = len(buf)
        sublime.status_message('{0} lines, {1} sentences, {2} words, {3} characters'
            .format(lines, sentences, words, chars))
