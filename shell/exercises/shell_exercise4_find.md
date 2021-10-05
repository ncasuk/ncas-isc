<!-- JavaScript Bundle with Popper -->
<head>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
    </head>
    <body>
      <div class="container">
Exercise 4: Needle in a haystack

AIM
Use find and grep to find the "Needle".
Issues covered
Commands: find, grep.
Instructions
1. Find the file "needle.txt" in the "acsoe" directory.
a.	Change directory to acsoe.
b.	Use the find command to look for the file called "needle.txt".
2. Expand your search to look for files with needle anywhere in the filename.
a.	Same again but use a * or two 
3. Use grep to find the word needle in the files under "acsoe/ease-96/Jetstream".
4. Use the man page for grep to work out how to do a case insensitive search for needle. 
5. Use grep on the "js960724.ps2" file to print all lines without 1 in. (use the man page to find the right option)
6. Use grep on the "js960724.ps2" file to print all lines without 4 or 6 in, but does contain 33. (use a pipes to chain grep commands together)








 
Solution 4: Needle in a haystack
1.
workshop_shell$ cd acsoe
acsoe$ find . -name needle.txt
./hillcloud-96/h2/needle.txt
2.
acsoe$ find . -name '*needle*'
./ease-96/jetstream/ddddd.needle.xxx
./hillcloud-96/h2/needle.txt
3.
acsoe$ cd ease-96/jetstream
jetstream$ grep needle *
js960719.nx7:201.453308  105246 needle   2.2  .1  2.1    0   2.15    1
4.
jetstream$ grep -i needle *
js960716.jn3:198.520544    122935   26.6   .0126 NEEDLE
js960719.nx7:201.453308  105246 needle   2.2  .1  2.1    0   2.15    1
5.
jetstream$ grep -v 1 js960724.ps2 
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
