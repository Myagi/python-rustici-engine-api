# coding: utf-8

# flake8: noqa
"""
    Rustici Engine API

    Rustici Engine API  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.about_schema import AboutSchema
from swagger_client.models.activity_result_schema import ActivityResultSchema
from swagger_client.models.comment_schema import CommentSchema
from swagger_client.models.completion_amount_schema import CompletionAmountSchema
from swagger_client.models.connector_content_item_schema import ConnectorContentItemSchema
from swagger_client.models.connector_content_list_entry_schema import ConnectorContentListEntrySchema
from swagger_client.models.connector_content_list_schema import ConnectorContentListSchema
from swagger_client.models.connector_content_search_context_schema import ConnectorContentSearchContextSchema
from swagger_client.models.connector_content_search_schema import ConnectorContentSearchSchema
from swagger_client.models.connector_list_schema import ConnectorListSchema
from swagger_client.models.connector_schema import ConnectorSchema
from swagger_client.models.connector_type_schema import ConnectorTypeSchema
from swagger_client.models.course_activity_schema import CourseActivitySchema
from swagger_client.models.course_connector_schema import CourseConnectorSchema
from swagger_client.models.course_list_non_paged_schema import CourseListNonPagedSchema
from swagger_client.models.course_list_schema import CourseListSchema
from swagger_client.models.course_reference_schema import CourseReferenceSchema
from swagger_client.models.course_schema import CourseSchema
from swagger_client.models.create_connector_schema import CreateConnectorSchema
from swagger_client.models.create_dispatch_id_schema import CreateDispatchIdSchema
from swagger_client.models.create_dispatch_list_schema import CreateDispatchListSchema
from swagger_client.models.create_dispatch_schema import CreateDispatchSchema
from swagger_client.models.create_registration_schema import CreateRegistrationSchema
from swagger_client.models.credential_created_schema import CredentialCreatedSchema
from swagger_client.models.credential_list_schema import CredentialListSchema
from swagger_client.models.credential_request_schema import CredentialRequestSchema
from swagger_client.models.credential_schema import CredentialSchema
from swagger_client.models.destination_id_schema import DestinationIdSchema
from swagger_client.models.destination_list_schema import DestinationListSchema
from swagger_client.models.destination_schema import DestinationSchema
from swagger_client.models.dispatch_id_list_schema import DispatchIdListSchema
from swagger_client.models.dispatch_id_schema import DispatchIdSchema
from swagger_client.models.dispatch_list_schema import DispatchListSchema
from swagger_client.models.dispatch_lti_info_schema import DispatchLtiInfoSchema
from swagger_client.models.dispatch_registration_count_schema import DispatchRegistrationCountSchema
from swagger_client.models.dispatch_schema import DispatchSchema
from swagger_client.models.enabled_schema import EnabledSchema
from swagger_client.models.form_data_import_file import FormDataImportFile
from swagger_client.models.id_list_schema import IdListSchema
from swagger_client.models.import_ad_hoc_reference_request_schema import ImportAdHocReferenceRequestSchema
from swagger_client.models.import_connector_request_schema import ImportConnectorRequestSchema
from swagger_client.models.import_fetch_request_schema import ImportFetchRequestSchema
from swagger_client.models.import_job_result_schema import ImportJobResultSchema
from swagger_client.models.import_media_file_reference_request_schema import ImportMediaFileReferenceRequestSchema
from swagger_client.models.import_reference_request_schema import ImportReferenceRequestSchema
from swagger_client.models.import_request_schema import ImportRequestSchema
from swagger_client.models.import_result_schema import ImportResultSchema
from swagger_client.models.integer_result_schema import IntegerResultSchema
from swagger_client.models.item_value_pair_schema import ItemValuePairSchema
from swagger_client.models.launch_history_list_schema import LaunchHistoryListSchema
from swagger_client.models.launch_history_schema import LaunchHistorySchema
from swagger_client.models.launch_link_request_schema import LaunchLinkRequestSchema
from swagger_client.models.launch_link_schema import LaunchLinkSchema
from swagger_client.models.launch_page_response_schema import LaunchPageResponseSchema
from swagger_client.models.learner_preference_schema import LearnerPreferenceSchema
from swagger_client.models.learner_schema import LearnerSchema
from swagger_client.models.link_schema import LinkSchema
from swagger_client.models.lti_reporter_id_schema import LtiReporterIdSchema
from swagger_client.models.lti_reporter_schema import LtiReporterSchema
from swagger_client.models.media_file_metadata_schema import MediaFileMetadataSchema
from swagger_client.models.message_schema import MessageSchema
from swagger_client.models.metadata_schema import MetadataSchema
from swagger_client.models.o_auth_credentials_schema import OAuthCredentialsSchema
from swagger_client.models.objective_schema import ObjectiveSchema
from swagger_client.models.pii_deletion_request_result_schema import PIIDeletionRequestResultSchema
from swagger_client.models.pii_deletion_request_schema import PIIDeletionRequestSchema
from swagger_client.models.pii_deletion_result_schema import PIIDeletionResultSchema
from swagger_client.models.permissions_schema import PermissionsSchema
from swagger_client.models.ping_schema import PingSchema
from swagger_client.models.plugin_version_schema import PluginVersionSchema
from swagger_client.models.post_back_schema import PostBackSchema
from swagger_client.models.refresh_connector_result_list_schema import RefreshConnectorResultListSchema
from swagger_client.models.refresh_connector_result_schema import RefreshConnectorResultSchema
from swagger_client.models.registration_instancing_schema import RegistrationInstancingSchema
from swagger_client.models.registration_list_schema import RegistrationListSchema
from swagger_client.models.registration_schema import RegistrationSchema
from swagger_client.models.reporting_plugin_schema import ReportingPluginSchema
from swagger_client.models.response_error_schema import ResponseErrorSchema
from swagger_client.models.runtime_interaction_schema import RuntimeInteractionSchema
from swagger_client.models.runtime_objective_schema import RuntimeObjectiveSchema
from swagger_client.models.runtime_schema import RuntimeSchema
from swagger_client.models.score_schema import ScoreSchema
from swagger_client.models.setting_list_schema import SettingListSchema
from swagger_client.models.settings_individual_schema import SettingsIndividualSchema
from swagger_client.models.settings_post_schema import SettingsPostSchema
from swagger_client.models.shared_data_entry_schema import SharedDataEntrySchema
from swagger_client.models.static_properties_schema import StaticPropertiesSchema
from swagger_client.models.string_result_schema import StringResultSchema
from swagger_client.models.tenant_list_schema import TenantListSchema
from swagger_client.models.tenant_schema import TenantSchema
from swagger_client.models.title_schema import TitleSchema
from swagger_client.models.token_info_schema import TokenInfoSchema
from swagger_client.models.token_request_schema import TokenRequestSchema
from swagger_client.models.update_connector_schema import UpdateConnectorSchema
from swagger_client.models.update_dispatch_schema import UpdateDispatchSchema
from swagger_client.models.user_count_detail_schema import UserCountDetailSchema
from swagger_client.models.user_count_summary_schema import UserCountSummarySchema
from swagger_client.models.xapi_account import XapiAccount
from swagger_client.models.xapi_activity import XapiActivity
from swagger_client.models.xapi_activity_definition import XapiActivityDefinition
from swagger_client.models.xapi_agent_group import XapiAgentGroup
from swagger_client.models.xapi_attachment import XapiAttachment
from swagger_client.models.xapi_context import XapiContext
from swagger_client.models.xapi_context_activity import XapiContextActivity
from swagger_client.models.xapi_credential_auth_type_schema import XapiCredentialAuthTypeSchema
from swagger_client.models.xapi_credential_permissions_level_schema import XapiCredentialPermissionsLevelSchema
from swagger_client.models.xapi_credential_post_schema import XapiCredentialPostSchema
from swagger_client.models.xapi_credential_put_schema import XapiCredentialPutSchema
from swagger_client.models.xapi_credential_schema import XapiCredentialSchema
from swagger_client.models.xapi_credentials_list_schema import XapiCredentialsListSchema
from swagger_client.models.xapi_endpoint_schema import XapiEndpointSchema
from swagger_client.models.xapi_interaction_component import XapiInteractionComponent
from swagger_client.models.xapi_result import XapiResult
from swagger_client.models.xapi_score import XapiScore
from swagger_client.models.xapi_self_sourced_pipe_schema import XapiSelfSourcedPipeSchema
from swagger_client.models.xapi_statement import XapiStatement
from swagger_client.models.xapi_statement_pipe_list_schema import XapiStatementPipeListSchema
from swagger_client.models.xapi_statement_pipe_post_schema import XapiStatementPipePostSchema
from swagger_client.models.xapi_statement_pipe_put_schema import XapiStatementPipePutSchema
from swagger_client.models.xapi_statement_pipe_schema import XapiStatementPipeSchema
from swagger_client.models.xapi_statement_reference import XapiStatementReference
from swagger_client.models.xapi_statement_result import XapiStatementResult
from swagger_client.models.xapi_verb import XapiVerb