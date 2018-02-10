# MessWithDevs

Wind up people that leave their computers unattended, they should probably learn
if they haven't already!

## What does it do?

Ever noticed how a greek question mark, `;`, looks a lot like a semicolon, `;`,
and thought that this little coincidence could play havoc with compiling and
running code?

Probably not, but we had. We also took it further than necessary, by changing a
host of common operators and even more common characters to their indistinguishable
doppelgangers. The idea being that after running MessWithDevs on someone else's
code they will get a bunch, nay shittonne, of compiler errors and will have no
idea why!

Cruel right? Well we thought so too, so we have added a reversing method so they
don't lose their jobs. I know, boring, but probably for the best.

## How?

To start messing with people, install on their machine with

  `pip install MessWithDevs`

Run the following command to break their code:

  `mwd _filename_`

and the following to reverse it:

  `mwd _filename_ -r`.

Simple.

Enjoy!

### Other stuff

This only works for python version 3.* unless you want to figure out a way to
make it work with older versions, but why would anyone use 2.* anyway?
