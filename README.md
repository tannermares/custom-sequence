Custom sequence (cseq)
=====================

cseq - print a sequence of numbers, with a custom range

Synopsis

seq [OPTION]... LAST RANGE
seq [OPTION]... FIRST LAST RANGE
TODO:seq [OPTION]... FIRST INCREMENT LAST RANGE

Description

Print numbers from FIRST to LAST, across RANGE.

--help
display this help and exit
--version
output version information and exit

If FIRST is omitted, it defaults to nnnn, where n is the first value in RANGE. If LAST is ommitted, it defaults to mmmm, where m is the last value in RANGE.
