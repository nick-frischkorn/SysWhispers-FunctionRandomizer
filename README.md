# SysWhispers-FunctionRandomizer
Quick python script to replace the NtAPI functions within SysWhispers' generated assembly and header files with random strings.

Usage: python3 sw_randomizer.py syscalls.h syscalls.asm

```
C:\Temp>python3 sw_randomizer.py sys.h sys-asm.x64.asm
[+] sys-modified.h Completed!
[+] sys-asm.x64-modified.asm Completed!
[+] NtAPIs and their corresponding value can be found in: changed_log.txt
---
NtWriteVirtualMemory : PHheJHzJrZ
NtProtectVirtualMemory : rFbdzYHSFU
NtOpenProcess : vJpFlKupTc
NtCreateSection : bVFATECoIS
NtMapViewOfSection : vCMJaXuVru
NtQueueApcThread : qaTMRgrBbN
NtResumeThread : mFkJbnVvaU
NtClose : ZgnJFpasBE
NtCreateFile : aBdUnQEcsG
NtUnmapViewOfSection : DiJrtjFaCv
---
[+] NOTE! You must change the header file reference in your SysWhispers .c file to reflect the new header file name!
```
