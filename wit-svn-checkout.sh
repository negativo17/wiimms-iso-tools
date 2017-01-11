#!/bin/sh

REV=7331
svn -r $REV co http://opensvn.wiimm.de/wii/trunk/wiimms-iso-tools/ wit
rm -fr wit/.svn
tar -cjf wit-${REV}svn.tar.bz2 wit
rm -fr wit

