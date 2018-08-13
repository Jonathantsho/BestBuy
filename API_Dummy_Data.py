## Use this only for Azure AD service-to-service authentication
from azure.common.credentials import ServicePrincipalCredentials

## Use this only for Azure AD end-user authentication
from azure.common.credentials import UserPassCredentials

## Use this only for Azure AD multi-factor authentication
from msrestazure.azure_active_directory import AADTokenCredentials

## Required for Azure Data Lake Store account management
from azure.mgmt.datalake.store import DataLakeStoreAccountManagementClient
from azure.mgmt.datalake.store.models import DataLakeStoreAccount

## Required for Azure Data Lake Store filesystem management
from azure.datalake.store import core, lib, multithread

# Common Azure imports
from azure.mgmt.resource.resources import ResourceManagementClient
from azure.mgmt.resource.resources.models import ResourceGroup

## Use these as needed for your application
import logging, getpass, pprint, uuid, time

## Declare variables
subscriptionId = ######
adlsAccountName = ########

## Create a filesystem client object
adlsFileSystemClient = core.AzureDLFileSystem( store_name=adlsAccountName)

adlsFileSystemClient.mkdir('/transformationV2')


## Upload a file
multithread.ADLUploader(adlsFileSystemClient, 
                        lpath='C:\\data\\mysamplefile.txt', 
                        rpath='/mysampledirectory/mysamplefile.txt', 
                        nthreads=64, 
                        overwrite=True, buffersize=4194304, 
                        blocksize=4194304)
