# Flow Control

## Conditions

### logical
|             opt 1             |               opt 2               |       |
|-------------------------------|-----------------------------------|-------|
| [ condition1 -a condition2 ]  | [ condition1 ] && [ condition2 ]  | AND   |
| [ condition1 -o condition2 ]  | [ condition1 ] \|\| [ condition2 ]  | OR    |
| [ ! condition ]               |                                   | NOT   |

### commands
|             opt 1             |                                                       |
|-------------------------------|-------------------------------------------------------|
| command1 && command2          | command2 will be executed if command1 returns 0       |
| command1 \|\| command2        | command2 will be executed if command1 returns not 0   |

### integer
x=3 y=7

|     opt 1     |       opt 2       |                   |
|---------------|-------------------|-------------------|
| [ $x -gt $y ] | (( $x > $y ))     | greater than      |
| [ $x -ge $y ] | (( $x >= $y ))    | greater or equal  |
| [ $x -eq $y ] | (( $x == $y ))    | equal             |
| [ $x -ne $y ] | (( $x != $y ))    | not equal         |
| [ $x -le $y ] | (( $x <= $y ))    | less or equal     |
| [ $x -lt $y ] | (( $x < $y ))     | less than         |

### string
x=Hello y=World

|       opt 1       |         opt 2         |         opt 3         |               |
|-------------------|-----------------------|-----------------------|---------------|
|                   | [[ "$x" > "$y" ]]     |                       | greater than  |
| [ "$x" = "$y" ]   | [[ "$x" == "$y" ]]    | [[ "$x" == PATTERN ]] | equal         |
| [ "$x" != "$y" ]  | [[ "$x" != "$y" ]]    | [[ "$x" != PATTERN ]] | greater than  |
|                   | [[ "$x" < "$y" ]]     |                       | less than     |
| [ -z "$y" ]       | [[ -z "$y" ]]         |                       | is empty      |
| [ -n "$y" ]       | [[ -n "$y" ]]         |                       | is not empty  |

### files
f1=file1.txt f2=file2.txt

|       opt 1       |                                                       |
|-------------------|-------------------------------------------------------|
| [ -b $f1 ]        | file exists and is a block special device             |
| [ -c $f1 ]        | file exists and is a character special file           |
| [ -d $f1 ]        | file exists and is a directory                        |
| [ -f $f1 ]        | file exists and is a regular file                     |
| [ -h $f1 ]        | file exists and is a symbolical link                  |
| [ -L $f1 ]        | file exists and is a symbolical link                  |
| [ -p $f1 ]        | file exists and is a named pipe                       |
| [ -S $f1 ]        | file exists and is a UNIX-Domain-Socket               |
| [ -t $f1 ]        |                                                       |
| [ -g $f1 ]        | file exists and the Setgid-Bit is set                 |
| [ -k $f1 ]        | file exists and the Sticky-Bit is set                 |
| [ -r $f1 ]        | file exists and is readable                           |
| [ -u $f1 ]        | file exists and the Setuid-Bit is set                 |
| [ -w $f1 ]        | file exists and is writeable                          |
| [ -x $f1 ]        | file exists and is executable                         |
| [ -O $f1 ]        | file exists and the user is the owner                 |
| [ -G $f1 ]        | file exists and the user has the same GID like $f1    |
| [ -e $f1 ]        | file exists                                           |
| [ -s $f1 ]        | file exists and is not empty                          |
| [ $f1 -ef $f2 ]   |                                                       |
| [ $f1 -nt $f2 ]   | file1 is newer than file2                             |
| [ $f1 -ot $f2 ]   | file1 is older than file2                             |
