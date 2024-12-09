#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

if __name__ == '__main__':
    # initialize window
    stdkeys.create_window()

    keyboard = "q2we4r5ty7u8i9op-[=]"
    Guitar_Strings = []
    plucked_strings = set()
    for i in range(20):
        Guitar_Strings.append(GuitarString(440 * (1.059463**(i-12))))

    n_iters = 0
    while True:
        # it turns out that the bottleneck is in polling for key events
        # for every iteration, so we'll do it less often, say every 
        # 1000 or so iterations
        if n_iters == 1000:
            stdkeys.poll()
            n_iters = 0
        n_iters += 1

        # check if the user has typed a key; if so, process it
        if stdkeys.has_next_key_typed():
            key = stdkeys.next_key_typed()
            counter = 0
            for i in keyboard:
                if i == key:
                    Guitar_Strings[counter].pluck()
                    Guitar_Strings[counter].modify_ticks(0)
                    plucked_strings.add(Guitar_Strings[counter])
                    continue
                counter += 1

        sample = 0
        temp = plucked_strings.copy()
        for i in temp:
            sample += i.sample()
            i.tick()
            if i.time() >= 176400:
                plucked_strings.remove(i)
                temp = plucked_strings.copy()
                
        # play the sample on standard audio
        play_sample(sample)