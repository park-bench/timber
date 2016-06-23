# Copyright 2015 Joel Allen Luellwitz and Andrew Klapp
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging

# Define trace log level
TRACE_LEVEL_NUMBER = 5
def trace(self, message, *args, **kws):
    if self.isEnabledFor(TRACE_LEVEL_NUMBER):
        self._log(TRACE_LEVEL_NUMBER, message, args, **kws)

# Add trace log level to logging.Logger
logging.addLevelName(TRACE_LEVEL_NUMBER, 'TRACE')
logging.Logger.trace = trace

# TODO: Consider doing this more transperently somehow?
#   Maybe we can replace the logger.getLogger method?

def get_root_logger(log_level, log_file):
    # Instantiate logger
    logger.logging.getLogger()
    logger.setLevel(log_level)

    # Add stdoutHandler and fileHandler
    stdout_handler = logging.StreamHandler()
    logger.addHandler(stdout_handler)
    logger.info('Logger instantiated.')

    file_handler = logging.fileHandler(log_file)
    logger.addHandler(file_handler)
    logger.info('Log file acquired.')

    return logger
