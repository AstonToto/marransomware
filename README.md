# Marransomware

> This project is purely academic (made in school, period), use at your own risk. I do not encourage in any way the use of this software illegally or to attack targets without their previous authorization.

### Marransomware ?

Yes 'cause 'marrant' means 'funny' in french maybe due to the fact that mine tries some (french) jokes where all your files are locked.

Locked ?

It's sad but yeah, it's a ransomware, a type of malware that prevents or limits users from accessing their system, either by locking the system's screen or by locking the users' files unless a ransom is paid.

This is only an adaptation of jlinoff script in an automated, ransomware-style, locking files use.

### Important

DON'T RUN THIS SCRIPT OR A COMPILED VERSION IN YOUR PERSONAL MACHINE, EXECUTE ONLY IN A TEST ENVIRONMENT!

### Requirements

- PyCrypto to make it work
- Py2exe to compile it

### What happens ?

In Windows only, when launch :

- it locks files in %USERPROFILE% of the sample types
- it asks some (stupid) questions (in french) and you have to answer correctly
- it unlocks the files

Do not exit the window during the questions nor interrupt the crypting process 'cause you'll have to adapt the script to recover your files otherwise.

### Credits

mauri870 for the quotes & jlinoff for the (de)crypting part
