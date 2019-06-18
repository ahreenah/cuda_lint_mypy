"""This module exports the Mypy plugin class."""

from cuda_lint import Linter, util


class MyPy(Linter):

    """Provides an interface to mypy"""
    cmd = 'mypy'
    executable = 'mypy'
    multiline = True
    syntax = ('Python')
    regex = (
        r'(?P<stdin>.*):(?P<line>\d+): error:(?P<message>.*)'
    )
    base_cmd = (
    ''
    )
    tempfile_suffix = 'py'


    def split_match(self, match):
   
        """Return the components of the error."""
        split_match = super(MyPy, self).split_match(match)

        match, line, col, error, warning, message, near = split_match
        return match, line, 0, '', '', message, ''
        


    def cmd(self):
    
        """Return the command line to execute."""
        result = self.executable + ' ' + self.base_cmd

        code_type='python'

        result += ''

        return result
