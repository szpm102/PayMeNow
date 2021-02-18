from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    location = 'media-test'
    file_overwrite = False