
# AuthenticateGoogleSheetsAPI

This component authenticates with the Google Sheets API using the Google API Python client and the provided service account credentials (preferably supplied as an environment variable or a JSON file). Returns the authenticated service object.

## Initial generation prompt
description: This component authenticates with the Google Sheets API using the Google
  API Python client and the provided service account credentials (preferably supplied
  as an environment variable or a JSON file). Returns the authenticated service object.
name: AuthenticateGoogleSheetsAPI


## Transformer breakdown
- Load credentials from the provided JSON file or environment variable
- Build the Google Sheets API client with the given credentials, API version, and scope
- Authenticate with the Google Sheets API and return the authenticated service object

## Parameters
[{'name': 'api_version', 'default_value': 'v4', 'description': 'The version of the Google Sheets API to be used for authentication.', 'type': 'string'}, {'name': 'scope', 'default_value': 'https://www.googleapis.com/auth/spreadsheets', 'description': 'The scope for which access permissions are requested from the API.', 'type': 'string'}]

        