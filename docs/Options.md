# Options

E-mail configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_offset** | **int, none_type** | By how long should an e-mail be delayed (in minutes). Maximum is 35 days. | [optional] 
**pool_name** | **str** | Name of your custom IP Pool to be used in the sending process | [optional] 
**channel_name** | **str** | Name of selected channel. | [optional] 
**encoding** | **dict** | 0 for None, 1 for Raw7Bit, 2 for Raw8Bit, 3 for QuotedPrintable, 4 for Base64 (Default), 5 for Uue note that you can also provide the text version such as \&quot;Raw7Bit\&quot; for value 1. NOTE: Base64 or QuotedPrintable is recommended if you are validating your domain(s) with DKIM. | [optional] 
**track_opens** | **bool** | Should the opens be tracked? If no value has been provided, Account&#39;s default setting will be used. | [optional] 
**track_clicks** | **bool** | Should the clicks be tracked? If no value has been provided, Account&#39;s default setting will be used. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


