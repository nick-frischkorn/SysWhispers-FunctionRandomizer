import sys, string, random

try:
    input_file1 = sys.argv[1]
    input_file2 = sys.argv[2]
except:
    print("--\nYou must specify both the header (.h) and assembly (.asm) files as input!")
    print("Example Usage: python3 sw_randomizer.py sys.h sys.x64.asm\n---")
    sys.exit()


# Initialize output names
if input_file1.__contains__(".h"):
    filename = input_file1.split(".h")
    output_file1 = filename[0]+"-modified.h"
elif input_file1.__contains__(".asm"):
    filename = input_file1.split(".asm")
    output_file1 = filename[0]+"-modified.asm"
else:
    output_file1 = input_file1 + "-modified"

if input_file2.__contains__(".h"):
    filename = input_file2.split(".h")
    output_file2 = filename[0]+"-modified.h"
elif input_file2.__contains__(".asm"):
    filename = input_file2.split(".asm")
    output_file2 = filename[0]+"-modified.asm"
else:
    output_file2 = input_file2 + "-modified"


# Sorted Z-A so that NtAPI's ending in "Ex" will always be checked first
list_of_APIs = ['NtAccessCheck',
                'NtYieldExecution',
                'NtWriteVirtualMemory',
                'NtWriteRequestData',
                'NtWriteFileGather',
                'NtWriteFile',
                'NtWorkerFactoryWorkerReady',
                'NtWaitLowEventPair',
                'NtWaitHighEventPair',
                'NtWaitForWorkViaWorkerFactory',
                'NtWaitForWnfNotifications',
                'NtWaitForSingleObject',
                'NtWaitForMultipleObjects32',
                'NtWaitForMultipleObjects',
                'NtWaitForKeyedEvent',
                'NtWaitForDebugEvent',
                'NtWaitForAlertByThreadId',
                'NtVdmControl',
                'NtUpdateWnfStateData',
                'NtUnsubscribeWnfStateChange',
                'NtUnmapViewOfSectionEx',
                'NtUnmapViewOfSection',
                'NtUnlockVirtualMemory',
                'NtUnlockFile',
                'NtUnloadKeyEx',
                'NtUnloadKey2',
                'NtUnloadKey',
                'NtUnloadDriver',
                'NtUmsThreadYield',
                'NtTranslateFilePath',
                'NtTraceEvent',
                'NtTraceControl',
                'NtThawTransactions',
                'NtThawRegistry',
                'NtTestAlert',
                'NtTerminateThread',
                'NtTerminateProcess',
                'NtTerminateJobObject',
                'NtTerminateEnclave',
                'NtSystemDebugControl',
                'NtSuspendThread',
                'NtSuspendProcess',
                'NtSubscribeWnfStateChange',
                'NtStopProfile',
                'NtStartTm',
                'NtStartProfile',
                'NtSinglePhaseReject',
                'NtSignalAndWaitForSingleObject',
                'NtShutdownWorkerFactory',
                'NtShutdownSystem',
                'NtSetWnfProcessNotificationEvent',
                'NtSetVolumeInformationFile',
                'NtSetValueKey',
                'NtSetUuidSeed',
                'NtSetTimerResolution',
                'NtSetTimerEx',
                'NtSetTimer2',
                'NtSetTimer',
                'NtSetThreadExecutionState',
                'NtSetSystemTime',
                'NtSetSystemPowerState',
                'NtSetSystemInformation',
                'NtSetSystemEnvironmentValueEx',
                'NtSetSystemEnvironmentValue',
                'NtSetSecurityObject',
                'NtSetQuotaInformationFile',
                'NtSetLowWaitHighEventPair',
                'NtSetLowEventPair',
                'NtSetLdtEntries',
                'NtSetIRTimer',
                'NtSetIoCompletionEx',
                'NtSetIoCompletion',
                'NtSetIntervalProfile',
                'NtSetInformationWorkerFactory',
                'NtSetInformationVirtualMemory',
                'NtSetInformationTransactionManager',
                'NtSetInformationTransaction',
                'NtSetInformationToken',
                'NtSetInformationThread',
                'NtSetInformationSymbolicLink',
                'NtSetInformationResourceManager',
                'NtSetInformationProcess',
                'NtSetInformationObject',
                'NtSetInformationKey',
                'NtSetInformationJobObject',
                'NtSetInformationFile',
                'NtSetInformationEnlistment',
                'NtSetInformationDebugObject',
                'NtSetHighWaitLowEventPair',
                'NtSetHighEventPair',
                'NtSetEventBoostPriority',
                'NtSetEvent',
                'NtSetEaFile',
                'NtSetDriverEntryOrder',
                'NtSetDefaultUILanguage',
                'NtSetDefaultLocale',
                'NtSetDefaultHardErrorPort',
                'NtSetDebugFilterState',
                'NtSetContextThread',
                'NtSetCachedSigningLevel2',
                'NtSetCachedSigningLevel',
                'NtSetBootOptions',
                'NtSetBootEntryOrder',
                'NtSerializeBoot',
                'NtSecureConnectPort',
                'NtSavepointTransaction',
                'NtSavepointComplete',
                'NtSaveMergedKeys',
                'NtSaveKeyEx',
                'NtSaveKey',
                'NtRollforwardTransactionManager',
                'NtRollbackTransaction',
                'NtRollbackSavepointTransaction',
                'NtRollbackRegistryTransaction',
                'NtRollbackEnlistment',
                'NtRollbackComplete',
                'NtRevertContainerImpersonation',
                'NtResumeThread',
                'NtResumeProcess',
                'NtRestoreKey',
                'NtResetWriteWatch',
                'NtResetEvent',
                'NtRequestWakeupLatency',
                'NtRequestWaitReplyPort',
                'NtRequestPort',
                'NtRequestDeviceWakeup',
                'NtReplyWaitReplyPort',
                'NtReplyWaitReceivePortEx',
                'NtReplyWaitReceivePort',
                'NtReplyPort',
                'NtReplacePartitionUnit',
                'NtReplaceKey',
                'NtRenameTransactionManager',
                'NtRenameKey',
                'NtRemoveProcessDebug',
                'NtRemoveIoCompletionEx',
                'NtRemoveIoCompletion',
                'NtReleaseWorkerFactoryWorker',
                'NtReleaseSemaphore',
                'NtReleaseMutant',
                'NtReleaseKeyedEvent',
                'NtReleaseCMFViewOwnership',
                'NtRegisterThreadTerminatePort',
                'NtRegisterProtocolAddressInformation',
                'NtRecoverTransactionManager',
                'NtRecoverResourceManager',
                'NtRecoverEnlistment',
                'NtReadVirtualMemory',
                'NtReadRequestData',
                'NtReadOnlyEnlistment',
                'NtReadFileScatter',
                'NtReadFile',
                'NtRaiseHardError',
                'NtRaiseException',
                'NtQueueApcThreadEx',
                'NtQueueApcThread',
                'NtQueryWnfStateNameInformation',
                'NtQueryWnfStateData',
                'NtQueryVolumeInformationFile',
                'NtQueryVirtualMemory',
                'NtQueryValueKey',
                'NtQueryTimerResolution',
                'NtQueryTimer',
                'NtQuerySystemTime',
                'NtQuerySystemInformationEx',
                'NtQuerySystemInformation',
                'NtQuerySystemEnvironmentValueEx',
                'NtQuerySystemEnvironmentValue',
                'NtQuerySymbolicLinkObject',
                'NtQuerySemaphore',
                'NtQuerySecurityPolicy',
                'NtQuerySecurityObject',
                'NtQuerySecurityAttributesToken',
                'NtQuerySection',
                'NtQueryQuotaInformationFile',
                'NtQueryPortInformationProcess',
                'NtQueryPerformanceCounter',
                'NtQueryOpenSubKeysEx',
                'NtQueryOpenSubKeys',
                'NtQueryObject',
                'NtQueryMutant',
                'NtQueryMultipleValueKey',
                'NtQueryLicenseValue',
                'NtQueryKey',
                'NtQueryIoCompletion',
                'NtQueryIntervalProfile',
                'NtQueryInstallUILanguage',
                'NtQueryInformationWorkerFactory',
                'NtQueryInformationTransactionManager',
                'NtQueryInformationTransaction',
                'NtQueryInformationToken',
                'NtQueryInformationThread',
                'NtQueryInformationResourceManager',
                'NtQueryInformationProcess',
                'NtQueryInformationPort',
                'NtQueryInformationJobObject',
                'NtQueryInformationFile',
                'NtQueryInformationEnlistment',
                'NtQueryInformationByName',
                'NtQueryInformationAtom',
                'NtQueryFullAttributesFile',
                'NtQueryEvent',
                'NtQueryEaFile',
                'NtQueryDriverEntryOrder',
                'NtQueryDirectoryObject',
                'NtQueryDirectoryFileEx',
                'NtQueryDirectoryFile',
                'NtQueryDefaultUILanguage',
                'NtQueryDefaultLocale',
                'NtQueryDebugFilterState',
                'NtQueryBootOptions',
                'NtQueryBootEntryOrder',
                'NtQueryAuxiliaryCounterFrequency',
                'NtQueryAttributesFile',
                'NtPulseEvent',
                'NtPullTransaction',
                'NtProtectVirtualMemory',
                'NtPropagationFailed',
                'NtPropagationComplete',
                'NtPrivilegeObjectAuditAlarm',
                'NtPrivilegedServiceAuditAlarm',
                'NtPrivilegeCheck',
                'NtPrePrepareEnlistment',
                'NtPrePrepareComplete',
                'NtPrepareEnlistment',
                'NtPrepareComplete',
                'NtPowerInformation',
                'NtPlugPlayControl',
                'NtOpenTransactionManager',
                'NtOpenTransaction',
                'NtOpenTimer',
                'NtOpenThreadTokenEx',
                'NtOpenThreadToken',
                'NtOpenThread',
                'NtOpenSymbolicLinkObject',
                'NtOpenSession',
                'NtOpenSemaphore',
                'NtOpenSection',
                'NtOpenResourceManager',
                'NtOpenRegistryTransaction',
                'NtOpenProcessTokenEx',
                'NtOpenProcessToken',
                'NtOpenProcess',
                'NtOpenPrivateNamespace',
                'NtOpenPartition',
                'NtOpenObjectAuditAlarm',
                'NtOpenMutant',
                'NtOpenKeyTransactedEx',
                'NtOpenKeyTransacted',
                'NtOpenKeyEx',
                'NtOpenKeyedEvent',
                'NtOpenKey',
                'NtOpenJobObject',
                'NtOpenIoCompletion',
                'NtOpenFile',
                'NtOpenEventPair',
                'NtOpenEvent',
                'NtOpenEnlistment',
                'NtOpenDirectoryObject',
                'NtNotifyChangeSession',
                'NtNotifyChangeMultipleKeys',
                'NtNotifyChangeKey',
                'NtNotifyChangeDirectoryFileEx',
                'NtNotifyChangeDirectoryFile',
                'NtModifyDriverEntry',
                'NtModifyBootEntry',
                'NtMarshallTransaction',
                'NtMapViewOfSectionEx',
                'NtMapViewOfSection',
                'NtMapUserPhysicalPagesScatter',
                'NtMapUserPhysicalPages',
                'NtMapCMFModule',
                'NtManagePartition',
                'NtManageHotPatch',
                'NtMakeTemporaryObject',
                'NtMakePermanentObject',
                'NtLockVirtualMemory',
                'NtLockRegistryKey',
                'NtLockProductActivationKeys',
                'NtLockFile',
                'NtLoadKeyEx',
                'NtLoadKey2',
                'NtLoadKey',
                'NtLoadHotPatch',
                'NtLoadEnclaveData',
                'NtLoadDriver',
                'NtListTransactions',
                'NtListenPort',
                'NtIsUILanguageComitted',
                'NtIsSystemResumeAutomatic',
                'NtIsProcessInJob',
                'NtInitiatePowerAction',
                'NtInitializeRegistry',
                'NtInitializeNlsFiles',
                'NtInitializeEnclave',
                'NtImpersonateThread',
                'NtImpersonateClientOfPort',
                'NtImpersonateAnonymousToken',
                'NtGetWriteWatch',
                'NtGetPlugPlayEvent',
                'NtGetNotificationResourceManager',
                'NtGetNlsSectionPtr',
                'NtGetNextThread',
                'NtGetNextProcess',
                'NtGetMUIRegistryInfo',
                'NtGetDevicePowerState',
                'NtGetCurrentProcessorNumberEx',
                'NtGetCurrentProcessorNumber',
                'NtGetContextThread',
                'NtGetCompleteWnfStateSubscription',
                'NtGetCachedSigningLevel',
                'NtFsControlFile',
                'NtFreezeTransactions',
                'NtFreezeRegistry',
                'NtFreeVirtualMemory',
                'NtFreeUserPhysicalPages',
                'NtFlushWriteBuffer',
                'NtFlushVirtualMemory',
                'NtFlushProcessWriteBuffers',
                'NtFlushKey',
                'NtFlushInstructionCache',
                'NtFlushInstallUILanguage',
                'NtFlushBuffersFileEx',
                'NtFlushBuffersFile',
                'NtFindAtom',
                'NtFilterTokenEx',
                'NtFilterToken',
                'NtFilterBootOption',
                'NtExtendSection',
                'NtEnumerateValueKey',
                'NtEnumerateTransactionObject',
                'NtEnumerateSystemEnvironmentValuesEx',
                'NtEnumerateKey',
                'NtEnumerateDriverEntries',
                'NtEnumerateBootEntries',
                'NtEnableLastKnownGood',
                'NtDuplicateToken',
                'NtDuplicateObject',
                'NtDrawText',
                'NtDisplayString',
                'NtDisableLastKnownGood',
                'NtDeviceIoControlFile',
                'NtDeleteWnfStateName',
                'NtDeleteWnfStateData',
                'NtDeleteValueKey',
                'NtDeletePrivateNamespace',
                'NtDeleteObjectAuditAlarm',
                'NtDeleteKey',
                'NtDeleteFile',
                'NtDeleteDriverEntry',
                'NtDeleteBootEntry',
                'NtDeleteAtom',
                'NtDelayExecution',
                'NtDebugContinue',
                'NtDebugActiveProcess',
                'NtCreateWorkerFactory',
                'NtCreateWnfStateName',
                'NtCreateWaitCompletionPacket',
                'NtCreateWaitablePort',
                'NtCreateUserProcess',
                'NtCreateTransactionManager',
                'NtCreateTransaction',
                'NtCreateTokenEx',
                'NtCreateToken',
                'NtCreateTimer2',
                'NtCreateTimer',
                'NtCreateThreadEx',
                'NtCreateThread',
                'NtCreateSymbolicLinkObject',
                'NtCreateSemaphore',
                'NtCreateSectionEx',
                'NtCreateSection',
                'NtCreateResourceManager',
                'NtCreateRegistryTransaction',
                'NtCreateProfileEx',
                'NtCreateProfile',
                'NtCreateProcessEx',
                'NtCreateProcess',
                'NtCreatePrivateNamespace',
                'NtCreatePort',
                'NtCreatePartition',
                'NtCreatePagingFile',
                'NtCreateNamedPipeFile',
                'NtCreateMutant',
                'NtCreateMailslotFile',
                'NtCreateLowBoxToken',
                'NtCreateKeyTransacted',
                'NtCreateKeyedEvent',
                'NtCreateKey',
                'NtCreateJobSet',
                'NtCreateJobObject',
                'NtCreateIRTimer',
                'NtCreateIoCompletion',
                'NtCreateFile',
                'NtCreateEventPair',
                'NtCreateEvent',
                'NtCreateEnlistment',
                'NtCreateEnclave',
                'NtCreateDirectoryObjectEx',
                'NtCreateDirectoryObject',
                'NtCreateDebugObject',
                'NtCreateCrossVmEvent',
                'NtConvertBetweenAuxiliaryCounterAndPerformanceCounter',
                'NtContinueEx',
                'NtContinue',
                'NtConnectPort',
                'NtCompressKey',
                'NtCompleteConnectPort',
                'NtCompareTokens',
                'NtCompareSigningLevels',
                'NtCompareObjects',
                'NtCompactKeys',
                'NtCommitTransaction',
                'NtCommitRegistryTransaction',
                'NtCommitEnlistment',
                'NtCommitComplete',
                'NtCloseObjectAuditAlarm',
                'NtClose',
                'NtClearSavepointTransaction',
                'NtClearEvent',
                'NtClearAllSavepointsTransaction',
                'NtCancelWaitCompletionPacket',
                'NtCancelTimer2',
                'NtCancelTimer',
                'NtCancelSynchronousIoFile',
                'NtCancelIoFileEx',
                'NtCancelIoFile',
                'NtCancelDeviceWakeupRequest',
                'NtCallEnclave',
                'NtCallbackReturn',
                'NtAssociateWaitCompletionPacket',
                'NtAssignProcessToJobObject',
                'NtAreMappedFilesTheSame',
                'NtApphelpCacheControl',
                'NtAlpcSetInformation',
                'NtAlpcSendWaitReceivePort',
                'NtAlpcRevokeSecurityContext',
                'NtAlpcQueryInformationMessage',
                'NtAlpcQueryInformation',
                'NtAlpcOpenSenderThread',
                'NtAlpcOpenSenderProcess',
                'NtAlpcImpersonateClientOfPort',
                'NtAlpcImpersonateClientContainerOfPort',
                'NtAlpcDisconnectPort',
                'NtAlpcDeleteSecurityContext',
                'NtAlpcDeleteSectionView',
                'NtAlpcDeleteResourceReserve',
                'NtAlpcDeletePortSection',
                'NtAlpcCreateSecurityContext',
                'NtAlpcCreateSectionView',
                'NtAlpcCreateResourceReserve',
                'NtAlpcCreatePortSection',
                'NtAlpcCreatePort',
                'NtAlpcConnectPortEx',
                'NtAlpcConnectPort',
                'NtAlpcCancelMessage',
                'NtAlpcAcceptConnectPort',
                'NtAllocateVirtualMemoryEx',
                'NtAllocateVirtualMemory',
                'NtAllocateUuids',
                'NtAllocateUserPhysicalPages',
                'NtAllocateReserveObject',
                'NtAllocateLocallyUniqueId',
                'NtAlertThreadByThreadId',
                'NtAlertThread',
                'NtAlertResumeThread',
                'NtAdjustTokenClaimsAndDeviceGroups',
                'NtAdjustPrivilegesToken',
                'NtAdjustGroupsToken',
                'NtAddDriverEntry',
                'NtAddBootEntry',
                'NtAddAtomEx',
                'NtAddAtom',
                'NtAcquireProcessActivityReference',
                'NtAcquireCMFViewOwnership',
                'NtAccessCheckByTypeResultListAndAuditAlarmByHandle',
                'NtAccessCheckByTypeResultListAndAuditAlarm',
                'NtAccessCheckByTypeResultList',
                'NtAccessCheckByTypeAndAuditAlarm',
                'NtAccessCheckByType',
                'NtAccessCheckAndAuditAlarm',
                'NtAcceptConnectPort',
                ]

# Function to generate random value
def genkey():
    letters = string.ascii_letters
    key = ""
    for i in range(10):
        z = random.choice(letters)
        key = key + z
    return key


# Populate dictionary with NtAPI and random value pair
api_hash_dict = {}
for i in list_of_APIs:
    api_hash_dict[i] = genkey()


# list to keep track of what APIs we are changing and corresponding value
changed_api_list = [""]


# Iterate through first input file and change NtAPI to random value
output1 = open(output_file1, 'w')
newline = ""

syscall_file1 = open(input_file1, 'r').readlines()
for i in syscall_file1:
    for api in list_of_APIs:
        if api in i:

            newline = i.replace(api, api_hash_dict.get(api))
            output1.write(newline)
            i = ""

            # If the API isn't already in the list (since .asm files will contain it 2x) append it
            # We only perform this on the first file as the second file should have identical NtAPIs.
            for append_api in changed_api_list:
                if api not in changed_api_list:
                    changed_api_list.append(api)
            break # NtAPIs ending in "Ex" will be checked first and break to avoid duplicates

    if i != "":
        output1.write(i)

output1.close()
print("[+] " + output_file1 + " Completed!")


# Iterate through second input file and change NtAPI to random value
output2 = open(output_file2, 'w')
newline = ""

syscall_file2 = open(input_file2, 'r').readlines()
for i in syscall_file2:
    for api in list_of_APIs:
        if api in i:

            newline = i.replace(api, api_hash_dict.get(api))
            output2.write(newline)
            i = ""
            break # NtAPIs ending in "Ex" will be checked first and break to avoid duplicates

    if i != "":
        output2.write(i)

output2.close()
print("[+] " + output_file2 + " Completed!")


# Write to output file what APIs we changed and the corresponding value
change_log = open("changed_log.txt", 'w')
print("[+] " + "NtAPIs and their corresponding value can be found in: changed_log.txt")
print("---")
for i in changed_api_list:
    try:
        logger = i + " : " + api_hash_dict.get(i)
        print(logger)
        change_log.write(logger)
    except:
        pass
print("---")
print("[+] NOTE! You must change the header file reference in your SysWhispers .c file to reflect the new header file name!")








