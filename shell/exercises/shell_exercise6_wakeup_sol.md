| [Questions](shell_exercise6_wakeup.md) | [Exercise list](shell_exercise_index.md) |
 
# Solution 6: Wake up

1.

        $ wc -l $(find shell/acsoe -type f) |sort -n  |tail -4| head -1
        14421 shell/acsoe/eae-97/macehead/mh970427.cn1

2.

        $ X=$(wc -l $(find shell/acsoe -type f) |sort -n  |tail -4| head -1)


3. 

        $ echo $X
        14421 shell/acsoe/eae-97/macehead/mh970427.cn1


 
1. Find the number of Macehead Ozone files in the `acsoe` directory. These files have a `.o31` extension.

        $ ls -l
        total 0
        drwxr-xr-x  12 sam.pepler  staff  384 26 Aug 12:32 acsoe
        drwxr-xr-x  31 sam.pepler  staff  992  6 Oct 10:10 exercises
        drwxr-xr-x   5 sam.pepler  staff  160 26 Aug 12:32 pain
        drwxr-xr-x  26 sam.pepler  staff  832  6 Oct 14:05 presentations
        $ find acsoe -name "*.o31" |wc 
            58      58    2061

2. Find the number of these files that have an `E-MAIL-CONTACT` line set. 

        $ cat $(find acsoe -name "*.o31") | grep E-MAIL-CONTACT| wc
            58      58    1915
    
    They all have an email contact!

3. See how many different email contacts there are for these files by sorting your output.  

        $ cat $(find acsoe -name "*.o31") | grep E-MAIL-CONTACT| sort | uniq
         E-MAIL-CONTACT=b.bandy@uea.ac.uk
        E-MAIL-CONTACT=B.Bandy@UEA.AC.UK
        E-MAIL-CONTACT=b.bandy@uea.ac.uk

4. How many different email contacts in all the files under the `acsoe` directory. 

        $ cat $(find acsoe -type f) | grep E-MAIL-CONTACT| sort | uniq |wc
            67      67    2751

5. Are they really different?

        $ cat $(find acsoe -type f) | grep E-MAIL-CONTACT| sort | uniq  
        E-MAIL-CONTACT=M.Bassford@bristol.ac.uk    
        E-MAIL-CONTACT=M.Bassford@bristol.ac.uk         
        E-MAIL-CONTACT=M.Bassford@bristol.ac.uk              
        E-MAIL-CONTACT=b.bandy@uea.ac.uk
        E-MAIL-CONTACT=B.Bandy@UEA.AC.UK
        E-MAIL-CONTACT=GRENFEJL@novell2.bham.ac.uk
        E-MAIL-CONTACT=GRENFEJL@novell2.bham.ac.uk    
        E-MAIL-CONTACT=JDJ563@novell2.bham.ac.uk
        E-MAIL-CONTACT=M.Bassford@bristol.ac.uk
        E-MAIL-CONTACT=M.Bassford@bristol.ac.uk          
        E-MAIL-CONTACT=M.Bassford@bristol.ac.uk             
        E-MAIL-CONTACT=M.Bassford@bristol.ac.uk                   

    Some of these look similar and some look identical?
         