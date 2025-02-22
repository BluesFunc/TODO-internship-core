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
    "permissioned_user,permissionless_user",
    [
        (
            (
                lf("mock_request_full_permission_user"),
                lf("mock_request_user_without_test_project_access"),
            )
        )
    ],
)
@pytest.mark.django_db
def test_project_viewer_permission(
    mock_project_nested_viewset: APIView,
    permissioned_user: Request,
    permissionless_user: Request,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
) -> None:
    permission = IsProjectCollaboratorReaderPermission()

    negative_permission_test = permission.has_permission(
        permissionless_user,
        mock_project_nested_viewset,
    )

    positive_permission_test = permission.has_permission(
        permissioned_user, mock_project_nested_viewset
    )

    assert negative_permission_test is False
    assert positive_permission_test is True


@pytest.mark.parametrize(
    "permissioned_user,permissionless_user",
    [
        (
            (
                lf("mock_request_full_permission_user"),
                lf("mock_request_user_without_test_project_access"),
            )
        )
    ],
)
@pytest.mark.django_db
def test_project_editor_permission(
    mock_project_nested_viewset: APIView,
    permissioned_user: Request,
    permissionless_user: Request,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
) -> None:
    permission = IsProjectCollaboratorEditorPermission()

    negative_permission_test = permission.has_permission(
        permissionless_user,
        mock_project_nested_viewset,
    )

    positive_permission_test = permission.has_permission(
        permissioned_user, mock_project_nested_viewset
    )

    assert negative_permission_test is False
    assert positive_permission_test is True
