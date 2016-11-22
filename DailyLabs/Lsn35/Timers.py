# CS 210 - Introduction to Programming - Fall 2014
#
# Author: _YOUR_NAME_HERE_
#
# Section: T1A/T3A, Dr. Bower
#
# Documentation Statement: None.
#

""" This file contains a simple Timer class extending Thread. """

from threading import Thread
from time import time, sleep
import winsound


class Timer( Thread ):
    """ Simple Timer class to be executed in a Thread where it will count
        down for the specified duration, sounding an alarm when complete.
    """

    def __init__( self, duration, progress_display="" ):
        """ Create the Timer object with the specified duration and progress display character. """
        # Make sure the Thread constructor does anything it needs to do.
        super().__init__()
        # Save the parameters as attributes so they are avaialable in run().
        self.duration = duration
        self.progress_display = progress_display

    def run( self ):
        """ This method is called when the Thread/Timer object is started. """
        start_time = time()
        while time() - start_time < self.duration:
            print( self.progress_display, end="", flush=True )  # Show progress.
            sleep( 1 )  # Accurate to one second.

        self.sound_alarm()

    def sound_alarm( self ):
        """ Print a message when the timer countdown is complete. """
        print( "Done" + self.progress_display )


class Bell( Timer ):
    """ This subclass of Timer plays the windows exclamation sound. """
    def sound_alarm( self ):
        """ Sound a simple beep when the timer countdown is complete. """
        super().sound_alarm()
        winsound.MessageBeep( winsound.MB_ICONEXCLAMATION )


class Sound( Timer ):
    """ This subclass of Timer plays a sound file in wav format. """
    # https://www.daniweb.com/software-development/python/code/216438/play-those-cute-little-wave-files-python

    def __init__( self, duration, progress_display="", sound_file="C:/Windows/Media/tada.wav" ):
        """ Creates the Sound timer, saving the sound file name. """
        # Make sure the Thread constructor does anything it needs to do.
        super().__init__( duration, progress_display )
        self.sound_file = sound_file

    def sound_alarm( self ):
        """ Plays the sound file when the timer countdown is complete. """
        super().sound_alarm()
        winsound.PlaySound( self.sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC )


class Notes( Timer ):
    """ This subclass of Timer plays a series of notes. """
    # http://stackoverflow.com/questions/17423267/pythons-winsound-beep-pause-issues

    def __init__( self, duration, progress_display="", notes="C", note_length=250 ):
        """ Creates the Notes timer, saving the notes string. """
        # Make sure the Thread constructor does anything it needs to do.
        super().__init__( duration, progress_display )
        self.notes = notes
        self.note_length = 250

    def sound_alarm( self ):
        """ Plays the series of notes when the timer countdown is complete. """
        super().sound_alarm()

        for note in self.notes:
            winsound.Beep( self.get_frequency( note ), self.note_length )

    def get_frequency( self, note ):
        """  """
        if note == 'C': return self.frequency( 3 )
        if note == 'D': return self.frequency( 5 )
        if note == 'E': return self.frequency( 7 )
        if note == 'F': return self.frequency( 8 )
        if note == 'G': return self.frequency( 10 )
        if note == 'A': return self.frequency( 12 )
        if note == 'B': return self.frequency( 14 )

    def frequency( self, half_notes_from_A4 ):
        """  """
        return int( 440 * ( 2 ** ( 1.0 / 12.0 ) ) ** half_notes_from_A4 )


def main():
    """ Main program to run the simple stopwatch. """

    # Create and start a few timers.
    timers = [ Timer( 3, '.' ), Bell( 5, '-' ), Sound( 7, '+' ), Notes( 10, '*', "EDCDEEE" ) ]
    for t in timers:
        t.start()

    # Nothing else to do here, so no need for the calls to join()
    # as in the previous example.


######## Main program ########
if __name__ == "__main__":
    main()
