'''
Created on 11 juillet 2014.
@author: Odile
'''

class Sequence(object):
    '''
    Manage the sequence of pulses.\n
    Transform the pulses into 32 bits words for the sequencer.
    
    :Example:
    
    >>> from pkg1.Sequencer import Sequence
    >>> pulses = ((0, 5, 1), (1, 6, 1), (1, 32, 1))
    >>> seq=Sequence()
    >>> seq.sortPulses(pulses)
    >>> print (seq.delays)
    [5, 1, 1, 25, 1]    
    >>> for i in list(range(len(seq.outputs))):
        print(format(seq.outputs[i], '08X'), end=' ')
    >>> print (s.data[0:3])
    >>> print (s.stepTime)
    [0.147, 0.148, 0.146]
    0.1
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.outputs = []
        self.delays = []
        
    def sortPulses(self, pulses):
        '''
        Constructor
        '''
        """ Build lists to sort pulse durations and channels """
        waits = []
        durations = []
        pulse_waits = []
        pulse_true = []
        """ Build lists to sort pulse durations and channels """
        """ pulse[0]=channel, pulse[1]=wait_delay, pulse[2]=duration """
        for i, pulse in enumerate(pulses):
            waits.append([pulse[1], pulse[0]])
            durations.append([pulse[2], pulse[0]])
            pulse_waits.append(pulse[1])
            pulse_true.append([False, pulse[0]])
            
        """ Find first pulse and last pulse """
        values = []
        delays = []
        delay = min(pulse_waits)
        delays.append(delay)
        out = 0x0000
        values.append(out)

        max_wait = max(pulse_waits)
        max_id = pulse_waits.index(max_wait)
        max_wait += durations[max_id][0]
                
        """ start looking for pulses after the first one """
        cur_wait = delays[0]
        
        while cur_wait < max_wait:
            min_waits = []
            
            for i in list(range(len(waits))):
                waits[i][0] -= delay
                
                if (waits[i][0] == 0 and pulse_true[i][0] == False):
                    mask = 1 << waits[i][1]
                    out = out ^ mask
                    waits[i][0] += durations[i][0]
                    pulse_true[i][0] = True
                    min_waits.append(waits[i][0])
                elif (waits[i][0] == 0 and pulse_true[i][0] == True):
                    mask = 1 << waits[i][1]
                    out = out ^ mask
                    pulse_true[i][0] = False
                else:
                    if (waits[i][0] > 0):
                        min_waits.append(waits[i][0])
                        
            delay = min(min_waits)
            values.append(out)
            delays.append(delay)
            cur_wait += delay
        
        """ Fill the public variables """
        self.outputs = values
        self.delays = delays

if __name__ == '__main__':
    ''' test '''
    pulses = (
              (0, 5, 1),
              (1, 6, 1),
              (24, 7, 1),
              (31, 12, 2),
              (1, 13, 1),
              (0, 30, 3),
              (1, 32, 1)
              )
    seq=Sequence()
    seq.sortPulses(pulses)
    for output in seq.outputs:
        print(format(output, '08X'), end=' ')
    print("\ndelays =", seq.delays)    
    
else:
    print("\nImporting... ", __name__)

