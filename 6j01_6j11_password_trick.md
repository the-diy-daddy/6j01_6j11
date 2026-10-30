
**Get root access on any 6j01 or 6j11 to fetch/reset u-boot password**
**Current stock firmware has to be lower than R3.2.3, No NAND read/write required**
===========================================

**Reset your router and login using default credentials**

    admin
    Jiocentrum

**set below password as the admin password.**

    Aa1$(passwd${IFS}-d${IFS}root)

**Login back using the same above password**

**Click on the user profile on the top right corner and proceed to change password**

**Set below password as new password**

    Cc2$(killall${IFS}dropbear)

**Login back using the above password**

**Again click on the user profile on the top right corner and proceed to change password**

**Set below password as new password**

    Dd3$(dropbear${IFS}-B)

**after this step you can login into ssh without any password.**

    ssh root@192.168.31.1

**After successful SSH access you can use below methods to flash your router**

**1. For 6j01 (including 6101) use ssh method**

    https://youtu.be/S8LuuL7tme4

or 
        
    https://github.com/the-diy-daddy/6j01_6j11


**2. For 6j11 use uart method**

    https://youtu.be/ODFnTourHYk

or

    https://github.com/the-diy-daddy/6j01_6j11/blob/main/6j11_instructions.md

