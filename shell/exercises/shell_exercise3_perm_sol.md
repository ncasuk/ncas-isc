
 
# Solution 3: Permissions

1. 1-4)

        $ cd acsoe/freetex-98/Jungfrau
        Jungfrau$ ls -l
        total 33064
        -rwxr-x---  1 sjp23  staff   183188 26 Feb 16:21 jf980314.em3
        -rwxr-x---  1 sjp23  staff   291474 26 Feb 16:21 jf980315.em1
        -rwxr-x---  1 sjp23  staff   200955 26 Feb 16:21 jf980315.em2
        -rwxr-x---  1 sjp23  staff    31641 26 Feb 16:21 jf980317.nox
        …

        Jungfrau$ ./set_chmod.sh 
        Jungfrau$ ls -l
        total 33064
        -rwx------  1 sjp23  staff   183188 26 Feb 16:21 jf980314.em3
        ----rwx---  1 sjp23  staff   291474 26 Feb 16:21 jf980315.em1
        -------rwx  1 sjp23  staff   200955 26 Feb 16:21 jf980315.em2
        -rwxrwx---  1 sjp23  staff    31641 26 Feb 16:21 jf980317.nox


1. 6) No user permission…

        $ more jf980315.em2
        jf980315.em2: Permission denied
        $ more jf980315.em1
        jf980315.em1: Permission denied

    Read permission ok…

        $ more jf980318.pr1
        24 1001
        Monks, Paul and Zanis, Prodromos
        School of Chemistry, Univesrity Leicester, Leicester, UK
        Peroxy Radical Chemical Amplifier II, Free Tropospheric Experiment II, Jungfraujoch, Switzerland
        FREETEX '98

    Execute permission ok… but not really something you can execute!

        $ ./jf980318.fm1
        ./jf980318.fm1: line 1: 24: command not found
        ./jf980318.fm1: line 2: Graham: command not found
        ./jf980318.fm1: line 3: syntax error near unexpected token `('
        ./jf980318.fm1: line 3: `School of Environmental Sciences, University of East Anglia (UEA), Norwich, UK'

