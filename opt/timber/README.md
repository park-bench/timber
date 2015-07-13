# Timber

Timber is a very basic logging library for daemons that will output to stdout if
a terminal is attached and to a file if no terminal is attached. The first file
location specified in a process will be the log file. All subsequent file
locations specified (such as by imported modules) will be ignored.

Timber is licensed under the GNU GPLv3.

Bug fixes are welcome.
