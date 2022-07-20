# Description

Path resolver is a small helper program for working with system paths. The application can be useful if you often work with server style path on windows or something similar.

# Functional

Path resolver have several function like:

* ## Reverse slashes

    Return string with reversed slashes.

    Arg:
        ```
        //dataserver/some/other/dirs
        ```

    Return:
        ```
        \\dataserver\some\other\dirs
        ```

* ## Get Filename

    Returns only filename with it extension.

    Arg:
        ```
        //dataserver/some/other/dirs/foo.txt
        ```

    Return:
        ```
        foo.txt
        ```

* ## Get Path

    Returns only path to file.

    Arg:
        ```
        //dataserver/some/other/dirs/foo.txt
        ```

    Return:
        ```
        //dataserver/some/other/dirs/
        ```

* ## Get Formatted string

    Returns string ready to paste in code.

    Arg:
        ```
        \\dataserver\some\other\dirs\foo.txt
        ```

    Return:
        ```
        "\\\\dataserver\\some\\other\\dirs\\foo.txt"
        ```

# Use application without GUI

To use path resolver in console mode, simply type in console:

    path_resolver -p C:/path/to/file -f reverse

arg *-f* have four different flags to work with.

|  flag    |    function          |
|----------|----------------------|
| reverse  | reverse slashes      |
| filename | get filename         |
| pathonly | get path only        |
| fstring  | get formatted string |