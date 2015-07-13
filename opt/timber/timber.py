import datetime
import sys

def get_instance():
    if (Timber.instance == None):
        raise Exception('No previous instance found, call get_instance_with_filename() first.')
    return Timber.instance

def get_instance_with_filename(filename, loglevel):
    returnInstance = None
    if (Timber.instance == None):
        Timber.instance = Timber(filename, loglevel)
    return Timber.instance
    

class Timber ():
    instance = None

    def __init__(self, filename, loglevel):
        if (Timber.instance != None):
            raise Exception('Timber instance already exists.')
        self.filename = filename
        self.file = None

        # Log levels:
        # 5 is trace
        # 4 is debug
        # 3 is info
        # 2 is warn
        # 1 is error
        # 0 is fatal
        if loglevel == 'trace':
            self.loglevel = 5
            self.info('Log level set to trace.  I hope you like reading logs.')
        elif loglevel == 'debug':
            self.loglevel = 4
            self.info('Log level set to debug.')
        elif loglevel == 'info':
            self.loglevel = 3
            self.info('Log level set to info.')
        elif loglevel == 'warn':
            self.loglevel = 2
        elif loglevel == 'error':
            self.loglevel = 1
        elif loglevel == 'fatal':
            self.loglevel = 0
        else:
            self.fatal('Log level not defined or invalid.')

        Timber.initialized = True

    def _msg(self, message):
        timestamp = datetime.datetime.now().strftime('%Y/%m/%d - %H:%M:%S:%f')

        full_message = '%s - %s' % (timestamp, message)

        if sys.stdout.isatty():
            print(full_message)
        else:
            try:
                if self.file == None:
                    self.file = open(self.filename, 'a', 0)	
                self.file.write('%s\n' % full_message)
            except Exception as exception:
                print exception
                print full_message
    ### END def _msg

    def trace(self, message):
        if self.loglevel >= 5:
            self._msg('Trace: ' + message)
    ### END def trace

    def debug(self, message):
        if self.loglevel >= 4:
            self._msg('Debug: ' + message)
    ### END def debug

    def info(self, message):
        if self.loglevel >= 3:
            self._msg('Info: ' + message)
    ### END def log

    def warn(self, message):
        if self.loglevel >= 2:
            self._msg('Warn: ' + message)
    ### END def warn

    def error(self, message):
        if self.loglevel >= 1:
            self._msg('Error: ' + message)
    ### END def error

    def fatal(self, message):
        if self.loglevel <= 0:
            self._msg('Fatal: ' + message)
    ### END def fatal
