import pytest
from projects.models import Project, ProjectCollaborators
from projects.permissions import (
    IsProjectCollaboratorEditorPermission,
    IsProjectCollaboratorReaderPermission,
)
from pytest_lazy_fixtures import lf
from rest_framework.request import Request
from rest_framework.views import APIView


@pytest.mark.parametrize(
    "permissioned_user",
    [lf("mock_request_full_permission_user")],
)
@pytest.mark.django_db
def test_positive_collaborator_viewer_permission(
    mock_project_nested_viewset: APIView,
    permissioned_user: Request,
    project_collaborator_reader_permission: IsProjectCollaboratorReaderPermission,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
) -> None:
    positive_permission_test = project_collaborator_reader_permission.has_permission(
        permissioned_user, mock_project_nested_viewset
    )
    assert positive_permission_test is True


@pytest.mark.parametrize(
    "permissionless_user", [lf("mock_request_user_without_test_project_access")]
)
@pytest.mark.django_db
def test_negative_collaborator_viewer_permission(
    mock_project_nested_viewset: APIView,
    permissionless_user: Request,
    project_collaborator_reader_permission: IsProjectCollaboratorReaderPermission,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
) -> None:
    negative_permission_test = project_collaborator_reader_permission.has_permission(
        permissionless_user, mock_project_nested_viewset
    )
    assert negative_permission_test is False


@pytest.mark.parametrize(
    "permissioned_user",
    [lf("mock_request_full_permission_user")],
)
@pytest.mark.django_db
def test_positive_project_editor_permission(
    mock_project_nested_viewset: APIView,
    permissioned_user: Request,
    project_instance: Project,
    project_collaborator_editor_permission: IsProjectCollaboratorEditorPermission,
    project_collaborator_editor_instance: ProjectCollaborators,
) -> None:

    positive_permission_test = project_collaborator_editor_permission.has_permission(
        permissioned_user, mock_project_nested_viewset
    )

    assert positive_permission_test is True


@pytest.mark.parametrize(
    "permissionless_user", [lf("mock_request_user_without_test_project_access")]
)
@pytest.mark.django_db
def test_negative_project_editor_permission(
    mock_project_nested_viewset: APIView,
    permissionless_user: Request,
    project_instance: Project,
    project_collaborator_editor_permission: IsProjectCollaboratorEditorPermission,
    project_collaborator_editor_instance: ProjectCollaborators,
) -> None:

    negative_permission_test = project_collaborator_editor_permission.has_permission(
        permissionless_user,
        mock_project_nested_viewset,
    )

    assert negative_permission_test is False
