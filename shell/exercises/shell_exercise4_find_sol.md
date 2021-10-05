| [Questions](shell_exercise4_find.md) | [Exercise list](shell_exercise_index.md) |

 
## Solution 4: Needle in a haystack

1.

    $ cd acsoe
    $ find . -name needle.txt
    ./hillcloud-96/h2/needle.txt
2.

    $ find . -name '*needle*'
    ./ease-96/jetstream/ddddd.needle.xxx
    ./hillcloud-96/h2/needle.txt

3.

    $ cd ease-96/jetstream
    $ grep needle *
    js960719.nx7:201.453308  105246 needle   2.2  .1  2.1    0   2.15    1

4.

    $ grep -i needle *
    js960716.jn3:198.520544    122935   26.6   .0126 NEEDLE
    js960719.nx7:201.453308  105246 needle   2.2  .1  2.1    0   2.15    1

5.

    $ grep -v 1 js960724.ps2 
    Lightman Paul
    ACRU Imperial College, TTC, Silwood Park, Ascot, Berks SL5 7PW
    GPS Lat & Long, Barometric Altitude
    ACSOE OXICOA EASE96
    Time in fractional Julian day (GMT Timebase)
    4
    999999 999 999 999
    Time GMT hhmmss
    Latitude  Decimal Degrees
    Longitude Decimal Degrees
    Altitude  m
    5
    THIS-FILE-NAME=js960724.ps2
    E-MAIL-CONTACT=p.lightman@ic.ac.uk
    Jday        Time GMT    Latitude    Longitude   Altitude

6.

    jetstream$ grep -v 4 js960724.ps2 | grep -v 6 | grep 33
    215.5025     120333     53.3098    -10.2228    592.9
    215.5025     120335     53.3102    -10.2205    590.5
    215.5037     120519     53.3332    -10.1023    598.3
    215.5037     120521     53.3337    -10.1001    599.2 
