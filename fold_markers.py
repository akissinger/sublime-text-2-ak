import sublime, sublime_plugin
import re


def do_fold(view, start_reg, end_reg, unfold=False):
  if start_reg != None and end_reg != None:
    after_start = view.full_line(start_reg).end()
    before_end = view.line(end_reg).begin()-1
    fold_reg = sublime.Region(after_start,before_end)
    
    if unfold:
      view.unfold(fold_reg)
    else:
      view.fold(fold_reg)
    
    return fold_reg
  else:
    return None


class FoldTopMarkersCommand(sublime_plugin.TextCommand):
  def run(self, edit, unfold=False):
    start_marker = '{{{'
    end_marker = '}}}'
    start_reg = None
    
    cursor = self.view.sel()[0].begin()
    brackets = []
    pattern = '(%s|%s)' % (re.escape(start_marker), re.escape(end_marker))
    regions = self.view.find_all(pattern, 0, '$1', brackets)
        
    depth = 0
    
    for i in range(len(regions)):
      if brackets[i] == start_marker:
        if depth == 0:
          start_reg = regions[i]
        depth += 1
      else:
        depth -= 1
        if depth == 0 and start_reg != None:
          do_fold(self.view, start_reg, regions[i], unfold)
          

class FoldMarkersCommand(sublime_plugin.TextCommand):  
  def run(self, edit, unfold=False):
    start_marker = '{{{'
    end_marker = '}}}'
    start_reg = None
    end_reg = None
    
    cursor = self.view.sel()[0].begin()
    brackets = []
    pattern = '(%s|%s)' % (re.escape(start_marker), re.escape(end_marker))
    regions = self.view.find_all(pattern, 0, '$1', brackets)
        
    rstack = []
    
    for i in range(len(regions)):
      if regions[i].begin() >= cursor and len(rstack) > 0:
        if start_reg == None:
          start_reg = rstack[-1]
        
        if brackets[i] == end_marker and start_reg == rstack[-1]:
          end_reg = regions[i]
          break
          
      if brackets[i] == start_marker: rstack.append(regions[i])
      elif len(rstack)>0: rstack.pop()
    
          
    fold_reg = do_fold(self.view, start_reg, end_reg, unfold)
    
    if not unfold:
      self.view.sel().clear()
      self.view.sel().add(sublime.Region(fold_reg.end(),fold_reg.end()))
